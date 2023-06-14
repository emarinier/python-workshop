# Hints

- Converting a series to a transposed DataFrame: `north_america = north_america.to_frame().transpose()`
- Concatinating DataFrames: `canada_visitors = pd.concat([canada_visitors, north_america])`
- Log scale: `ax.set_yscale("log")`
- Disabling minor ticks: `plt.minorticks_off()`
