from pathlib import Path
import joblib 

BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR)
model = joblib.load(BASE_DIR/'models/Xgb_model.pkl')

def predict(df):
    return model.predict(df)
