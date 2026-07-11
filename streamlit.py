import streamlit as st
import pandas as pd 
import joblib
from src.preprocess import preprocess_data
from src.feature_engineering import create_features
from src.prediction import predict

# Path configuration
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent

# UI header layouts 
st.set_page_config(page_title='Stream flow prediction',layout='centered')
st.title("Stream flow prediction dashboard")

@st.cache_resource
def load_assets():
    model=joblib.load(BASE_DIR/'models/Xgb_model.pkl')
    return model

try:
    model=load_assets()
except Exception as e:
    st.error(f"Error loading model assets : {e}")
    st.stop()

# File uploading/selection
upload_file=st.file_uploader(
    'Upload CSV file: ',
    type =['csv','xlsx']
)

if st.button("Use Demo Data"):
    df= pd.read_csv("demo/sample_input.csv")
    st.subheader("Demo file used ")  
    
elif upload_file:
    if upload_file.name.endswith('.csv'):
        df =pd.read_csv(upload_file)
    else:
        df=pd.read_excel(upload_file)
    st.subheader("File uploaded successfully ")  
else:
    st.warning("Upload a csv file or Use demo data")
    st.stop()
    
    
st.dataframe(df)
row_ids=df['row_id']

if "streamflow_tomorrow_cumecs" in df.columns:
    df.drop('streamflow_tomorrow_cumecs',axis=1,inplace=True)

df= create_features(df)
cleaned_df = preprocess_data(df)

# model prediction 
predictions=model.predict(cleaned_df)

result=pd.DataFrame({ # Results 
    'row_id':row_ids, 
    'predicted_streamflow':predictions
})

st.subheader("Predictions")
st.dataframe(result)
csv=result.to_csv(index=False)

st.download_button( # Download options for result
    'Download Predictions',
    csv,
    'prediction.csv',
    'text/csv'
)
st.line_chart(predictions)
