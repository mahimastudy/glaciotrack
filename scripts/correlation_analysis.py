import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import STL
from scipy.stats import pearsonr

# -------------------------
# Load data
# -------------------------
df = pd.read_csv("data/generated_station.csv", parse_dates=["date"])
df.set_index("date", inplace=True)

# -------------------------
# Remove trend using STL
# -------------------------
stl_disp = STL(df["vertical_mm"], period=12).fit()
stl_temp = STL(df["temp_c"], period=12).fit()

seasonal_disp = stl_disp.seasonal
seasonal_temp = stl_temp.seasonal

# -------------------------
# Normalize signals (z-score)
# -------------------------
disp_norm = (seasonal_disp - seasonal_disp.mean()) / seasonal_disp.std()
temp_norm = (seasonal_temp - seasonal_temp.mean()) / seasonal_temp.std()

# -------------------------
# Pearson correlation
# -------------------------
corr, p_value = pearsonr(disp_norm, temp_norm)

print("\n=== Seasonal Correlation Results ===")
print("Correlation coefficient:", round(corr, 3))
print("P-value:", p_value)

# -------------------------
# Confidence interval (Fisher z-transform)
# -------------------------
# Fisher z-transform
n = len(disp_norm)
z = np.arctanh(corr)
se = 1 / np.sqrt(n - 3)

z_ci_low = z - 1.96 * se
z_ci_high = z + 1.96 * se

ci_low = np.tanh(z_ci_low)
ci_high = np.tanh(z_ci_high)

