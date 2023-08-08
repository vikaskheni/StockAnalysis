import yfinance as yf # pip install yfinanc
import pandas as pd

data = yf.download('RELIANCE.NS')

data.to_csv('RELIANCE.CSV')  #gives wholesome data about the realiance

details = pd.read_csv('EQUITY_L.CSV')

print(details.SYMBOL) #gives the name of all listed stock

for name in details.SYMBOL:  #write [0:number of data]
    try:
        data = yf.download(f'{name}.NS')
        data.to_csv(f'./Data/{name}.CSV')
    except Exceptions as e:
        print(f'{name} ===> {e}')