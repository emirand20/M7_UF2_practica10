import pandas as pd

def totalPoblacio():
    df = pd.read_csv("population.csv", usecols=['City','Population'], nrows=10)
    return df