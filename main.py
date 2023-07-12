
# https://app.composer.trade/symphony/XJgqdL5MHtxMU7NRt2jS/details
import generate
import buyingfunc


def sortingFunction(indicator, window_length, number_of_items_to_sort, stockClass = []):
  if indicator=="RSI":
    stocks = []
    for item in stockClass:
      rsi_val = item.get_rsi_value(window_length=window_length)
      stocks.append({"item": item, "val" : rsi_val})

    aa = sorted(stocks,key=lambda x: x.get('val'))
    return aa[number_of_items_to_sort-1]



SPY = generate.StockSymbol("SPY")

PSQ = generate.StockSymbol("PSQ" )

SHY = generate.StockSymbol("SHY")

QQQ =generate.StockSymbol("QQQ")


cp =SPY.get_closing_price()
ccp=  SPY.get_current_price()
df = SPY.get_data_frame()
rsi = SPY.get_rsi(14)
rsi_value = SPY.get_rsi_value(14)
sma = SPY.get_sma(200)
smaVal = SPY.get_sma_value(200)


is_current_price_of_spy_above_200d_moving_average = SPY.get_closing_price() > SPY.get_sma_value(window_length=200)
is_current_price_of_qqq_less_than_20d_moving_average_price_of_qqq = QQQ.get_closing_price() < QQQ.get_sma_value(window_length=20)



def define_logic():
    if is_current_price_of_spy_above_200d_moving_average:
        buyingfunc.buy(symbol="QQQ", qty=1)
    else:
        if QQQ.get_current_price() > QQQ.get_sma_value(window_length=20):
          sorted_items = sortingFunction(indicator="RSI", window_length=10, number_of_items_to_sort=1,stockClass=[PSQ,SPY] )
          for x in sorted_items:
            buyingfunc.buy(symbol= x.get_symbol(),qty=1)
        else:
          buyingfunc.buy(symbol="QQQ",qty=1)




# logic execution take in factors such as time
def execute_logic():
  define_logic()







