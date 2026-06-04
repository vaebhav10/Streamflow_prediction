# Stream Flow Prediction — IIIT Lucknow Challenge 2026

This repository contains code and assets for the Stream Flow Prediction challenge (IIIT Lucknow). It includes data preprocessing, model training (XGBoost), and a Streamlit app for inference and visualization.

- Clone the repo and install dependencies:

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate
pip install -r requirements.txt
```

- Run the pipeline:

```bash
python main.py
```

- Run the Streamlit demo UI:

```bash
streamlit run streamlit.py
```

**Repository layout**

- [main.py](main.py): example script that runs preprocessing, split/scale, training and prediction.
- [streamlit.py](streamlit.py): Streamlit app for uploading a CSV and getting predictions.
- [requirements.txt](requirements.txt): Python dependencies.
- [src/preprocess.py](src/preprocess.py): dataset feature engineering and cleanup.
- [src/Dataset_split.py](src/Dataset_split.py): scaling and train/validation split utilities.
- [src/training.py](src/training.py): model training and evaluation code (XGBoost).
- [data/](data): `train_flood.csv` and `test_flood.csv` used by the example pipeline.
- [demo/sample_input.csv](demo/sample_input.csv): example CSV compatible with the Streamlit app.
- [models/](models): directory to save or load trained model artifacts (e.g. `flood_xgb_model.pkl`, `scaler.pkl`).
- [catboost_info/](catboost_info): additional CatBoost training logs/artifacts (if used).

**Data**

- The example pipeline reads `data/train_flood.csv` and `data/test_flood.csv`.
- Use `demo/sample_input.csv` to test the Streamlit app (click "Use Demo Data").

**How it works (short)**

- `src/preprocess.py` performs feature transforms (cyclic encodings for month/day, merged interaction features, scaled upstream rain features, antecedent rain aggregation).
- `src/Dataset_split.py` scales data using `StandardScaler` and returns scaled train/val/test sets.
- `src/training.py` fits an `XGBRegressor`, prints train/validation metrics (MAE, RMSE, R2), and returns the fitted model.

**Using the Streamlit app**

- Start the app with `streamlit run streamlit.py`.
- The app loads model artifacts from the `models/` directory. Place `flood_xgb_model.pkl`, `scaler.pkl`, and `features.pkl` there to enable predictions.
- Upload a CSV with the expected columns (or use the demo file). The app will preprocess, predict, and allow CSV download of predictions.

**Reproducibility / notes**

- The example `main.py` is a minimal pipeline intended to demonstrate end-to-end flow. For full experiments, adapt hyperparameters and add model checkpointing.
- `requirements.txt` pins many packages; consider creating a lightweight env with only the packages you need for training or inference.
