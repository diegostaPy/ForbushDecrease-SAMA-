import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer
from scipy.optimize import curve_fit
import scipy.stats

# Crear carpeta para guardar figuras
os.makedirs("figures", exist_ok=True)

# Cargar datos
df = pd.read_csv("data/first_period/fiuna.csv")
df['timestamp'] = pd.to_datetime(df['timestamp'])
df.set_index('timestamp', inplace=True)

# Función para eliminar outliers
def remove_outliers(df_in, col_name):
    q1, q3 = np.percentile(df_in[col_name].dropna(), [25, 75])
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    df_in[col_name] = df_in[col_name].where(df_in[col_name].between(lower, upper))
    return df_in

# Plot inicial de muones
plt.figure(figsize=(15, 2))
plt.plot(df.index, df['muons'], color='k')
plt.title("Conteo original de muones")
plt.xlabel("Fecha")
plt.ylabel("Muones")
plt.savefig("figures/muones_original.png")
plt.close()

# Procesamiento horario
df2 = df.apply(pd.to_numeric, errors='coerce').resample('h').mean()
df3 = df2.loc["2024-05-07":"2024-05-17"]

# Datos de clima
df4 = pd.read_csv('data/first_period/profileweather_teff.csv')
df4['timestamp'] = pd.to_datetime(df4['timestamp'])
df4.set_index('timestamp', inplace=True)

# Unir datasets
df_merged = pd.merge(df3, df4, left_index=True, right_index=True, how='outer')
df_merged = df_merged.loc["2024-05-07":"2024-05-17"]

# Plots de variables
variables = ['muons', 'external_pressure', 'lab_temp', 'external_temp']
axes = df_merged[variables].plot(marker='.', markersize=2, figsize=(10, 7), subplots=True)
for ax, var in zip(axes, variables):
    ax.set_ylabel(var)
    ax.set_xlabel('Fecha')
plt.suptitle("Variables ambientales y conteo de muones")
plt.savefig("figures/variables_ambientales.png")
plt.close()

# Corrección por presión
P0 = df_merged['external_pressure'].mean()
Im = df_merged['muons'].mean()

df_merged['dP'] = df_merged['external_pressure'] - P0
df_merged['ln_IoIm'] = np.log(df_merged['muons'] / Im) * 100

# Imputación
imputer = SimpleImputer(strategy='mean')
df_merged[['ln_IoIm', 'dP']] = imputer.fit_transform(df_merged[['ln_IoIm', 'dP']])

# Modelo lineal presión
X = df_merged[['dP']]
y = df_merged['ln_IoIm']
model_p = LinearRegression().fit(X, y)
beta = model_p.coef_[0]

# Aplicar corrección por presión
df_merged['IoPC'] = df_merged['muons'] * np.exp(-0.01 * beta * df_merged['dP'])

# Plot muones corregidos por presión
plt.figure(figsize=(15, 5))
plt.plot(df_merged.index, df_merged['muons'], label='Original', color='red')
plt.plot(df_merged.index, df_merged['IoPC'], label='Corregido por presión', color='blue')
plt.title("Corrección por presión atmosférica")
plt.legend()
plt.savefig("figures/correccion_presion.png")
plt.close()

# Regresión visual presión
sns.set(style="darkgrid")
plt.figure(figsize=(10, 6))
sns.regplot(x='dP', y='ln_IoIm', data=df_merged, scatter_kws={"color": "blue"}, line_kws={"color": "red"})
plt.xlabel('Δ Presión (dP)')
plt.ylabel('ln(I/Im) [%]')
plt.title('Regresión lineal: ln(I/Im) vs ΔP')
plt.savefig("figures/regresion_presion.png")
plt.close()

# Corrección por temperatura
T0 = df_merged['TMP_MSS'].mean()
Im2 = df_merged['IoPC'].mean()
df_merged['dT'] = df_merged['TMP_MSS'] - T0
df_merged['ln_IoIm2'] = np.log(df_merged['IoPC'] / Im2) * 100

df_merged[['ln_IoIm2', 'dT']] = imputer.fit_transform(df_merged[['ln_IoIm2', 'dT']])

# Modelo lineal temperatura
X_temp = df_merged[['dT']]
y_temp = df_merged['ln_IoIm2']
model_t = LinearRegression().fit(X_temp, y_temp)
alpha = model_t.coef_[0]

# Aplicar corrección final
df_merged['IoTPC'] = df_merged['IoPC'] * np.exp(-0.01 * alpha * df_merged['dT'])

# Plot final
plt.figure(figsize=(15, 5))
plt.plot(df_merged.index, df_merged['muons'], label='Original', color='red')
plt.plot(df_merged.index, df_merged['IoTPC'], label='Corregido presión + temperatura', color='green')
plt.title("Corrección total de muones")
plt.legend()
plt.savefig("figures/correccion_total.png")
plt.close()

# Regresión visual temperatura
plt.figure(figsize=(10, 6))
sns.regplot(x='dT', y='ln_IoIm2', data=df_merged, scatter_kws={"color": "blue"}, line_kws={"color": "red"})
plt.xlabel('Δ Temperatura (dT)')
plt.ylabel('ln(I/Im) [%]')
plt.title('Regresión lineal: ln(I/Im) vs ΔT')
plt.savefig("figures/regresion_temperatura.png")
plt.close()

# Guardar CSV con correcciones
df_merged['alpha'] = alpha
df_merged['beta'] = beta
df_merged[['muons', 'IoPC', 'IoTPC', 'dP', 'dT', 'alpha', 'beta']].to_csv("data/first_period/muones_corregidos.csv")

print(f"Corrección completada. Alpha = {alpha:.4f}, Beta = {beta:.4f}")



