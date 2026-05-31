import streamlit as st
import pandas as pd 
import joblib
from src.preprocess import preprocess_data

# Path configuration
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
MODEL_DIR = BASE_DIR / "models"

# UI header
st.set_page_config(page_title='Stream flow prediction',layout='centered')
st.title("Stream flow prediction dashboard")

@st.cache_resource
def load_assets():
    model=joblib.load(MODEL_DIR/'flood_xgb_model.pkl')
    scaler=joblib.load(MODEL_DIR/'scaler.pkl')
    feature_names=joblib.load(MODEL_DIR/'features.pkl')
    return model, scaler,feature_names

try:
    model,scaler,feature_names=load_assets()
except Exception as e:
    st.error(f"Error loading model assets : {e}")
    st.stop()


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
    
    
st.dataframe(df.head())
row_ids=df['row_id']


try:
    processed_df=preprocess_data(df)
except :
    st.warning(f"Dataset mismatch")
    st.stop()
    
if "streamflow_tomorrow_cumecs" in processed_df.columns:
    processed_df.drop('streamflow_tomorrow_cumecs',axis=1,inplace=True)
processed_df = processed_df[feature_names]
processed_df=scaler.transform(processed_df)

predictions=model.predict(processed_df)

result=pd.DataFrame({
    'row_id':row_ids,
    'predicted_streamflow':predictions
})
st.subheader("Predictions")
st.dataframe(result)
csv=result.to_csv(index=False)

st.download_button(
    'Download Predictions',
    csv,
    'prediction.csv',
    'text/csv'
)
st.line_chart(predictions)
