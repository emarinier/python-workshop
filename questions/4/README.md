# Question 4: Map of World Happiness

Create a map showing the world happiness index ("Life Ladder" / "Ladder Score") for each country in 2021. Considering that the data collection is somewhat delayed, are there any observations that you can make?

Use pandas to read and manipulate the data, and plotly express choropleth to create the map.

## Resources

- [Question Starting Point](canada_visitors_map.py)
- [Visitors to Canada Data](../../data/Canada_visitors.csv)
- [Country Codes](../../data/countries_codes.csv)
- [Pandas Replace (dict-like)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.replace.html)
- [Pandas Rename](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rename.html)
- [Pandas fillna](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.fillna.html)
- [Plotly Express Choropleth Maps](https://plotly.com/python/choropleth-maps/)
- [Plotly Colour Scales](https://plotly.com/python/builtin-colorscales/)

## Remarks on the Data

- Many country names need to be changed such that they match the names in the ISO3 codes file. This is a similar process as question 3, but not all of the countries that need to be changed are the same. For example:
  - "Libya": "Libyan Arab Jamahiriya"
  - "Sudan": "Sudan, The Republic of"
  - And many more.
