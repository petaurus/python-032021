import pandas
import requests
import numpy

# r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/london_merged.csv")
# open("london_merged.csv", 'wb').write(r.content)

london = pandas.read_csv("london_merged.csv")

london = london.reset_index()
london["timestamp"] = pandas.to_datetime(london["timestamp"])
london["year"] = london["timestamp"].dt.year

london_pivot = pandas.pivot_table(london, index="year", columns="weather_code", values="cnt", aggfunc=numpy.sum,margins=True )

print(london_pivot)
