import pandas as pd
from statsmodels.tsa.seasonal import STL
import matplotlib.pyplot as plt

df = pd.read_csv("data/generated_station.csv", parse_dates=["date"])
df.set_index("date", inplace=True)

stl = STL(df["vertical_mm"], period=12)
result = stl.fit()

result.plot()
plt.show()

amplitude = result.seasonal.max() - result.seasonal.min()
print("Seasonal amplitude:", round(amplitude, 2), "mm")
