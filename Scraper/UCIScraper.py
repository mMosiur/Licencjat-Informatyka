from bs4 import BeautifulSoup
from requests import get


class UCIScraper:
	def __init__(self, verbose: bool = True) -> None:
		self.verbose = verbose
		# self.base_url = "https://archive.ics.uci.edu/ml/"
		self.base_url = "https://web.archive.org/web/20071229225652/http://archive.ics.uci.edu/ml/"
		# self.links_location = "datasets.php"
		self.links_location = "datasets.html"
		return

	def log(self, msg: str, end="\n") -> None:
		if not self.verbose:
			return
		print(msg, end=end)

	def get_headers(self) -> tuple:
		return (
			"Name",							# string
			"Data Set Characteristics",		# string
			"Attribute Characteristics",  # string
			"Associated Tasks",				# string
			"Number of Instances",			# number
			"Number of Attributes",			# number
			"Missing Values",				# boolean
			"Area",							# string
			"Date Donated",					# date
			"Number of Web Hits",			# number
			"Number of Citations"			# number
		)

	def add_headers(self, data: list) -> dict:
		return dict(zip(self.get_headers(), data))

	def get_database_links(self):
		url = self.base_url + self.links_location
		self.log("Downloading links from: {}".format(url))
		soup = BeautifulSoup(get(url).text, features="lxml")
		self.log("Links downloaded")
		tab = soup.body.find_all("table")[1].find_all(
			"table", recursive=True)[3]
		for tr in tab.find_all("tr", recursive=False)[1:]:
			a = tr.td.find_all("a", recursive=True, href=True)[1]
			link = a["href"]
			name = a.contents[0]
			yield (name, self.base_url+link)

	def get_databases(self):
		links = tuple(self.get_database_links())
		for db in self.get_databases(links):
			yield db

	def get_databases_from_links(self, links):
		count = len(links)
		for index, (name, link) in enumerate(links):
			self.log("Getting database {} out of {} ... ".format(
				index+1, count), end="")
			soup = BeautifulSoup(get(link).text, features="lxml")
			try:
				tab = soup.body.find_all("table")[3]
				citations = soup.find(
					text="Papers That Cite This Data Set", recursive=True)
				nof_citations = 0 if citations is None else (
					len(citations.parent.parent.find_next("p").find_all("br")) // 2)
				db_data = [
					name,
					str(tab.find_all("tr")[0].find_all("td")[1].p.contents[0].strip("\"")),
					str(tab.find_all("tr")[1].find_all("td")[1].p.contents[0].strip("\"")),
					str(tab.find_all("tr")[2].find_all("td")[1].p.contents[0].strip("\"")),
					str(tab.find_all("tr")[0].find_all("td")[3].p.contents[0].strip("\"")),
					str(tab.find_all("tr")[1].find_all("td")[3].p.contents[0].strip("\"")),
					str(tab.find_all("tr")[2].find_all("td")[3].p.contents[0].strip("\"")),
					str(tab.find_all("tr")[0].find_all("td")[5].p.contents[0].strip("\"")),
					str(tab.find_all("tr")[1].find_all("td")[5].p.contents[0].strip("\"")),
					str(tab.find_all("tr")[2].find_all("td")[5].p.contents[0].strip("\"")),
					str(nof_citations)
				]
				for i in range(len(db_data)):
					if db_data[i] == "N/A":
						db_data[i] = ""
				self.log("Loaded")
				yield self.add_headers(db_data)
			except Exception as e:
				self.log("Exception in database {} - {}".format(link, e))


def generate_links_file(filename: str) -> None:
	scraper = UCIScraper()
	with open(filename, "w", encoding="utf-8") as out:
		links = tuple(scraper.get_database_links())
		print("Name\tLink", file=out)
		for name, link in links:
			print(name, link, sep="\t", file=out)


def generate_databases_file(filename: str) -> None:
	scraper = UCIScraper()
	with open(filename, "w", encoding="utf-8") as out:
		headers = scraper.get_headers()
		print("\t".join(headers), file=out, flush=True)
		for db in scraper.get_databases():
			print("\t".join(db.values()), file=out, flush=True)
	print("Finished")


def generate_databases_file_from_linksfile(filename: str, links_filename: str) -> None:
	scraper = UCIScraper()
	links = []
	with open(links_filename, "r", encoding="utf-8") as links_file:
		links = links_file.read().splitlines()[1:]
		for i in range(len(links)):
			links[i] = tuple(links[i].split("\t"))
	with open(filename, "w", encoding="utf-8") as out:
		headers = scraper.get_headers()
		print("\t".join(headers), file=out, flush=True)
		for db in scraper.get_databases_from_links(links):
			print("\t".join(db.values()), file=out, flush=True)
	print("Finished")




if __name__ == "__main__":
	generate_links_file("2007links.tsv")
	# generate_databases_file("2007databases.tsv") # Links to databases are downloaded
	generate_databases_file_from_linksfile("2007databases.tsv", "2007links.tsv") # Links to databases are imported from file
