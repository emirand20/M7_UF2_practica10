import pandas as pd
import datetime

def fallecidos():
    df = pd.read_csv("df_covid19_countries.csv", nrows=10)
    a = df.loc[:,['reproduction_rate', 'date', 'location']]
    #df['date'] = df['location'].dt.time
    #df.groupby('date').mean()
    return a