import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# Set destination folder for the output
# (must end with '/' or be empty)
output_dir = "Source/Images/"


# Area
plotname = "Area"
labels = [
    "Business",
    "Life",
    "Computer",
    "Social",
    "Physical"
]
web_hits_per_day_means = [
    97.5026251466547,
    46.6719117823716,
    40.7990616728854,
    61.1283855315268,
    39.1768414327089
]
web_hits_per_day_medians = [
    68.3113043478261,
    29.8797767282095,
    28.6781651376147,
    28.0968992248062,
    24.0927460092948
]
overall_mean = 48.0151966575709
overall_median = 29.4331527591751
fig, axs = plt.subplots(2, 1)
# Plot with means
axs[0].bar(labels, web_hits_per_day_means, label="Means")
axs[0].axhline(y = overall_mean, color = "red")
# Plot with medians
axs[1].bar(labels, web_hits_per_day_medians, label="Medians")
axs[1].axhline(y = overall_median, color = "red")
plt.savefig(output_dir+plotname.replace(" ", "")+"Plot.pdf")


# Associated Tasks
plotname = "Associated Tasks"
labels = [
    "Regression",
    "Clustering",
    "Classification",
    "Causal-Discovery"
]
web_hits_per_day_medians = [
    42.0281437125749,
    38.2255683546754,
    29.4000559666687,
    24.8001854197506
]
overall_median = 29.7893674150147
plt.bar(labels, web_hits_per_day_medians)
plt.axhline(y = overall_median, color="red")
plt.savefig(output_dir+plotname.replace(" ", "")+"Plot.pdf")


# Attribute Characteristics
plotname = "Attribute Characteristics"
labels = [
    "Real",
    "Integer",
    "Categorical"
]
web_hits_per_day_medians = [
    32.7393798449612,
    28.9011627906977,
    16.8981441519206
]
overall_median = 29.5409562727882
plt.axhline(y = overall_median, color="red")
plt.bar(labels, web_hits_per_day_medians)
plt.savefig(output_dir+plotname.replace(" ", "")+"Plot.pdf")


# Data Set Characteristics
plotname = "Data Set Characteristics"
labels = [
    "Time-Series",
    "Univariate",
    "Multivariate",
    "Sequential",
    "Text",
    "Domain-Theory"
]
web_hits_per_day_medians = [
    36.1556072953046,
    31.1440015568176,
    29.8434876210980,
    29.1660219774022,
    25.8350659191781,
    18.5250873149915
]
overall_median = 28.9655858084115
plt.axhline(y = overall_median, color="red")
plt.bar(labels, web_hits_per_day_medians)
plt.savefig(output_dir+plotname.replace(" ", "")+"Plot.pdf")


# Missing Values
plotname = "Missing Values"
labels = [
    "Yes",
    "No"
]
web_hits_per_day_medians = [
    32.0568887958992,
    16.2583589372854
]
overall_median = 26.4095238095238
plt.axhline(y = overall_median, color="red")
plt.bar(labels, web_hits_per_day_medians)
plt.savefig(output_dir+plotname.replace(" ", "")+"Plot.pdf")
