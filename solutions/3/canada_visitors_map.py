"""
QUESTION 3: Map of Monthly Visitors Entering Canada

USAGE:

python questions/3/canada_visitors_map.py data/Canada_visitors.csv data/countries_codes.csv

OUTPUT:

A PNG file named "canada_visitors_map.png" and an interactable HTML
file named "canada_visitors_map.html" will be written to the current
directory.

"""

import os
import sys
import math

import pandas as pd
import plotly.express as px


def substitute(canada_visitors):
    """
    Substitute country names in the "Canada_visitors.csv" data. These names are not
    meant to politic statements; just having different data sets match.

    canada_visitors: A pandas DataFrame object that contains the loaded contents of
                     the "Canada_visitors.csv" input file.
    
    Returns: A pandas DataFrame object with some country names substituted, such that
             they match the names in the ISO3 country codes file.
    """

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


# ----
# MAIN
# ----

# Load the Canada visitors filepath command line argument:
canada_visitors_filepath = sys.argv[1]

#  Check that the passed Canada visitors filepath exists:
if not os.path.exists(canada_visitors_filepath):
    print("The passed filepath: " + str(canada_visitors_filepath) + " does not exist!")
    exit(1)

# Load the visitors CSV file:
canada_visitors = pd.read_csv(canada_visitors_filepath)

# Load the country codes filepath command line argument:
countries_codes_filepath = sys.argv[2]

#  Check that the passed country codes filepath exists:
if not os.path.exists(countries_codes_filepath):
    print("The passed filepath: " + str(countries_codes_filepath) + " does not exist!")
    exit(1)

# Load the codes CSV file:
countries_codes = pd.read_csv(countries_codes_filepath, sep=";", usecols=["ISO3 CODE", "LABEL EN"])
countries_codes = countries_codes.rename(columns={"ISO3 CODE": "ISO3", "LABEL EN": "Country"})

# Make necessary substitutions in the data:
canada_visitors = substitute(canada_visitors)

monthly_visitors = canada_visitors["2022-05"]
monthly_visitors.name = "Visitors"
monthly_visitors = monthly_visitors.to_frame()

# Log scale as the US dominates:
monthly_visitors["log(Visitors)"] = monthly_visitors.apply(lambda row : math.log(row["Visitors"], 10) if row["Visitors"] != 0 else 0, axis=1)

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
#fig.show()  # Useful for running on some systems.
