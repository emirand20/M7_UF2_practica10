import pandas as pd

def pais():
    df = pd.read_csv("df_covid19_countries.csv", nrows=10000)
    a = df.loc[:, ['date', 'population']]
    #a = df.loc[:['date', 'population']]
    return a