import numpy as np
from scipy.stats import pearsonr
from statsmodels.tsa.seasonal import STL

def seasonal_correlation(series1, series2, period=12):
    stl1 = STL(series1, period=period).fit()
    stl2 = STL(series2, period=period).fit()

    s1 = stl1.seasonal
    s2 = stl2.seasonal

    s1 = (s1 - s1.mean()) / s1.std()
    s2 = (s2 - s2.mean()) / s2.std()

    corr, p = pearsonr(s1, s2)

    return corr, p
