from sklearn.ensemble import RandomForestRegressor 
from xgboost import XGBRegressor 
from sklearn.metrics import mean_squared_error, r2_score,mean_absolute_error
from catboost import CatBoostRegressor

model =XGBRegressor(
    # learning_rate= 0.1,
    # max_depth= 6,
    # n_estimators= 100,
    # subsample= 0.8
)
def model_training(X_train,X_val,y_train,y_val):
    model.fit(X_train, y_train)
    val_pred = model.predict(X_val)
    train_xgb=model.predict(X_train)
    print("Train MAE : ",mean_absolute_error(y_train, train_xgb) )
    evaluate(y_val,val_pred)
    return model
def evaluate(y_true,y_pred):
    rmse = mean_squared_error(y_true, y_pred) ** 0.5
    mae = mean_absolute_error(y_true, y_pred) 
    r2 = r2_score(y_true, y_pred)
    print("Test evaluated metrices: ")
    print(f"RMSE: {rmse:.4f}")
    print(f"MAE: {mae:.4f}")
    print(f"R2: {r2:.4f}")
    