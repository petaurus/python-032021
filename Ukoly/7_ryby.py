import pandas
import requests
import statsmodels.formula.api as smf

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/Fish.csv")
with open("Fish.csv", "wb") as f:
  f.write(r.content)

df = pandas.read_csv("Fish.csv")
print(df.head().to_string())
df["prumer_Species"] = df["Species"].map(df.groupby('Species')['Weight'].mean())
mod = smf.ols(formula="Weight ~ Length2 + Height + prumer_Species", data=df)
res = mod.fit()
print(res.summary())