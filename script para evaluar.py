
import pandas as pd
import numpy as np
import statsmodels.api as sm
import plotly.express as px
from scipy import stats

#data_folder = 'data/first_period/'
data_folder = 'data/second_period/'

df = pd.read_csv(data_folder + 'fiuna.csv', index_col='timestamp', parse_dates=['timestamp'])
dst = pd.read_csv(data_folder + 'dst.csv', index_col='timestamp', parse_dates=['timestamp'])
neutrons = pd.read_csv('data/first_period/neutrons.csv', index_col='timestamp', parse_dates=['timestamp'])
# Use statsmodels library for the fit.
muon_col = 'muons'
fit_cols = ['lab_temp','external_temp','external_pressure']

mod = sm.OLS(df[muon_col], sm.add_constant(df[fit_cols].values))
fit = mod.fit()
errors = fit.summary2().tables[1]['Std.Err.'][1:].values
const = fit.params.values[0]
params = fit.params.values[1:]
means = df.mean()[fit_cols].values

# Calculate the necessary correction based on this fit.
df['correction'] = df.apply(lambda r: np.sum((means - r[fit_cols].values) * params), axis=1)

# Use 2 * errors for 95% confidence interval
df['correction_err'] = df.apply(lambda r: np.sqrt(np.sum(
    ((means - r[fit_cols].values) * errors * 2) ** 2
)), axis=1)

# Apply the correction.
df['muons_corrected'] = df[muon_col] + df['correction']

# Show the results
params, errors, means

muons_per_hour = df[['muons_corrected']].resample('h').mean() * 60
px.line(muons_per_hour)
# Align on continuous time index using Pandas join; impute gaps
aligned_data = muons_per_hour.join(dst).interpolate(method='linear')
x = aligned_data['dst'].copy()
y = aligned_data['muons_corrected'].copy()

# For the TTS test to apply, at least one input series must pass an Augmented Dickey-Fuller test for stationarity.
# Here the p-values are printed, at least one of which should be low.
from statsmodels.tsa.stattools import adfuller
adfuller(x.values)[1], adfuller(y.values)[1]


# Align on continuous time index using Pandas join; impute gaps
aligned_data = muons_per_hour.join(dst).interpolate(method='linear')
x = aligned_data['dst'].copy()
y = aligned_data['muons_corrected'].copy()

# For the TTS test to apply, at least one input series must pass an Augmented Dickey-Fuller test for stationarity.
# Here the p-values are printed, at least one of which should be low.
from statsmodels.tsa.stattools import adfuller
adfuller(x.values)[1], adfuller(y.values)[1]

r=48
# Sort the taus by descending value
t = pd.Series(taus).sort_values(ascending=False)

# Get the rank (position) of tau_r
B = t.index.get_loc(r) + 1

# Get the u-statistic
u = B / (r+1)

print(f"B: {B}, u: {u:.4f}")