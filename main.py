from pathlib import Path
import pandas as pd

from src.preprocess import preprocess_data
from src.Dataset_split import split_scale
from src.training import model_training,evaluate
import time

start=time.perf_counter()
path = Path(__file__).resolve().parent
train=pd.read_csv(path/'data/train_flood.csv')
test=pd.read_csv(path/'data/test_flood.csv')

# Dataset cleaning 
cleaned_train=preprocess_data(train)
cleaned_test=preprocess_data(test)

# Splitting dataset and scalling 
X_train,X_val,y_train,y_val,test_scaled=split_scale(cleaned_train,cleaned_test)

# training and evaluation on train dataset 
model=model_training(X_train,X_val,y_train,y_val)

# prediction on test dataset
test_pred = model.predict(test_scaled)

end =time.perf_counter()
print ( "Tota time taken :" , end-start)