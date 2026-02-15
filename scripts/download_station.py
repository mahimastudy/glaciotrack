import pandas as pd
import numpy as np

# Time range
dates = pd.date_range("2015-01-01", "2020-12-01", freq="MS")

# Long-term uplift (mm)
trend = np.linspace(0, 10, len(dates))

# Seasonal displacement (glacier loading)
seasonal_disp = 5 * np.sin(2 * np.pi * dates.month / 12)

# Temperature seasonal cycle (°C)
# Slight phase shift to simulate melt lag
seasonal_temp = 15 * np.sin(2 * np.pi * (dates.month - 1) / 12)

noise = np.random.normal(0, 0.5, len(dates))

vertical = trend + seasonal_disp + noise

df = pd.DataFrame({
    "date": dates,
    "vertical_mm": vertical,
    "temp_c": seasonal_temp
})

df.to_csv("data/generated_station.csv", index=False)

print("Generated synthetic station + temperature data.")
