import pandas as pd

def mk2():
    df = pd.read_csv('population.csv', usecols=['City','Density KM2'])
    return df.head(10).dropna()