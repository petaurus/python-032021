import requests
import pandas

r = requests.get("https://raw.githubusercontent.com/lutydlitatova/czechitas-datasets/main/datasets/lexikon-zvirat.csv")
open("lexikon-zvirat.csv", "wb").write(r.content)

lexikon = pandas.read_csv("lexikon-zvirat.csv", sep=";")

lexikon = lexikon.dropna(how="all", axis="columns")
lexikon = lexikon.dropna(how="all", axis="rows")
lexikon = lexikon.set_index("id")

def popisek(radek):
    zvire = radek["title"]
    strava = radek["food"]
    typ_stravy = radek["food_note"]
    znaky_zvirete = radek["description"]
    return f"{zvire} preferuje následující typ stravy: {strava}. Konkrétně ocení když mu do misky přistanou {typ_stravy}. \nJak toto zvíře poznáme: {znaky_zvirete}."

lexikon["popisek"] = lexikon.apply(popisek, axis=1)

print(lexikon["popisek"])

print(lexikon["popisek"][320])
print(lexikon["popisek"][300])