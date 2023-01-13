#All imports listed
import pandas as pnd
import numpy as np
import seaborn as sbn
import matplotlib.pyplot as pyplt

#initializing the data set
data = pd.read_csv(r"C:/Users/anudeephegde/Desktop/DAP/all-states-history.csv")
data.isnull().sum()

sbn.relplot(x="positive", y="recovered", data=data)
