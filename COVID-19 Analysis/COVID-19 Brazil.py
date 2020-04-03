# From Kaggle:
#   "Novel Corona Virus 2019 Dataset"
#   "Day level information on covid-19 affected cases"
#   https://www.kaggle.com/sudalairajkumar/novel-corona-virus-2019-dataset#covid_19_data.csv

import numpy as np
import pandas as pd

dataset_deaths = pd.read_csv("/kaggle/input/novel-corona-virus-2019-dataset/time_series_covid_19_deaths.csv")
dataset_deaths = dataset_deaths.iloc[:].values

dataset_confirmed = pd.read_csv("/kaggle/input/novel-corona-virus-2019-dataset/time_series_covid_19_confirmed.csv")
dataset_confirmed = dataset_confirmed.iloc[:].values

dataset_recovered = pd.read_csv("/kaggle/input/novel-corona-virus-2019-dataset/time_series_covid_19_recovered.csv")
dataset_recovered = dataset_recovered.iloc[:].values

