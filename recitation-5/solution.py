import pandas as pd
import csv


df_readings = pd.read_csv('readings.csv')
print(df_readings)

df_stations = pd.read_csv('stations.csv')
print(df_stations)

print(df_readings.columns)
print(df_stations.columns)

joined_output = df_readings.set_index('id').join(df_stations.set_index('id'),how='inner')

print(joined_output)