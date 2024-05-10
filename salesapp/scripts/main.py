# main.py


# Step 1: Data Ingestion
from data_ingestion import load_data

from graphs import plot_graphs

# Step 2: Data Preprocessing
from data_preprocessing import preprocess_data

# Step 3: Model Training
from model_training import train_model

#Step 4: Model Evaluation
from inference import prediction


def main():
    # Step 1: Data Ingestion
    bigmart_train = load_data("Train.csv")
    bigmart_test= load_data("Test.csv")
    



    # Step 2: Data Preprocessing
    train_data = preprocess_data(bigmart_train)
    test_data = preprocess_data(bigmart_test)
    
    plot_graphs(train_data)



    # Step 5: Model Training
    model = train_model(train_data)

    # X_test = test_data.drop(columns=["Item_Outlet_Sales"])   
    prediction(test_data, model)
    

if __name__ == "__main__":
    main()
