def SMA(data, period):
    return data.rolling(window=period).mean()