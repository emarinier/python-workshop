import pandas as pd
import matplotlib.pyplot as plt

canada_visitors = pd.read_csv("Canada_visitors.csv")

canada_visitors = canada_visitors.rename(columns={"Country of residence": "Country"})
canada_visitors = canada_visitors.set_index("Country")

#Non-resident visitors entering Canada
all_visitors = canada_visitors.loc["Non-resident visitors entering Canada"].fillna(0)

dates = list(all_visitors.index)
visitors = list(all_visitors)

# Total visitors by month:
plt.close("all")
fig, ax = plt.subplots()

ax.plot(dates, visitors)
ax.set(xlabel="month", ylabel="visitors", title="Visitors to Canada by Month")
ax.xaxis.set_major_locator(plt.MaxNLocator(12))
fig.autofmt_xdate(rotation=45)

plt.savefig("canada_visitors_by_month.png")
#plt.show()
