import pandas as pd
from sys import argv

input_path = "databases.tsv"
output_path = "extended_" + input_path
if len(argv) > 1:
    input_path = argv[1]
    output_path = "extended_" + input_path
if len(argv) > 2:
    output_path = argv[2]
if len(argv) > 3:
    print("Wrong number of arguments, use {} [input_path [output_path]]".format(argv[0]))
    exit(1)

data = pd.read_csv(input_path, sep="\t")

# Add a column with the number of days a given data set is available
days_available_label = "Days Available"
if days_available_label not in data.columns:
    #current_date = "2020-11-17"
    current_date = "2007-12-29"
    data.insert(9, days_available_label,
                (pd.to_datetime(current_date) -
                 data["Date Donated"].astype("datetime64")).dt.days
                )

# Add a column with the number of web hits a given data set gets per one day of it being available
number_of_web_hits_per_day_label = "Number of Web Hits per Day"
if number_of_web_hits_per_day_label not in data.columns:
    data.insert(12, number_of_web_hits_per_day_label,
                (pd.to_numeric(data["Number of Web Hits"], downcast="float") /
                 data[days_available_label]).astype(str).replace("nan", "")
                )

# Add a column with the number of citations a given data set gets per one day of it being available
number_of_citations_per_day_label = "Number of Citations per Day"
if number_of_citations_per_day_label not in data.columns:
    data.insert(13, number_of_citations_per_day_label,
                (pd.to_numeric(data["Number of Citations"], downcast="float") /
                 data[days_available_label]).astype(str).replace("nan", "")
                )

data.to_csv(output_path, sep="\t", index=False, float_format='%.f')
