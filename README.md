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

| Metric   | Score  |
| -------- | ------ |
| MAE      | ~20    |
| Base MAE | ~43.755|
| RMSE     | ~85    |
| R² Score | ~0.998 |

### Kaggle Public Leaderboard

```text
KGE Score: 0.99181

```

---

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

## Running the Training Pipeline

```bash
python main.py
```

This will:

1. Load the dataset
2. Apply preprocessing and feature engineering
3. Scale features
4. Train the XGBoost model
5. Evaluate model performance
6. Generate predictions

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
