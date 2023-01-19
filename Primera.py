import pandas as pd

def pais():
    df = pd.read_csv("df_covid19_countries.csv", nrows=10000)
    pais =  df.groupby(by='location').sum()
    a = pais.loc[:,['date', 'population']]
    return a
#    a = df.loc[:,['location','date', 'population']]
print(pais())