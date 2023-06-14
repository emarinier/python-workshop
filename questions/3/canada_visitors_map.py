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
    
    Returns: A pandas DataFrame object with the country column renamed and some
             country names substituted, such that they match the names in the ISO3
             country codes file.
    """

    # Name substitutions (matching codes names):
    name_substitutions = {"United States of America residents entering Canada": "United States",
                    "South Africa, Republic of": "South Africa"}
                    # TODO: Many more...


    # ----------
    # TODO:
    # Make the name substitutions.
    # (Optionally) rename the country column.
    # Handle NAs
    # Set the DataFrame index to the country column.
    # ----------

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

# ----------
# TODO:
# Get the monthly visitors for May 2022.
# Combine the monthly visitors and country codes DataFrames.
# Build a choropleth figure from the combined DataFrame.
# ----------

# ----------
# TODO:
#fig.write_image("canada_visitors_map.png")
#fig.write_html("canada_visitors_map.html")
# ----------

#fig.show()  # Useful for running on some systems.
