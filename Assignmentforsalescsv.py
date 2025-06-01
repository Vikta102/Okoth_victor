import pandas as pd

df_sales = pd.read_csv('Sales.csv')

df_sales['Customer Name'] = df_sales['Customer Name'].fillna('Unknown')

df_sales['Quantity'] = df_sales['Quantity'].fillna(0)  
df_sales['Unit Price'] = df_sales['Unit Price'].fillna(df_sales['Unit Price'].median())

df_sales['Total Revenue'] = df_sales['Quantity'] * df_sales['Unit Price']

df_sales['Order Date'] = df_sales['Order Date'].str.replace("'", "")
df_sales['Order Date'] = pd.to_datetime(df_sales['Order Date'], format='mixed')

df_sales = df_sales.drop_duplicates(subset=['Order ID'], keep='first')

df_sales['Quantity'] = df_sales['Quantity'].abs()

df_sales['Total Revenue'] = df_sales['Quantity'] * df_sales['Unit Price']

df_sales.to_csv('Cleaned_Sales.csv', index=False)