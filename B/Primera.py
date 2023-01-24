import pandas as pd

df = pd.read_csv("population.csv", usecols=['City','Population'], nrows=10)
print(df)