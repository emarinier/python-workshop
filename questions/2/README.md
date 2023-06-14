# Question 2: Monthly Visitors Entering Canada by Region

Create a plot showing the number of non-resident visitors entering Canada by region (North America, South America, Europe, Africa, Asia, Oceania, Antarctica) for the month of May 2022. Which region has the most visitors entering Canada and which has the least?

Use pandas to read and manipulate the data, and Matplotlib to create the plot. You may wish to modify the following elements of the plot:

- xlabel, ylabel, and title
- The scale of the y-axis

## Resources

- [Question Starting Point](canada_visitors_by_region.py)
- [Visitors to Canada Data](../../data/Canada_visitors.csv)

## Remarks on the Data

- North America is comprised of two separate entries that will need to be combined:
  - "North America, countries other than the United States of America"
  - "United States of America residents entering Canada"
- There are many NA values in the data.
