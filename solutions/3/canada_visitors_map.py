import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import math

def substitutions(canada_visitors):

    # Name substitutions (matching codes names):
    name_substitutions = {"United States of America residents entering Canada": "United States",
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
                    "Laos": "Lao People's Dem. Rep."}

    # Make the substitutions:
    canada_visitors["Country of residence"] = canada_visitors["Country of residence"].replace(name_substitutions)
    canada_visitors = canada_visitors.rename(columns={"Country of residence": "Country"})
    canada_visitors = canada_visitors.fillna(0)

    # Set index:
    canada_visitors = canada_visitors.set_index("Country")

    return canada_visitors


canada_visitors = pd.read_csv("Canada_visitors.csv")
canada_visitors = substitutions(canada_visitors)

monthly_visitors = canada_visitors["2022-05"]
monthly_visitors.name = "Visitors"
monthly_visitors = monthly_visitors.to_frame()

# Log scale as the US dominates:
monthly_visitors["log(Visitors)"] = monthly_visitors.apply(lambda row : math.log(row["Visitors"], 10) if row["Visitors"] != 0 else 0, axis=1)
# TODO: log visitors of specific month


# Codes
countries_codes = pd.read_csv("countries_codes.csv", sep=";", usecols=["ISO3 CODE", "LABEL EN"])
countries_codes = countries_codes.rename(columns={"ISO3 CODE": "ISO3", "LABEL EN": "Country"})

# Combine the country codes with the country data
combined = pd.merge(monthly_visitors, countries_codes, how="inner", on="Country")

fig = px.choropleth(combined, locations="ISO3", locationmode="ISO-3",
                    color='log(Visitors)',
                    color_continuous_scale="Viridis",
                    title="May 2022 Visitors to Canada",
                    labels={'log(Visitors)':'log_10(Visitors)'})

fig.update_layout(margin={"r":0,"t":30,"l":0,"b":0})
fig.write_image("canada_visitors_map.png")
fig.write_html("canada_visitors_map.html")
#fig.show()
