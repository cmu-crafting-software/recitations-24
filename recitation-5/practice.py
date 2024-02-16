import pandas as pd

# 1. Read the readings and stations csv files using pandas and print them to the screen.
df1 = pd.read_csv('readings.csv')
df2 = pd.read_csv('sensors.csv')
df3 = pd.read_csv('stations_sensors.csv')
df4 = pd.read_csv('stations.csv')
print(df1)
print(df2)
print(df3)
print(df4)

# 2. Print the columns of each dataframe to the screen 
print("Columns in readings:", df1.columns)
print("Columns in sensors:", df2.columns)
print("Columns in stations_sensors:", df3.columns)
print("Columns in stations:", df4.columns)

# 3. Perform an inner join between readings and stations.
df1_indexed = df1.set_index('id') # readings
df4_indexed = df4.set_index('id') # stations
df1_df4_inner_joined = df1_indexed.join(df4_indexed, how='inner')

#4. Print the joined output to the screen
print(df1_df4_inner_joined)

# 5. Join all readings to stations to sensors and print the joined output to the screen. 
# Try out the different types of joins (inner, left, right, and outter).
df2_indexed = df2.set_index('id') # sensors
all_inner_joined = df1_df4_inner_joined.join(df2_indexed, how='inner') #inner joins

# write this to a csv file
all_inner_joined.to_csv('joined_dataframe.csv', index=False)

