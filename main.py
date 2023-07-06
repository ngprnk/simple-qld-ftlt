from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest, StockLatestBarRequest
from alpaca.data.timeframe import TimeFrame
from datetime import datetime, date
import pandas as pd
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce
from alpaca.trading.client import TradingClient
import config
import calcfunc
import buyingfunc
from dotenv import load_dotenv
load_dotenv()



client = TradingClient(config.API_KEY, config.SECRET_KEY, paper=True)

window_length = 252


# local imports

STOCK_SYMBOLS = ["SPY"]


stock_client = StockHistoricalDataClient(config.API_KEY, config.SECRET_KEY)

spy_request_params = StockBarsRequest(
                        symbol_or_symbols="SPY",
                        timeframe=TimeFrame.Day,
                        start=datetime(2010, 1, 1),
                        end=datetime(2023, 7, 1),
                 )

psq_request_params = StockBarsRequest(
                        symbol_or_symbols="PSQ",
                        timeframe=TimeFrame.Day,
                        start=datetime(2010, 1, 1),
                        end=datetime(2023, 7, 1),
                 )

shy_request_params = StockBarsRequest(
                        symbol_or_symbols="SHY",
                        timeframe=TimeFrame.Day,
                        start=datetime(2010, 1, 1),
                        end=datetime(2023, 7, 1),
                 )

shy_request_params = StockBarsRequest(
                        symbol_or_symbols="QQQ",
                        timeframe=TimeFrame.Day,
                        start=datetime(2010, 1, 1),
                        end=datetime(2023, 7, 1),
                 )

bars_spy = stock_client.get_stock_bars(spy_request_params)
bars_psq = stock_client.get_stock_bars(spy_request_params)
bars_shy = stock_client.get_stock_bars(spy_request_params)
bars_qqq = stock_client.get_stock_bars(spy_request_params)



# convert the bars into data frames
df_spy = bars_spy.df
df_psq = bars_psq.df
df_shy = bars_shy.df
df_qqq = bars_qqq.df



def get_end_moving_average(data_frame, window_length):
    return data_frame["moving average"].rolling(window_length).mean()[len(data_frame.rolling(window_length).mean())-1]


# get moving average
df_spy["moving average"] = df_spy["close"].rolling(200).mean()
df_qqq["moving average"] = df_qqq["close"].rolling(200).mean()

df_psq["diff"] = df_psq["close"].diff()
df_psq['gain'] = df_psq['diff'].clip(lower=0).round(2)




# # get current price of the stock
current_price_spy = stock_client.get_stock_latest_bar(StockLatestBarRequest(symbol_or_symbols="SPY", limit=1))
current_price_qqq = stock_client.get_stock_latest_bar(StockLatestBarRequest(symbol_or_symbols="QQQ", limit=1))

closing_price_spy = current_price_spy["SPY"].close
closing_price_qqq = current_price_qqq["QQQ"].close

print("Get last value from moving average-------------")
print(get_end_moving_average(df_spy, window_length))
print("Get last value from moving average ----- END -----")


is_current_price_of_spy_above_moving_average = closing_price_spy > get_end_moving_average(df_spy, window_length)
is_current_price_of_qqq_less_than_20d_moving_average_price_of_qqq = closing_price_qqq < get_end_moving_average(df_qqq, 20)


df_with_rsi_psq = calcfunc.get_rsi_df_with_df_from_data(df_psq,10)
df_with_rsi_shy  = calcfunc.get_rsi_df_with_df_from_data(df_shy,10)
rsi_value_psq= calcfunc.get_rsi_value_of_stock_from_df(df_with_rsi_psq)
rsi_value_shy = calcfunc.get_rsi_value_of_stock_from_df(df_with_rsi_shy)


selected_stock = ""

if(rsi_value_psq>=rsi_value_psq):
  selected_stock="PSQ"
else:
  selected_stock="SHY"



if(is_current_price_of_spy_above_moving_average):
   orderdata = buyingfunc.buy(symbol="QQQ", qty=1)
else:
  if(is_current_price_of_qqq_less_than_20d_moving_average_price_of_qqq):
    orderdata = buyingfunc.buy(selected_stock, qty=1)
  else:
    orderdata = buyingfunc.buy("QQQ", qty=1)

















