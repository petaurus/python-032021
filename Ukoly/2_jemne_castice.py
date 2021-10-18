import requests
import pandas
import numpy

# with requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/air_polution_ukol.csv") as r:
#  open("air_polution_ukol.csv", 'w', encoding="utf-8").write(r.text)

castice = pandas.read_csv("air_polution_ukol.csv")
castice["date"] = pandas.to_datetime(castice["date"])

castice["year"] = castice["date"].dt.year
castice["month"] = castice["date"].dt.month

castice_pivot = pandas.pivot_table(castice, index="month", columns="year", values="pm25", aggfunc=numpy.mean)

print(castice_pivot)
