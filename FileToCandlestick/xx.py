file = pd.read_csv('1M_nasdaq_20191201-20191231_1m.csv', infer_datetime_format=True, delimiter=r";")
file['Date'] = pd.to_datetime(file['Date'])
file.set_index('Date', inplace=True)
iday = file.loc['01/12/2019':'01/12/2019':]
mpf.plot(iday, type='candle')