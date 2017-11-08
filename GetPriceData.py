import quandl

quandl.ApiConfig.api_key = ""

# price data for Boeing Co.
price_data = quandl.get_table('WIKI/PRICES', ticker='BA', date={'gte': '2016-01-01', 'lte': '2016-12-31'}, paginate=True)

# key words for Boeing Co.
# ['boeing', 'Dennis Muilenburg', 'Raymond Conner', 'William Boeing', 'Aviall', 'Jeppesen', 'aircraft', 'aerospace',
# '737', '747', '757', '777', '787', '']



