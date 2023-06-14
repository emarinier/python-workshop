# Question 2: Monthly Visitors Entering Canada by Region

Create a plot showing the number of non-resident visitors entering Canada by region (North America, South America, Europe, Africa, Asia, Oceania, Antarctica) for the month of May 2022. Which region has the most visitors entering Canada and which has the least?

Use pandas to read and manipulate the data, and Matplotlib to create the plot. You may wish to modify the following elements of the plot:

- xlabel, ylabel, and title
- The scale of the y-axis

## Resources

- [Question Starting Point](canada_visitors_by_region.py)
- [Visitors to Canada Data](../../data/Canada_visitors.csv)
- [Pandas DataFrame Sum](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sum.html)
- [Pandas Series to Frame](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_frame.html)
- [Pandas DataFrame Transpose](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.transpose.html)
- [Pandas Concatinating DataFrames](https://pandas.pydata.org/docs/user_guide/merging.html)
- [Matplotlib Bar Charts](https://matplotlib.org/stable/gallery/lines_bars_and_markers/bar_colors.html#sphx-glr-gallery-lines-bars-and-markers-bar-colors-py)
- [Matplotlib Scale](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.yscale.html)

## Remarks on the Data

- North America is comprised of two separate entries that will need to be combined:
  - "North America, countries other than the United States of America"
  - "United States of America residents entering Canada"
- There are many NA values in the data.
