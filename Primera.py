import pandas as pd

def pais():
    df = pd.read_csv("df_covid19_countries.csv", nrows=10)
    a = df.loc[:,['location','date', 'population']]
    return a

#print(pais())