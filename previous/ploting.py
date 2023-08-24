import pandas as pd
input = pd.read_csv('input.csv')

input.columns = ['SYMBOL', 'VALUE', 'DAY']

first_row = input.iloc[1]

symbol = first_row['SYMBOL']
value = first_row['VALUE']
day = first_row['DAY']
print(f"Symbol: {symbol}, Value: {value}, Day: {day}")