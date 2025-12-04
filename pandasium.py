import pandas as pd

calories = {"Day 1" : 1700, "Day 2" : 2000, "Day 3" : 1960}

series = pd.Series(calories)

print(series)

print(series["Day 1"])

print(series[series < 2000])


