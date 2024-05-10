# model_training.py
from sklearn.linear_model import LinearRegression
import joblib

def train_model(data):
    
    X = data.drop(columns=["Item_Outlet_Sales"])
    y = data["Item_Outlet_Sales"]
    print("SHItssss")
    model = LinearRegression()
    model.fit(X, y)
    joblib.dump(model, 'linear_regression_model.pkl')
    return model



# loaded_model = joblib.load('linear_regression_model.pkl')