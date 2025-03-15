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

### **Second Period (October 2024)**
- `data/second_period/muon_counts.csv` – Time series of muon flux measurements.  
- `data/second_period/dst.csv` – Dst index values.  
- `data/second_period/neutrons.csv` – Neutron monitor data.

## **Analysis**
The analysis of the dataset is performed using **Python** and **Jupyter Notebooks**, employing statistical methods such as the **Truncated Time-Shift (TTS) test** for time-series correlation analysis.

### **Main Files in This Repository**
- `analysis.ipynb` – Jupyter Notebook with step-by-step data processing and analysis.  
- `requirements.txt` – List of dependencies required to run the analysis.  
- `README.md` – Documentation of the repository.

## **Installation and Usage**
To reproduce the analysis:

1. **Clone this repository:**
   ```bash
   git clone https://github.com/your-username/forbush-decrease-sama.git
   cd forbush-decrease-sama
 Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

2. ** Open and run the Jupyter Notebook:**

```bash
jupyter notebook analysis.ipynb
```

## Citation

If you use this dataset or analysis in your research, please cite:

- Zenodo Dataset: DOI: 10.5281/zenodo.15032283
- AGU Journal Paper: Pending publication

## Authors and Contributors

-   Molina, Jorge;
    Richard, Euan;
    Giovanni, Secchia;
    Stalder, Diego;
    Bertoli, Mathias;
    Trepowski, Caleb;
    Baez, Oscar;
    Benitez Montiel, Carlos;
    Cho, Lucas;
    Cristaldo, Esteban;
    Barrios, Fernando Pio;
    Nuñez, Jesus;
    Cuevas, Alan


## License

This project is licensed under the MIT License.
