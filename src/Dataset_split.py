from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split,GridSearchCV,TimeSeriesSplit
from sklearn.metrics import accuracy_score ,mean_squared_error,r2_score,mean_absolute_error

def split_scale(train_df,test_df,scale =True):
    sc=StandardScaler()     

    split=int(train_df.shape[0]*0.8)
    train=train_df.iloc[:split]
    test=train_df.iloc[split:]
    
    X_train=train.drop('streamflow_tomorrow_cumecs',axis=1)
    y_train=train['streamflow_tomorrow_cumecs']

    X_test=test.drop('streamflow_tomorrow_cumecs',axis=1)
    y_test=test['streamflow_tomorrow_cumecs']
        
    X_train_scaled=sc.fit_transform(X_train)
    X_test_scaled=sc.transform(X_test)
    test_scaled=sc.transform(test_df)
    return X_train_scaled,X_test_scaled,y_train,y_test ,test_scaled