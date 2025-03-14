def EMA(data, period):
    return data.ewm(span=period, adjust=False).mean()