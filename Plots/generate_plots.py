import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# Set destination folder for the output
# (must end with '/' or be empty)
output_dir = "Source/Images/"

MEDIAN_COLOR = "#5B7EBD"
ALL_MEDIAN_COLOR = "#0000CC"
MEAN_COLOR = "#EE854A"
ALL_MEAN_COLOR = "#CC0000"

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
plt.xlabel("Dziedzina", fontsize = "large")
plt.ylabel("Ilość wyświetleń na dzień", fontsize = "large")
plt.bar(labels, web_hits_per_day_means, label = "Średnia", color = MEAN_COLOR)
plt.bar(labels, web_hits_per_day_medians, label = "Mediana", color = MEDIAN_COLOR)
plt.axhline(y = overall_mean, color = ALL_MEAN_COLOR)
plt.axhline(y = overall_median, color = ALL_MEDIAN_COLOR)
plt.legend()
plt.savefig(output_dir+plotname.replace(" ", "")+"Plot.pdf")
plt.close()


# Associated Tasks
plotname = "Associated Tasks"
labels = [
    "Regression",
    "Clustering",
    "Classification",
    "Causal-Discovery"
]
web_hits_per_day_means = [
    60.8208282923251,
    57.5518400453074,
    47.4435706879225,
    43.9305695604709
]
web_hits_per_day_medians = [
    42.0281437125749,
    38.2255683546754,
    29.4000559666687,
    24.8001854197506
]
overall_mean = 47.8447186857058
overall_median = 29.7893674150147
plt.xlabel("Dziedzina", fontsize = "large")
plt.ylabel("Ilość wyświetleń na dzień", fontsize = "large")
plt.bar(labels, web_hits_per_day_means, label = "Średnia", color = MEAN_COLOR)
plt.bar(labels, web_hits_per_day_medians, label = "Mediana", color = MEDIAN_COLOR)
plt.axhline(y = overall_mean, color = ALL_MEAN_COLOR)
plt.axhline(y = overall_median, color = ALL_MEDIAN_COLOR)
plt.legend()
plt.savefig(output_dir+plotname.replace(" ", "")+"Plot.pdf")
plt.close()


# Attribute Characteristics
plotname = "Attribute Characteristics"
labels = [
    "Real",
    "Integer",
    "Categorical"
]
web_hits_per_day_means = [
    52.4213793303745,
    49.0239619294068,
    27.8513493750351
]
web_hits_per_day_medians = [
    32.7393798449612,
    28.9011627906977,
    16.8981441519206
]
overall_mean = 47.7484250089279
overall_median = 29.5409562727882
plt.xlabel("Dziedzina", fontsize = "large")
plt.ylabel("Ilość wyświetleń na dzień", fontsize = "large")
plt.bar(labels, web_hits_per_day_means, label = "Średnia", color = MEAN_COLOR)
plt.bar(labels, web_hits_per_day_medians, label = "Mediana", color = MEDIAN_COLOR)
plt.axhline(y = overall_mean, color = ALL_MEAN_COLOR)
plt.axhline(y = overall_median, color = ALL_MEDIAN_COLOR)
plt.legend()
plt.savefig(output_dir+plotname.replace(" ", "")+"Plot.pdf")
plt.close()


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
web_hits_per_day_means = [
    61.2964009809620,
    50.8545878809314,
    49.7219830647435,
    44.9979290224581,
    37.2563425344624,
    28.7873251485220
]
web_hits_per_day_medians = [
    36.1556072953046,
    31.1440015568176,
    29.843487621098 ,
    29.1660219774022,
    25.8350659191781,
    18.5250873149915
]
overall_mean = 46.3988901141464
overall_median = 28.9655858084115
plt.xlabel("Dziedzina", fontsize = "large")
plt.ylabel("Ilość wyświetleń na dzień", fontsize = "large")
plt.bar(labels, web_hits_per_day_means, label = "Średnia", color = MEAN_COLOR)
plt.bar(labels, web_hits_per_day_medians, label = "Mediana", color = MEDIAN_COLOR)
plt.axhline(y = overall_mean, color = ALL_MEAN_COLOR)
plt.axhline(y = overall_median, color = ALL_MEDIAN_COLOR)
plt.legend()
plt.savefig(output_dir+plotname.replace(" ", "")+"Plot.pdf")
plt.close()


# Missing Values
plotname = "Missing Values"
labels = [
    "Yes",
    "No"
]
web_hits_per_day_means = [
    49.3893245295069,
    29.8110445027449
]
web_hits_per_day_medians = [
    32.0568887958992,
    16.2583589372854
]
overall_mean = 42.0871552222281
overall_median = 26.4095238095238
plt.xlabel("Dziedzina", fontsize = "large")
plt.ylabel("Ilość wyświetleń na dzień", fontsize = "large")
plt.bar(labels, web_hits_per_day_means, label = "Średnia", color = MEAN_COLOR)
plt.bar(labels, web_hits_per_day_medians, label = "Mediana", color = MEDIAN_COLOR)
plt.axhline(y = overall_mean, color = ALL_MEAN_COLOR)
plt.axhline(y = overall_median, color = ALL_MEDIAN_COLOR)
plt.legend()
plt.savefig(output_dir+plotname.replace(" ", "")+"Plot.pdf")
plt.close()
