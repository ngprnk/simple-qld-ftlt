import stockdata
import talib as talib


def pre_generate_data(symbol=""):
  dict = {
      symbol: {
        "dataframe": None,
        "RSI": {
          },
        "SMA": {
          },
        "smavalue": None,
        "current_price": None,
        "closing_price": None
        }
    }

  dict[symbol]["dataframe"]  = stockdata.get_bar_data(symbol)
  dict[symbol]["current_price"]  = stockdata.get_current_price(symbol)[symbol]
  dict[symbol]["closing_price"] = dict[symbol]["current_price"].close
  return dict



class StockSymbol:
  def __init__(self, symbol):
    self.symbol = symbol
    self.data = pre_generate_data(symbol=symbol)


  def get_symbol(self):
    return self.symbol

  def getall(self):
    return self.data

  def get(self, key):
    return self.data[key]

  def get_data_frame(self):
    return self.data[self.symbol]["dataframe"]

  def get_rsi(self, window_length ):
    self.data[self.symbol]["RSI"][window_length]= {}
    self.data[self.symbol]["RSI"][window_length]["items"] =talib.RSI(self.data[self.symbol]["dataframe"]["close"], timeperiod=window_length)
    return self.data[self.symbol]["RSI"][window_length]["items"]


  def get_rsi_value(self, window_length):
    rsi = self.get_rsi(window_length=window_length)
    return self.data[self.symbol]["RSI"][window_length]["items"][-1]

  def get_sma(self, window_length):
     self.data[self.symbol]["SMA"][window_length] = {}
     self.data[self.symbol]["SMA"][window_length]["items"] = talib.SMA(self.data[self.symbol]["dataframe"]["close"], timeperiod=window_length)
     return self.data[self.symbol]["SMA"][window_length]["items"]

  def get_current_price(self):
    return self.data[self.symbol]["current_price"]

  def get_closing_price(self):
    return self.data[self.symbol]["closing_price"]

  def get_sma_value(self, window_length):
    sma = self.get_sma(window_length=window_length)
    return self.data[self.symbol]["SMA"][window_length]["items"][-1]



MSFT = StockSymbol("MSFT")





