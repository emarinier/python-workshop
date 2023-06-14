"""
USAGE:

python questions/1/canada_visitors_by_month.py data/Canada_visitors.csv

OUTPUT:

A PNG file named "canada_visitors_by_month.png" will be written to the
current directory.

"""

import os
import sys

import pandas as pd
import matplotlib.pyplot as plt


# Check that the passed filepath exists:
canada_visitors_filepath = sys.argv[1]

if not os.path.exists(canada_visitors_filepath):
    print("The passed filepath: " + str(canada_visitors_filepath) + " does not exist!")
    exit(1)

# Load the CSV file:
canada_visitors = pd.read_csv(canada_visitors_filepath)

canada_visitors = canada_visitors.rename(columns={"Country of residence": "Country"})
canada_visitors = canada_visitors.set_index("Country")

# ----------
# Access the non-resident vistors (loc).
# Get the dates and visitors as lists.
# ----------

# Plot the visitors:
plt.close("all")
fig, ax = plt.subplots()

# ----------
# Configure the plot.
# ----------

# Create the plot:
plt.savefig("canada_visitors_by_month.png")
#plt.show()  # Useful for running on some systems.
