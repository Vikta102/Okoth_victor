import pandas as pd
import numpy as np

df_mine = pd.read_csv('Mine.csv')

numeric_cols = ['Duration', 'Pulse', 'Maxpulse', 'Calories']
for col in numeric_cols:
    df_mine[col] = df_mine[col].fillna(df_mine[col].median())

df_mine = df_mine.dropna(subset=['Date'])


df_mine['Date'] = df_mine['Date'].str.replace("'", "")
df_mine['Date'] = pd.to_datetime(df_mine['Date'], format='mixed')

df_mine = df_mine.drop_duplicates()

df_mine['Duration'] = df_mine['Duration'].clip(upper=120)

median_maxpulse = df_mine['Maxpulse'].median()
df_mine['Maxpulse'] = np.where(df_mine['Maxpulse'] < 120, median_maxpulse, df_mine['Maxpulse'])


df_mine.to_csv('Cleaned_Mine.csv', index=False)