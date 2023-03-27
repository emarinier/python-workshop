import pandas as pd
import json
import plotly.express as px


"""
with open("geojson-counties-fips.json") as counties_file:
    counties = json.load(counties_file)

df = pd.read_csv("fips-unemp-16.csv", dtype={"fips": str})

fig = px.choropleth(df, geojson=counties, locations='fips', color='unemp',
                    color_continuous_scale="Viridis",
                    range_color=(0, 12),
                    scope="usa",
                    labels={'unemp':'unemployment rate'})

fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.write_image("geo.png")
fig.write_html("geo.html")
"""

pd.set_option('display.max_rows', 300)

canada_vistors = pd.read_csv("Canada_visitors.csv")

# Name fixes:
canada_vistors = canada_vistors.replace("United States of America residents entering Canada", "United States")
canada_vistors = canada_vistors.replace("South Africa, Republic of", "South Africa")
# others?


monthly_visitors = canada_vistors[["Country of residence", "2022-05"]]
monthly_visitors = monthly_visitors.rename(columns={"Country of residence": "Country", "2022-05": "Visitors"})
print(monthly_visitors)

countries_codes = pd.read_csv("countries_codes.csv", sep=";", usecols=["ISO3 CODE", "LABEL EN"])
countries_codes = countries_codes.rename(columns={"ISO3 CODE": "ISO3", "LABEL EN": "Country"})
print(countries_codes)

combined = pd.merge(monthly_visitors, countries_codes, how="inner", on="Country")
print(combined)
# This loses about 40 countries.

#fig = px.choropleth(combined, locations="ISO3", locationmode="ISO-3",
#                    color='Visitors',
#                    color_continuous_scale="Viridis")

# Capping the range so the USA doesn't dominate:
fig = px.choropleth(combined, locations="ISO3", locationmode="ISO-3",
                    color='Visitors',
                    range_color=(0, 10000),
                    color_continuous_scale="Viridis")

fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.write_image("geo.png")
fig.write_html("geo.html")
#fig.show()

