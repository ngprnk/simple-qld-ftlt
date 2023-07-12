def sort(indicator, window_length, number_of_items_to_sort, stockClass = []):
  if indicator=="RSI":
    stocks = []
    for item in stockClass:
      rsi_val = item.get_rsi_value(window_length=window_length)
      stocks.append({"item": item, "val" : rsi_val})

    aa = sorted(stocks,key=lambda x: x.get('val'))
    return aa[number_of_items_to_sort-1]
