import pandas
import requests
import numpy

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/titanic.csv")
open("titanic.csv", 'wb').write(r.content)

titanic = pandas.read_csv("titanic.csv")
titanic_pivot = pandas.pivot_table(titanic, values="Survived", index="Pclass", columns="Sex", aggfunc=numpy.sum, margins=True)

print(titanic_pivot)

# control = titanic[titanic["Survived"] > 0]
# print(control)