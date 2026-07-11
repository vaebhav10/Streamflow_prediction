import numpy as np 
import pandas as pd

def create_features(df):
    df['month_cos']=np.cos(2*np.pi*df['month']/12 )
    df['month_sin']=np.sin(2*np.pi*df['month']/12 )
    df['dayofyear_cos']=np.cos(2*np.pi*df['day_of_year']/365 )
    df['dayofyear_sin']=np.sin(2*np.pi*df['day_of_year']/365)
    
    # single merged interaction
    df['merged_rain_interaction'] = df[[
        'rain_soilmoisture_interaction', 
        'rain_urban_interaction', 
        'rain_slope_interaction', 
        'rain_basinsize_interaction',
        'uparea_rain_interaction',
        'antecedent_saturation_interaction'
    ]].mean(axis=1)
    
    # single merged scaled
    df['upstream_rain_weighted' ]=(df['upstream_rain_mean_scaled']*0.6)+(df['upstream_rain_weighted_scaled']*0.4)
    
    # giving higher weight to recent rain
    df['antecedent_total'] = (df['antecedent_rain_3d_sum'] * 0.4) + (df['antecedent_rain_7d_sum'] * 0.3) + (df['antecedent_rain_15d_sum'] * 0.1)+(df['antecedent_rain_30d_sum']*0.05)+(df['antecedent_rain_60d']*0.05)+(df['antecedent_rain_ewm']*0.1)
    
    df['merged_upstream']=(df['merged_rain_interaction']*0.6)+(df['upstream_rain_weighted']*0.4)
    
    return df 