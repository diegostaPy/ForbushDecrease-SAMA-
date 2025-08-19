# **Forbush Decrease Events in the South Atlantic Magnetic Anomaly**

## **Overview**
This repository contains code and data for the analysis of **Forbush Decrease (FD) events** observed at the **South Atlantic Magnetic Anomaly (SAMA)** using a low-cost muon detector deployed in Paraguay. The study investigates the correlation between cosmic-ray muon flux variations and geomagnetic disturbances, particularly during the **May and October 2024** FD events.

The dataset is published on **Zenodo**, and the analysis is submitted to the **AGU Journal**.

## **Dataset**
The full dataset is available on **Zenodo**:  
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.15032283.svg)](https://doi.org/10.5281/zenodo.15032283)

The dataset is divided into two observation periods:

### **First Period (May 2024)**
- `data/first_period/muon_counts.csv` – Time series of muon flux measurements.  
- `data/first_period/dst.csv` – Disturbance Storm Time (Dst) index values.  
- `data/first_period/neutrons.csv` – Neutron monitor data.
- `data/first_period/fiuna.csv` – Raw muon detector data.
- `data/first_period/muones_corregidos.csv` – Muon counts corrected for pressure and temperature.
- `data/first_period/muons_may_junecorrected.csv` – Muon counts for May–June, corrected.
- `data/first_period/profileweather_teff.csv` – Weather profile data (temperature, pressure).
- `data/first_period/profileweather.csv` – Additional weather data.
- `data/first_period/vasouras.csv` – Reference data from Vasouras station.

### **Second Period (October 2024)**
- `data/second_period/muon_counts.csv` – Time series of muon flux measurements.  
- `data/second_period/dst.csv` – Dst index values.  
- `data/second_period/neutrons.csv` – Neutron monitor data.
- `data/second_period/fiuna.csv` – Raw muon detector data.
- `data/second_period/muons_sep_octcorrected.csv` – Muon counts for Sep–Oct, corrected.
- `data/second_period/neutron_second_period.csv` – Neutron monitor data for second period.
- `data/second_period/profileweather_teff.csv` – Weather profile data.
- `data/second_period/profileweather.csv` – Additional weather data.
- `data/second_period/vasouras.csv` – Reference data from Vasouras station.

## **Analysis**
The analysis of the dataset is performed using **Python** and **Jupyter Notebooks**, employing statistical methods such as the **Truncated Time-Shift (TTS) test** for time-series correlation analysis.

### **Main Files in This Repository**
- `analysisfirstperiod.ipynb` – Jupyter Notebook for May–June 2024 FD event analysis, including temperature and pressure corrections and statistical testing.
- `analysissecondperiod.ipynb` – Jupyter Notebook for September–October 2024 FD event analysis, with similar methodology as the first period.
- `analysisWithTeff.ipynb` – Notebook demonstrating a simplified analysis workflow, matching the published paper, with step-by-step explanations.
- `temperaturaPresureCorrection.py` – Python script for correcting muon counts using atmospheric pressure and temperature data, generating figures and a corrected CSV.
- `donwloadGdas.py` – Script to download GDAS meteorological data from NOAA FTP servers for further analysis.

#### **New Analysis and Plotting Notebooks**
- `plot_and_analysis.ipynb` – Notebook for visualizing and analyzing muon, pressure, temperature, neutron, and DST data for both periods. Includes hourly resampling, outlier removal, and comparative plots.
- `plot_analysis_magnetic_and_muons.ipynb` – Notebook for joint analysis and plotting of magnetic field data (from Vasouras station) and muon data, including percent change calculations and event marking.

#### **Other Files**
- `requirements.txt` – List of dependencies required to run the analysis.  
- `README.md` – Documentation of the repository.

## **Installation and Usage**
To reproduce the analysis:

1. **Clone this repository:**
   ```bash
   git clone https://github.com/your-username/forbush-decrease-sama.git
   cd forbush-decrease-sama
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Open and run the Jupyter Notebooks:**
   ```bash
   jupyter notebook analysisfirstperiod.ipynb
   # or
   jupyter notebook analysissecondperiod.ipynb
   # or
   jupyter notebook analysisWithTeff.ipynb
   # or
   jupyter notebook plot_and_analysis.ipynb
   # or
   jupyter notebook plot_analysis_magnetic_and_muons.ipynb
   ```

## **Citation**

If you use this dataset or analysis in your research, please cite:

- Zenodo Dataset: DOI: 10.5281/zenodo.15032283
- AGU Journal Paper: Pending publication

## **Authors and Contributors**

- Molina, Jorge;
- Richard, Euan;
- Giovanni, Secchia;
- Stalder, Diego;
- Bertoli, Mathias;
- Trepowski, Caleb;
- Baez, Oscar;
- Benitez Montiel, Carlos;
- Cho, Lucas;
- Cristaldo, Esteban;
- Barrios, Fernando Pio;
- Nuñez, Jesus;
- Cuevas, Alan

## **License**

This project is licensed under the MIT License.
