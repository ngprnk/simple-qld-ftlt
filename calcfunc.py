# Description: This file contains all the functions that are used to calculate
def get_rsi_df_with_df_from_data(dd, window_length):
  # calculation
  dd["diff"] = dd["close"].diff()
  dd['gain'] = dd['diff'].clip(lower=0).round(2)
  dd['loss'] = dd['diff'].clip(upper=0).abs().round(2)
  dd['avg_gain'] = dd['gain'].rolling(
    window=window_length, min_periods=window_length).mean()[:window_length+1]
  dd['avg_loss'] = dd['loss'].rolling(
    window=window_length, min_periods=window_length).mean()[:window_length+1]

  # # average gain
  for i, row in enumerate(dd['avg_gain'].iloc[window_length+1:]):
    dd['avg_gain'].iloc[i + window_length + 1] =\
        (dd['avg_gain'].iloc[i + window_length] *
        (window_length - 1) +
        dd['gain'].iloc[i + window_length + 1])\
        / window_length
  # Average Losses
  for i, row in enumerate(dd['avg_loss'].iloc[window_length+1:]):
      dd['avg_loss'].iloc[i + window_length + 1] =\
          (dd['avg_loss'].iloc[i + window_length] *
          (window_length - 1) +
          dd['loss'].iloc[i + window_length + 1])\
          / window_length

  # rs and rsi
  dd['rs'] = dd['avg_gain'] / dd['avg_loss']
  dd['rsi'] = 100 - (100 / (1.0 + dd['rs']))

  return dd


def get_rsi_value_of_stock_from_df(df):
  return df['rsi'].iloc[-1]









# def calculateRsiOfStock(symbol, dataframe):






