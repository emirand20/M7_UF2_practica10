import pandas as pd

def morts():
    df = pd.read_csv("df_covid19_countries.csv", nrows=10)
    a = df.loc[:,['total_deaths','date','location']]
    return a
    