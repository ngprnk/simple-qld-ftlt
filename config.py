from dotenv import dotenv_values
from alpaca.trading.client import TradingClient
from alpaca.data.historical import StockHistoricalDataClient

values = dotenv_values(".env")

API_KEY=values["API_KEY"]
SECRET_KEY=values["SECRET_KEY"]


trading_client = TradingClient(API_KEY, SECRET_KEY, paper=True)

stock_client = StockHistoricalDataClient(API_KEY, SECRET_KEY)


