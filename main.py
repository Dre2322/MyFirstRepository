stocks_dict = {
  'AAL' : '44.56',
  'IBM' : '60.50',
  'ALF' : '55.78',
  'BIG' : '32.56',
  'TAG' : '65.86',
  'HAP' : '75.90',
  'FOO' : '41.52',
  'CAN' : '89.09',
  'HOP' : '72.89',
  'HIG' : '42.02',
}

x = input('Please enter your stock symbol: ')
z = stocks_dict.get(x, 'Ticker symbol was not found')
print (x,':', z)