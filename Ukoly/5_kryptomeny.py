# Ukol https://github.com/pesikj/python-032021/blob/master/02_statistika/01/ukol/ukol.ipynb

import requests
import pandas
import statistics
import numpy
import matplotlib.pyplot as plt
import seaborn

# r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/crypto_prices.csv")
# open("crypto_prices.csv", "wb").write(r.content)

crypto_prices = pandas.read_csv("crypto_prices.csv")

# Použij zavírací cenu kryptoměny (sloupec Close) a vypočti procentuální změnu jednotlivých kryptoměn.
# Pozor na to, ať se ti nepočítají ceny mezi jednotlivými měnami. Ošetřit to můžeš pomocí metody groupby(), jako jsme to dělali např. u metody shift().

crypto_prices["Close_next"] = crypto_prices.groupby(["Name"])["Close"].shift(1)
crypto_prices["change"] = crypto_prices["Close"]/crypto_prices["Close_next"]*100-100
crypto_prices = crypto_prices.dropna(subset=["change"])
crypto_prices["pct"] = crypto_prices.groupby(["Name"])["Close"].pct_change()

print(crypto_prices.head().to_string())

# Vytvoř korelační matici změn cen jednotlivých kryptoměn a zobraz je jako tabulku

crypto_prices_pivot = pandas.pivot_table(crypto_prices, index="Date", columns="Symbol", values="pct", aggfunc=numpy.sum)

print(crypto_prices_pivot.corr().to_string())

# V tabulce vyber dvojici kryptoměn s vysokou hodnotou koeficientu korelace a jinou dvojici s koeficientem korelace blízko 0.
# Změny cen pro dvojice měn, které jsou nejvíce a nejméně korelované, si zobraz jako bodový graf.

print(crypto_prices_pivot.corr().abs().min().min())
print(crypto_prices_pivot.corr().abs().min())
print(crypto_prices_pivot.corr().idxmin())

def check_radek(radek):
    radek = radek.sort_values(ascending=False)
    radek = radek.iloc[1]
    return radek

max = 0
max_index = None
for index, radek in crypto_prices_pivot.corr().iterrows():
    result = check_radek(radek)
    if result > max:
        max = result
        max_index = index

#max
seaborn.jointplot("BTC", "WBTC", crypto_prices_pivot.corr(), kind='scatter', color='blue')
#min
seaborn.jointplot("SOL", "USDC", crypto_prices_pivot.corr(), kind='scatter', color='green')
plt.show()

print(max)
print(max_index)

max_sloupec = crypto_prices_pivot.corr()[max_index]
print(max_sloupec[max_sloupec == max])