
# https://app.composer.trade/symphony/XJgqdL5MHtxMU7NRt2jS/details
import generate
import buyingfunc
import sorting_util

AMOUNT_ALLOCATED = 50000 # to be implemented
SPY = generate.StockSymbol("SPY")
PSQ = generate.StockSymbol("PSQ" )
SHY = generate.StockSymbol("SHY")
QQQ =generate.StockSymbol("QQQ")

is_current_price_of_spy_above_200d_moving_average = SPY.get_closing_price() > SPY.get_sma_value(window_length=200)
is_current_price_of_qqq_less_than_20d_moving_average_price_of_qqq = QQQ.get_closing_price() < QQQ.get_sma_value(window_length=20)

def define_logic():
    if is_current_price_of_spy_above_200d_moving_average:
        buyingfunc.buy(symbol="QQQ", qty=1)
    else:
        if QQQ.get_current_price() > QQQ.get_sma_value(window_length=20):
          sorted_items = sorting_util.sort(indicator="RSI", window_length=10, number_of_items_to_sort=1,stockClass=[PSQ,SPY] )
          for x in sorted_items:
            buyingfunc.buy(symbol= x.get_symbol(),qty=1)
        else:
          buyingfunc.buy(symbol="QQQ",qty=1)


# logic execution take in factors such as time
def execute_logic():
  define_logic()







