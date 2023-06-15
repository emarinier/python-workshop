"""
QUESTION 4: Map of World Happiness

USAGE:

python questions/4/happiness.py data/world-happiness-report-2021.csv data/countries_codes.csv

OUTPUT:

A PNG file named "happiness-2021.png" and an interactable HTML
file named "happiness-2021.html" will be written to the current
directory.

"""

import os
import sys
import math

import pandas as pd
import plotly.express as px


# Load the 2021 World Happiness filepath command line argument:
world_happiness_2021_filepath = sys.argv[1]

#  Check that the passed 2021 World Happiness filepath exists:
if not os.path.exists(world_happiness_2021_filepath):
    print("The passed filepath: " + str(world_happiness_2021_filepath) + " does not exist!")
    exit(1)

# Load the World Happiness 2021 CSV:
world_happiness_2021 = pd.read_csv(world_happiness_2021_filepath)
world_happiness_2021 = world_happiness_2021.rename(columns={"Country name": "Country",
                                                            "Ladder score": "Ladder 2021"})

# Load the country codes filepath command line argument:
countries_codes_filepath = sys.argv[2]

#  Check that the passed country codes filepath exists:
if not os.path.exists(countries_codes_filepath):
    print("The passed filepath: " + str(countries_codes_filepath) + " does not exist!")
    exit(1)

# Load the codes CSV file:
countries_codes = pd.read_csv(countries_codes_filepath, sep=";", usecols=["ISO3 CODE", "LABEL EN"])
countries_codes = countries_codes.rename(columns={"ISO3 CODE": "ISO3", "LABEL EN": "Country"})

# Name fixes (matching codes names):
substitutions = {"Venezuela": "Venezuela, Bolivarian Rep. of",
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
                "Ivory Coast": "Côte d'Ivoire"}

# Make the substitutions:
world_happiness_2021["Country"] = world_happiness_2021["Country"].replace(substitutions)

# Merge the DataFrames:
combined_2021 = pd.merge(world_happiness_2021, countries_codes, how="inner", on="Country")

# Build the figure:
fig = px.choropleth(combined_2021, locations="ISO3", locationmode="ISO-3",
                    color='Ladder 2021',
                    color_continuous_scale="Viridis",
                    title="World Happiness 2021",
                    labels={'Ladder 2021':'Score'})

fig.update_layout(margin={"r":0,"t":30,"l":0,"b":0})
fig.write_image("happiness-2021.png")
fig.write_html("happiness-2021.html")
#fig.show()  # Useful for running on some systems.
