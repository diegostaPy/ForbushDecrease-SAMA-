import pandas as pd
import numpy as np
lista=['first_period/profileweather.csv','second_period/profileweather.csv']
for file in lista:
    # Leer archivo CSV generado previamente
    df = pd.read_csv("data/"+file, parse_dates=['date'])

    # Inicializar lista para TMP_MSS
    tmp_mss_list = []

    # Constantes
    R = 8.31447  # J/mol·K
    M = 28.9644  # g/mol

    # Loop por cada fila (perfil)
    for _, row in df.iterrows():
        # Extraer vectores de perfil
        temperatures = row[[f"T_{i}" for i in range(23)]].values  # en K
        pressures = row[[f"P_{i}" for i in range(23)]].values      # en hPa
        altitudes = row[[f"H_{i}" for i in range(23)]].values      # en m

        # Convertir unidades
        altitudes_km = altitudes / 1000  # m -> km
        pressure_pa = pressures * 100    # hPa -> Pa

        # Calcular densidad [g/cm³]
        density = (M * pressure_pa) / (R * temperatures) * 1e-6  # g/cm³

        #M = 28.9644 g/mol → molar mass of dry air

        #pressure is in Pascals (Pa) → your input is in hPa, so it's multiplied by 100

        #R = 8.31447 J/(mol·K) → universal gas constant

        #temperature is in Kelvin (K)

        #1e-6 converts the result from g/m³ to g/cm³ (since atmospheric depth is calculated in g/cm²)
        
        # Calcular profundidad atmosférica [g/cm²]
        prof = np.zeros_like(density)
        for h in range(23):
            if h < 22:
                prof[h] = np.trapz(density[h:], altitudes_km[h:])
            else:
                prof[h] = density[22] * (altitudes_km[22] - altitudes_km[21])

        # Función peso
        w = np.zeros_like(prof)
        w[:-1] = (prof[:-1] - prof[1:]) / prof[0]
        w[-1] = prof[-1] / prof[0]

        # Temperatura ponderada por masa
        tmp_mss = np.sum(w * temperatures)
        tmp_mss_list.append(tmp_mss)

    # Añadir columna al DataFrame
    df["TMP_MSS"] = tmp_mss_list

    # Guardar resultados
    df[["date", "Ps", "Ts", "TMP_MSS"]].to_csv("data/"+file[:-4]+"_teff.csv", index=False)
