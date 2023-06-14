"""
QUESTION 1: Number of Visitors Entering Canada by Month

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


# Load the command line argument:
canada_visitors_filepath = sys.argv[1]

#  Check that the passed filepath exists:
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

# Non-resident visitors entering Canada
all_visitors = canada_visitors.loc["Non-resident visitors entering Canada"].fillna(0)

dates = list(all_visitors.index)
visitors = list(all_visitors)

# Plot the visitors:
plt.close("all")
fig, ax = plt.subplots()

# ----------
# Configure the plot.
# ----------

ax.plot(dates, visitors)
ax.set(xlabel="month", ylabel="visitors", title="Visitors to Canada by Month")
ax.xaxis.set_major_locator(plt.MaxNLocator(15))
fig.autofmt_xdate(rotation=45)

# Create the plot:
plt.savefig("canada_visitors_by_month.png")
#plt.show()  # Useful for running on some systems.
