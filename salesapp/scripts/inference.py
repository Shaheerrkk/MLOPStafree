from sklearn.metrics import mean_squared_error
import joblib
import os

def prediction(data, model=None, y_test=None):
    
    # Get the current directory`
    current_dir = os.path.dirname(__file__)

    # Specify the full path to the .pkl file
    pkl_file_path = os.path.join(current_dir, 'linear_regression_model.pkl')

    # Load the model
    loaded_model = joblib.load(pkl_file_path)


    if 'Item_Outlet_Sales' in data.columns:
        X_test = data.drop(columns=["Item_Outlet_Sales"])   
        y = data["Item_Outlet_Sales"]
    else:
        X_test = data   
    y_pred = loaded_model.predict(X_test)
    if len(y_pred) > 1:
        print("Multiple values in prediction:", y_pred)
    if y_test is not None:
        mse = mean_squared_error(y_test, y_pred)
        return y_pred, mse  # Return the predictions and mean squared error if available
    return y_pred
 