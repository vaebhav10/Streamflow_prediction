from pathlib import Path
import pandas as pd

from src.preprocess import preprocess_data
from src.prediction import predict
from src.feature_engineering import create_features

import time
start = time.perf_counter()

BASE_DIR = Path(__file__).resolve().parent

df=pd.read_csv(BASE_DIR/'data/test_flood.csv')

df =create_features(df)
cleaned_df = preprocess_data(df)

pred= predict(cleaned_df)

end =time.perf_counter()
print ( "Tota time taken :" , end-start)