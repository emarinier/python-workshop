import pandas as pd
import json
import plotly.express as px
import math
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', 300)


canada_vistors = pd.read_csv("Canada_visitors.csv")

# Name fixes (matching codes names):
canada_vistors["Country of residence"] = canada_vistors["Country of residence"].replace({"United States of America residents entering Canada": "United States",
                                                                                         "South Africa, Republic of": "South Africa",
                                                                                         "Venezuela": "Venezuela, Bolivarian Rep. of",
                                                                                         "Libya": "Libyan Arab Jamahiriya",
                                                                                         "Sudan": "Sudan, The Republic of",
                                                                                         "South Sudan": "South Sudan, The Republic of",
                                                                                         "Iran": "Iran, Islamic Rep. of",
                                                                                         "Korea, North": "Korea, Dem. People's Rep. of",
                                                                                         "Korea, South": "Korea, Republic of",
                                                                                         "Taiwan": "Taiwan, China",
                                                                                         "Czechia": "Czech Republic",
                                                                                         "Tanzania": "Tanzania, United Republic of",
                                                                                         "Congo, Republic of the": "Congo",
                                                                                         "Laos": "Lao People's Dem. Rep."})
# others?


monthly_visitors = canada_vistors[["Country of residence", "2022-05"]]
monthly_visitors = monthly_visitors.rename(columns={"Country of residence": "Country", "2022-05": "Visitors"})
#print(monthly_visitors)



# Visitors by region
plt.close("all")
fig, ax = plt.subplots()

regions = ["North America", "South America", "Europe", "Africa", "Asia", "Oceania", "Antarctica"]

counts = [
    list(monthly_visitors.loc[monthly_visitors["Country"] == "North America, countries other than the United States of America"]["Visitors"])[0] + \
    list(monthly_visitors.loc[monthly_visitors["Country"] == "United States"]["Visitors"])[0],
    list(monthly_visitors.loc[monthly_visitors["Country"] == "South America"]["Visitors"])[0],
    list(monthly_visitors.loc[monthly_visitors["Country"] == "Europe"]["Visitors"])[0],
    list(monthly_visitors.loc[monthly_visitors["Country"] == "Africa"]["Visitors"])[0],
    list(monthly_visitors.loc[monthly_visitors["Country"] == "Asia"]["Visitors"])[0],
    list(monthly_visitors.loc[monthly_visitors["Country"] == "Oceania"]["Visitors"])[0],
    list(monthly_visitors.loc[monthly_visitors["Country"] == "Antarctica"]["Visitors"])[0]
]

ax.bar(regions, counts)
ax.set_ylabel("Vistors")
ax.set_title("May 2022 Visitors to Canada by Region")
ax.set_yscale("log")
plt.minorticks_off()
plt.xticks(rotation=45, ha='right')
plt.subplots_adjust(bottom=0.30)
plt.savefig("regions.png")


# Total visitors by month:
plt.close("all")
fig, ax = plt.subplots()

#Non-resident visitors entering Canada
all_visitors = canada_vistors.loc[canada_vistors["Country of residence"] == "Non-resident visitors entering Canada"].fillna(0)

dates = all_visitors.columns.values[1:]
visitors = all_visitors.values.tolist()[0][1:]

ax.plot(dates, visitors)
ax.set(xlabel="date", ylabel="visitors", title="Non-Resident Visitors to Canada by Month")
#ax.xaxis.set_major_formatter(plt.NullFormatter())
#ax.xaxis.set_minor_formatter(plt.NullFormatter())
ax.xaxis.set_major_locator(plt.MaxNLocator(12))
#plt.xticks(rotation=45, ha='right')
fig.autofmt_xdate(rotation=45)

#

plt.savefig("all_visitors.png")


#ax.plot(all_visitors)


# Codes
countries_codes = pd.read_csv("countries_codes.csv", sep=";", usecols=["ISO3 CODE", "LABEL EN"])
countries_codes = countries_codes.rename(columns={"ISO3 CODE": "ISO3", "LABEL EN": "Country"})
#print(countries_codes)


# This loses about 40 countries.

#fig = px.choropleth(combined, locations="ISO3", locationmode="ISO-3",
#                    color='Visitors',
#                    color_continuous_scale="Viridis")

# Capping the range so the USA doesn't dominate:

# Need to convert NaN to 0 in visitors column:
monthly_visitors["Visitors"] = monthly_visitors["Visitors"].fillna(0)
#print(monthly_visitors)

# Log scale:
monthly_visitors["log(Visitors)"] = monthly_visitors.apply(lambda row : math.log(row["Visitors"], 10) if row["Visitors"] != 0 else 0, axis=1)


combined = pd.merge(monthly_visitors, countries_codes, how="inner", on="Country")
#print(combined)


fig = px.choropleth(combined, locations="ISO3", locationmode="ISO-3",
                    color='log(Visitors)',
                    color_continuous_scale="Viridis",
                    title="May 2022 Visitors to Canada",
                    labels={'log(Visitors)':'log_10(Visitors)'})

fig.update_layout(margin={"r":0,"t":30,"l":0,"b":0})
fig.write_image("geo.png")
fig.write_html("geo.html")
#fig.show()

