#%% Imports
import re
from typing import List

#%% Define patterns
# Pattern tuples: (pattern, replacement)
patterns = (
	(r" ?\\cite\{[^{;]+\}\n?", r""),
	(r"^\s|\t+\n?", r""),
	(r"\\begin\{[^{;]+\}(\[.*\])?(\{.*\})?\n?", r""),
	(r"\\end\{[^{;]+\}\n?", r""),
	(r"\\item\n?", r"-"),
	(r"\\[^{;]+\{([^{;]*)\}\n?", r"\1"),
	(r"(``)|('')\n?", r"\""),
	(r"~", r" "),
	(r"--", r"–"),
)

#%% Define include fetching function
def get_includes_from(filename: str) -> List[str]:
	""" Gets files that are included in given file using \include{<filename>} directive """
	f = open(filename, "r")
	content = f.read()
	f.close()
	return re.findall(r"^\\include\{(.+)\}", content, re.MULTILINE)

#%% Define detexifying function
def detexify(text: str) -> str:
	""" Returns the detexified version of provided text """
	detexified_text = text
	for pattern, replacement in patterns:
		detexified_text = re.sub(pattern, replacement, detexified_text)
	return detexified_text

#%% Detexify includes from root file 
for file in get_includes_from("thesis.tex"):
	f = open(file+".tex", "r")
	content = f.read()
	f.close()
	f = open(file+"_detexified.txt", "w")
	f.write(detexify(content))
	f.close()
