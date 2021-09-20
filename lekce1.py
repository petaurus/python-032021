import requests
import pandas

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/sales_plan.csv")
open("sales_plan.csv", 'wb').write(r.content)

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/sales_actual.csv")
open("sales_actual.csv", 'wb').write(r.content)

df_plan = pandas.read_csv("sales_plan.csv")
# print(df_plan.head())
df_plan["sales_plan_cumsum"] = df_plan.groupby("year")["sales"].cumsum() #pribude sloupec s kumulativnimi pocty
# print(df_plan.tail())

df_actual = pandas.read_csv("sales_actual.csv")
df_actual["date"] = pandas.to_datetime(df_actual["date"]) # prevede text v date na datum (vypada stejne)
df_actual["month"] = df_actual["date"].dt.month # prida sloupec, kde vypise cislo mesice
df_actual["year"] = df_actual["date"].dt.year # prida se sloupec, kde je vypsan rok

# print(df_actual.head())

df_actual_grouped = df_actual.groupby(["month", "year"]).sum() # zobrazi se contract_value
df_actual_grouped["sales_actual_cumsum"] = df_actual_grouped["contract_value"].cumsum()
df_actual_grouped = df_actual_grouped.reset_index() #nazvy sloupcu jsou v jedne rovine (stejne typy sloupcu??)

# print(df_actual_grouped.tail())

# print(df_actual.head().to_string()) # zobrazeni vsech sloupcu


df_joined = pandas.merge(df_plan, df_actual_grouped, on=["month", "year"])
df_joined = df_joined.set_index("month")

# print(df_joined.tail())

import matplotlib.pyplot as plt

#ax = df_joined.plot(color="red", y="sales_plan_cumsum", title="Skutecne vs planovane trzby") # ax rika, ze chci graf do existujici plochy
#df_joined.plot(kind="bar", y="sales_actual_cumsum", ax=ax) # graf je kousek posunuty, zkusime jiny typ grafu dole

#df_joined.plot(kind="bar", y=["sales_plan_cumsum", "sales_actual_cumsum"]) # jiny typ grafu nez vyse, ted by mel byt spravne
#plt.show()

#kontingenctni tabulky
#import numpy
#df_actual_pivot = pandas.pivot_table(df_actual, index="country", columns="sales_manager", values="contract_value", aggfunc=numpy.sum) #tabulka kdo je jak uspesny v jake zemi
#print(df_actual_pivot)




#url = ("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/user_registration.json")
#r = requests.get(url)
#open("user_registration.json", 'wb').write(r.content)

data = pandas.read_json ("user_registration.json")
print(data.columns)

data = data.drop_duplicates(subset="email", keep="last")
#data.groupby("date_time").size().cumsum().plot()
# plt.show() # ukaze graf

#data_pivot = pandas.pivot_table(data, index="marketing_channel", columns="age_goup", aggfunc=len, values="email")
data_pivot = pandas.pivot_table(data, index='marketing_channel', columns='age_group', aggfunc=len, values='email')
#print(data_pivot)

# ?????? nekde problem
# #sns.heatmap(data_pivot, annot=True, fmt=".1f")
# sns.heatmap(data_pivot, annot=True, fmt='.1f')
# plt.show()




