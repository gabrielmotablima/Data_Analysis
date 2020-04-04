# From Kaggle:
#   "Novel Corona Virus 2019 Dataset"
#   "Day level information on covid-19 affected cases"
#   https://www.kaggle.com/sudalairajkumar/novel-corona-virus-2019-dataset#covid_19_data.csv

# Importing the libraries
import numpy as np
import pandas as pd

# Dataset paths
deaths = 'novel-corona-virus-2019-dataset/time_series_covid_19_deaths.csv'
confirmed = 'novel-corona-virus-2019-dataset/time_series_covid_19_confirmed.csv'
recovered = 'novel-corona-virus-2019-dataset/time_series_covid_19_recovered.csv'

# Importing the datasets
dataset_deaths = pd.read_csv(deaths)
dataset_deaths = dataset_deaths.iloc[:].values

dataset_confirmed = pd.read_csv(confirmed)
dataset_confirmed = dataset_confirmed.iloc[:].values

dataset_recovered = pd.read_csv(recovered)
dataset_recovered = dataset_recovered.iloc[:].values

# Getting the Brazil COVID-19 data
for i in range(len(dataset_recovered)):
    if dataset_deaths[i][1] == 'Brazil':
        deaths_brazil = dataset_deaths[i]
    if dataset_confirmed[i][1] == 'Brazil':
        confirmed_brazil = dataset_confirmed[i]
    if dataset_recovered[i][1] == 'Brazil':
        recovered_brazil = dataset_recovered[i]

# An array of 0 up to last registered day
unit_per_day = []
for i in range(len(deaths_brazil[4:])):
    unit_per_day.append(i)
    
##############################################################################################################
from pylab import *
plot(unit_per_day, deaths_brazil[4:], 'red')
plot(unit_per_day, confirmed_brazil[4:], 'orange')
plot(unit_per_day, recovered_brazil[4:], 'green')

xlabel('Unit Day')
ylabel('Red - Deaths\n Orange - Confirmed\n Green - Deaths')
title('Covid-19 in Brazil - Cumulative Chart')
grid(True)
show()


##############################################################################################################
deaths_per_day = []
confirmed_per_day = []
recovered_per_day = []

deaths_per_day.append(0)
confirmed_per_day.append(0)
recovered_per_day.append(0)

for i in range(1, len(deaths_brazil[4:])):
    deaths_per_day.append(deaths_brazil[4+i] - deaths_brazil[3+i])
    confirmed_per_day.append(confirmed_brazil[4+i] - confirmed_brazil[3+i])
    recovered_per_day.append(recovered_brazil[4+i] - recovered_brazil[3+i])

##############################################################################################################
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(len(unit_per_day[-20:]))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects = ax.bar(x, confirmed_per_day[-20:], width, label='confirmed', color = 'orange')

ax.set_ylabel('Orange - Confirmed')
ax.set_title('Covid-19 in Brazil - Occurrences per Day (last 20 days)')
ax.set_xticks(x)
ax.set_xticklabels(unit_per_day)
ax.legend()

def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects)

fig.tight_layout()

plt.show()

##############################################################################################################
x = np.arange(len(unit_per_day[-20:]))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, deaths_per_day[-20:], width, label='deaths', color = 'red')
rects2 = ax.bar(x + width/2, recovered_per_day[-20:], width, label='recovered', color = 'green')

ax.set_ylabel('Red - Deaths\nGreen - Recovered')
ax.set_title('Covid-19 in Brazil - Occurrences per Day (last 20 days)')
ax.set_xticks(x)
ax.set_xticklabels(unit_per_day)
ax.legend()

def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

fig.tight_layout()

plt.show()
