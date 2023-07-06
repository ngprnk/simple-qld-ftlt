from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce
from alpaca.trading.client import TradingClient

import config
client = TradingClient(config.API_KEY, config.SECRET_KEY, paper=True)


def buy(symbol="", qty=0, side=OrderSide.BUY, time_in_force=TimeInForce.DAY):
  order_details = MarketOrderRequest(
      symbol=symbol,
      qty=qty,
      side=OrderSide.BUY,
      time_in_force=TimeInForce
    )
  order = client.submit_order(order_data=order_details)
  return order


def sell():
  print("SELLL YOLO")
