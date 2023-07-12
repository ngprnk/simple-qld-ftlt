import config
from alpaca.data.requests import StockBarsRequest, StockLatestBarRequest
from alpaca.data.timeframe import TimeFrame
from datetime import datetime, date
from alpaca.data.historical import StockHistoricalDataClient

def get_bar_data(symbol="", timeframe =TimeFrame.Day, start= datetime(2020,1,1), end= datetime(2023,7,1)):
    return config.stock_client.get_stock_bars(
        StockBarsRequest(
            symbol_or_symbols=symbol,
            timeframe=timeframe,
            start=start,
            end=end,
        )
    ).df

def get_latest_bar_data(symbol=""):
    return config.stock_client.get_latest_stock_bar(
        StockLatestBarRequest(
            symbol=symbol
        )
    )


def get_current_price(symbol=""):
    return config.stock_client.get_stock_latest_bar(StockLatestBarRequest(symbol_or_symbols=symbol, limit=1))





