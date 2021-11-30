import requests
import pandas
import statsmodels.formula.api as smf

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/Concrete_Data_Yeh.csv")
with open("Concrete_Data_Yeh.csv", "wb") as f:
  f.write(r.content)

df = pandas.read_csv("Concrete_Data_Yeh.csv")
mod = smf.ols(formula="csMPa ~ cement + slag + flyash + water + superplasticizer + coarseaggregate + fineaggregate + age", data=df)
res = mod.fit()
print(res.summary())

# water ma zaporny koeficient a ovlivnuje silu betonu. Vic vody zpusobi nizsi pevnost beronu