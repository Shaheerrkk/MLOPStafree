# data_preprocessing.py
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder

from sklearn.model_selection import train_test_split

def preprocess_data(data):
    if isinstance(data, dict):
        data = pd.DataFrame(data, index=[0])
    else:
        data = pd.DataFrame(data)

    
    print(data)
    print("aheebb \n\n\n\n\n")
    # Handling missing values
    data['Item_Weight'].fillna(data['Item_Weight'].mean(), inplace=True)
    data['Outlet_Size'] = data['Outlet_Size'].map({"Small":1,"Medium":2,"High":3})
    data['Outlet_Size'].fillna(data['Outlet_Size'].mode()[0], inplace=True)

    # Encoding categorical variables
    columns_to_encode = ['Item_Fat_Content', 'Outlet_Location_Type', 'Outlet_Type', 'Item_Type']

    label_encoders = {}
    for col in columns_to_encode:
        le = LabelEncoder()
        data[col] = le.fit_transform(data[col])
        # Storing the label encoder for possible future use
        label_encoders[col] = le

    columns_to_drop = ['Outlet_Identifier', 'Item_Identifier', 'Outlet_Establishment_Year']
    columns_to_drop = [col for col in columns_to_drop if col in data.columns]
    if columns_to_drop:
        data.drop(columns=columns_to_drop, inplace=True)

    
    # Scaling numerical features
    # scaler = MinMaxScaler()
    # data[['Item_Weight', 'Item_MRP']] = scaler.fit_transform(data[['Item_Weight', 'Item_MRP']])

    

    return data


