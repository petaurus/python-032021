import requests
import pandas
import numpy

# with requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/1976-2020-president.csv") as r:
#   open("1976-2020-president.csv", 'w', encoding="utf-8").write(r.text)

volby = pandas.read_csv("1976-2020-president.csv")
volby['rank']=volby.groupby(["state",'year'])['candidatevotes'].rank(method="min", ascending=False)

prezidenti_vitezove =volby[volby["rank"] == 1]

vitezove_razeni = prezidenti_vitezove.sort_values(["state", "year"])
vitezove_razeni['previous_elections'] = vitezove_razeni.groupby(['state'])["party_simplified"].shift(1)

vitezove_razeni_2 = vitezove_razeni.dropna(subset=['previous_elections']).reset_index(drop=True)
vitezove_razeni_2["compare"] = numpy.where(vitezove_razeni_2["party_simplified"] == vitezove_razeni_2['previous_elections'] , 0, 1)

vysledek = vitezove_razeni_2.groupby(["state"])["compare"].sum()

vyhodnoceni_serazeno = vysledek.sort_values()

print(vyhodnoceni_serazeno)