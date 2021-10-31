import requests
import pandas

r = requests.get("https://raw.githubusercontent.com/lutydlitatova/czechitas-datasets/main/datasets/lexikon-zvirat.csv")
open("lexikon-zvirat.csv", "wb").write(r.content)

lexikon = pandas.read_csv("lexikon-zvirat.csv", sep=";")

lexikon = lexikon.dropna(how="all", axis="columns")
lexikon = lexikon.dropna(how="all", axis="rows")
lexikon = lexikon.set_index("id")

def check_url(radek):
    url = radek["image_src"]
    if isinstance(url, str) and url.startswith("https://zoopraha.cz/images/") and url.lower().endswith("jpg"):
        return True

neplatne_url = pandas.DataFrame(columns=["nazev_zvirete"])

for idx, zvire in lexikon.iterrows():
    nazev_zvirete = zvire["title"]
    if not check_url(zvire):
        neplatne_url = neplatne_url.append({"nazev_zvirete": nazev_zvirete}, ignore_index=True)

print(neplatne_url)