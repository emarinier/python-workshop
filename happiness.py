import pandas as pd
import plotly.express as px

pd.set_option('display.max_rows', 300)

# World Happiness 2021
world_happiness_2021 = pd.read_csv("world-happiness-report-2021.csv")
world_happiness_2021 = world_happiness_2021.rename(columns={"Country name": "Country",
                                                            "Ladder score": "Ladder 2021"})

# Name fixes (matching codes names):
world_happiness_2021["Country"] = world_happiness_2021["Country"].replace({"Venezuela": "Venezuela, Bolivarian Rep. of",
                                                                            "Libya": "Libyan Arab Jamahiriya",
                                                                            "Sudan": "Sudan, The Republic of",
                                                                            "South Sudan": "South Sudan, The Republic of",
                                                                            "Iran": "Iran, Islamic Rep. of",
                                                                            "Russia": "Russian Federation",
                                                                            "South Korea": "Korea, Republic of",
                                                                            "Taiwan": "Taiwan, China",
                                                                            "Tanzania": "Tanzania, United Republic of",
                                                                            "Congo (Brazzaville)": "Congo",
                                                                            "Laos": "Lao People's Dem. Rep.",
                                                                            "Vietnam": "Viet Nam",
                                                                            "Ivory Coast": "Côte d'Ivoire"})

# Codes
countries_codes = pd.read_csv("countries_codes.csv", sep=";", usecols=["ISO3 CODE", "LABEL EN"])
countries_codes = countries_codes.rename(columns={"ISO3 CODE": "ISO3", "LABEL EN": "Country"})

combined_2021 = pd.merge(world_happiness_2021, countries_codes, how="inner", on="Country")

# Figure
fig = px.choropleth(combined_2021, locations="ISO3", locationmode="ISO-3",
                    color='Ladder 2021',
                    color_continuous_scale="Viridis",
                    title="World Happiness 2021",
                    labels={'Ladder 2021':'Score'})

fig.update_layout(margin={"r":0,"t":30,"l":0,"b":0})
fig.write_image("happiness-2021.png")
fig.write_html("happiness-2021.html")


# World Happiness 2010
world_happiness_2010 = pd.read_csv("world-happiness-report.csv")
world_happiness_2010 = world_happiness_2010.rename(columns={"Country name": "Country",
                                                            "Life Ladder": "Ladder 2010"})
world_happiness_2010 = world_happiness_2010[world_happiness_2010["year"] == 2010]

# Name fixes (matching codes names):
world_happiness_2010["Country"] = world_happiness_2010["Country"].replace({"Venezuela": "Venezuela, Bolivarian Rep. of",
                                                                            "Libya": "Libyan Arab Jamahiriya",
                                                                            "Sudan": "Sudan, The Republic of",
                                                                            "South Sudan": "South Sudan, The Republic of",
                                                                            "Iran": "Iran, Islamic Rep. of",
                                                                            "Russia": "Russian Federation",
                                                                            "South Korea": "Korea, Republic of",
                                                                            "Taiwan": "Taiwan, China",
                                                                            "Tanzania": "Tanzania, United Republic of",
                                                                            "Congo (Brazzaville)": "Congo",
                                                                            "Laos": "Lao People's Dem. Rep.",
                                                                            "Vietnam": "Viet Nam",
                                                                            "Ivory Coast": "Côte d'Ivoire"})


combined_2010_2021 = pd.merge(world_happiness_2010[["Country", "Ladder 2010"]],
                         world_happiness_2021[["Country", "Ladder 2021"]],
                         how="inner", on="Country")

combined_2010_2021 = pd.merge(combined_2010_2021,
                         countries_codes[["Country", "ISO3"]],
                         how="inner", on="Country")

combined_2010_2021["Change"] = combined_2010_2021["Ladder 2021"] - combined_2010_2021["Ladder 2010"]

# Figure
fig = px.choropleth(combined_2010_2021, locations="ISO3", locationmode="ISO-3",
                    color='Change',
                    color_continuous_scale="RdBu_r",
                    range_color=(-2, 2),
                    title="Change in World Happiness from 2010 to 2021",
                    labels={'Change':'Change'})

fig.update_layout(margin={"r":0,"t":30,"l":0,"b":0})
fig.write_image("happiness-change.png")
fig.write_html("happiness-change.html")
#fig.show()
