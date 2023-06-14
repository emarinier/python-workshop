import pandas as pd
import matplotlib.pyplot as plt

def substitutions(canada_visitors):

    # Rename country column
    canada_visitors = canada_visitors.rename(columns={"Country of residence": "Country"})

    # Set index:
    canada_visitors = canada_visitors.set_index("Country")

    # North America is a special case.
    # Let's add a row that reflects visitors from North America:
    north_america = canada_visitors.loc[[
        "North America, countries other than the United States of America",
        "United States of America residents entering Canada"]].sum()
    north_america.name = "North America"
    north_america = north_america.to_frame().transpose()
    canada_visitors = pd.concat([canada_visitors, north_america])

    return canada_visitors


canada_visitors = pd.read_csv("Canada_visitors.csv")
canada_visitors = substitutions(canada_visitors)

# Select a specific month (May 2022):
monthly_visitors = canada_visitors[["2022-05"]]
monthly_visitors = monthly_visitors.rename(columns={"2022-05": "Visitors"})

# Build the region labels:
regions = ["North America", "South America", "Europe", "Africa", "Asia", "Oceania", "Antarctica"]

# Build the region counts:
counts = []

for region in regions:
    count = monthly_visitors.loc[region]["Visitors"]
    counts.append(count)

# Build the plot:
plt.close("all")
fig, ax = plt.subplots()

ax.bar(regions, counts)
ax.set_ylabel("visitors")
ax.set_title("Visitors to Canada by Region (May 2022)")
ax.set_yscale("log")  # Log scale because the counts are orders of magnitude different.

plt.minorticks_off()
plt.xticks(rotation=45, ha='right')  # Rotates x-axis labels.
plt.subplots_adjust(bottom=0.30)  # Makes room for x-axis labels.

plt.savefig("canada_visitors_by_region.png")
#plt.show()
