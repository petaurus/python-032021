# Ukol https://github.com/pesikj/python-032021/blob/master/02_statistika/01/ukol/ukol.ipynb

import requests
import pandas
import statistics

pandas.set_option('display.max_columns', None)

# r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/crypto_prices.csv")
# open("crypto_prices.csv", "wb").write(r.content)

crypto = pandas.read_csv("crypto_prices.csv")
crypto["pct_change"] = crypto.groupby("Name")["Close"].pct_change()
crypto["pct_change"] = crypto["pct_change"] + 1

rust = crypto[crypto['Symbol'] == "XMR"].iloc[:,-1].dropna().tolist()
print(statistics.geometric_mean(rust)-1)



