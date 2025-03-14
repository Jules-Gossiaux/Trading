def MACD(data, short_period=12, long_period=26, signal_period=9):
    short_ema = pd.Series(data).ewm(span=short_period, adjust=False).mean()
    long_ema = pd.Series(data).ewm(span=long_period, adjust=False).mean()
    macd = short_ema - long_ema
    signal = macd.ewm(span=signal_period, adjust=False).mean()
    return macd, signal
