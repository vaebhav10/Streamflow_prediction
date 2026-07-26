# Streamflow Prediction System

## Overview

The objective is to predict next-day streamflow using hydrological, meteorological, and watershed-related features.
The solution uses an **XGBoost Regressor** combined with feature engineering techniques such as cyclic temporal encoding, rainfall aggregation, and interaction feature consolidation on a csv file with shape **(2571055, 34)**. A Streamlit dashboard is provided for interactive predictions and visualization.

---

## Features

* Streamflow forecasting using XGBoost
* Automated preprocessing pipeline
* Temporal feature engineering (month and day-of-year encoding)
* Rainfall aggregation and interaction feature generation
* Streamlit-based web application
* CSV upload and batch prediction support
* Downloadable prediction results
* Interactive visualization dashboard

---

## Model Performance

### Validation Performance

## 📊 Model Performance Metrics

| Model | MAE | RMSE | NSE | Time |
|---    |---: |---:  |---:  |---:|
| Base Error | 43.756 | 140.810 | 0.99569 | — |
| XGBoost | 30.422 | 99.486 | 0.99785 | 3.040s |
| CatBoost | 34.564 | 95.506 | 0.99802 | 45.969s |
| Random Forest | 39.470 | 128.696 | 0.99640 | 309.495s |

## Installation

Clone the repository:

```bash
git clone https://github.com/vaebhav10/Streamflow_prediction.git
cd Streamflow_prediction
```

Create and activate a virtual environment:

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux / macOS
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```
---

## Running the Streamlit Dashboard

```bash
streamlit run streamlit.py
```

The dashboard supports:

* Uploading custom CSV files
* Running predictions on uploaded data
* Using built-in demo data
* Downloading prediction outputs
* Visualizing predicted streamflow trends

---

## Using Demo Data

A sample dataset is included for quick testing:

```text
demo/sample_input.csv
```


---

## Data

Due to dataset size constraints, the original competition datasets are not included in this repository.

To test the application:

* Use the provided demo dataset
* Upload a CSV following the same schema as the competition dataset

---

## Tech Stack

* Python
* Pandas
* NumPy
* Scikit-Learn
* XGBoost
* Streamlit
* Joblib

---  
-- GitHub Copilot
