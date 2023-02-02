import pandas as pd

def totalPoblacio():
    df = pd.read_csv("population.csv", usecols=['City','Population'])
    return df.head(10).dropna()