import pandas as pd

def M2():
    df = pd.read_csv('population.csv', usecols=['City','Area M2'], nrows=10)
    print(df)