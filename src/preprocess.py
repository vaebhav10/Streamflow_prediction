import pandas as pd
import numpy as np

def preprocess_data(df):
    df.drop('row_id',axis=1,inplace=True)
    df.drop('month',axis=1,inplace=True)
    df.drop('day_of_year',axis=1,inplace=True) 
    
    # Columns to drop 
    drop_cols=[
    'rain_soilmoisture_interaction', 
    'rain_urban_interaction', 
    'rain_slope_interaction', 
    'rain_basinsize_interaction',
    'uparea_rain_interaction',
    'antecedent_saturation_interaction',
    'upstream_rain_mean_scaled',
    'upstream_rain_weighted_scaled'
    ]
    df.drop(columns=drop_cols,inplace=True) 
    antecedent_cols=[
    'antecedent_rain_3d_sum',
    'antecedent_rain_7d_sum',
    'antecedent_rain_15d_sum',
    'antecedent_rain_30d_sum',
    'antecedent_rain_60d',
    'antecedent_rain_ewm' 
    ]
    df.drop(columns=antecedent_cols,inplace=True)
    df.drop(columns=['merged_rain_interaction','upstream_rain_weighted','flow_rate_of_change' ],inplace=True)

    return df