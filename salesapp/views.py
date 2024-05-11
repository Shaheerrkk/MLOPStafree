from django.shortcuts import render
from django.http import HttpResponse
from .scripts import data_ingestion, data_preprocessing, model_training, inference
from .scripts.graphs import plot_graphs
import os
import time

# Get the base directory of the Django app
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def home(request):
    return render(request, 'home.html')
def run_pipelinee(request):
    # Data Ingestion
    data_ingestion_view(request)
    time.sleep(2)

    # Data Preprocessing
    data_preprocessing_view(request)
    time.sleep(2)

    # Model Training
    model_training_view(request)
    time.sleep(2)

    # Model Evaluation
    model_evaluation_view(request)
    return render(request, 'index.html')

def data_ingestion_view(request):
    train_csv_path = os.path.join(BASE_DIR, 'salesapp\\scripts', 'Train.csv')
    test_csv_path = os.path.join(BASE_DIR, 'salesapp\\scripts', 'Test.csv')
    bigmart_train = data_ingestion.load_data(train_csv_path)
    bigmart_test = data_ingestion.load_data(test_csv_path)
    print("Data Ingestion completed successfully.")

def data_preprocessing_view(request):
    
    train_csv_path = os.path.join(BASE_DIR, 'salesapp\\scripts', 'Train.csv')
    bigmart_train = data_ingestion.load_data(train_csv_path)
    plot_graphs(bigmart_train)
    train_data = data_preprocessing.preprocess_data(bigmart_train)
    
    print("Data Preprocessing completed successfully.")

def model_training_view(request):
    train_csv_path = os.path.join(BASE_DIR, 'salesapp\\scripts', 'Train.csv')
    bigmart_train = data_ingestion.load_data(train_csv_path)
    train_data = data_preprocessing.preprocess_data(bigmart_train)
    model = model_training.train_model(train_data)
    print("Model Training completed successfully.")

def model_evaluation_view(request):
    test_csv_path = os.path.join(BASE_DIR, 'salesapp\\scripts', 'Test.csv')
    bigmart_test = data_ingestion.load_data(test_csv_path)
    test_data = data_preprocessing.preprocess_data(bigmart_test)
    train_csv_path = os.path.join(BASE_DIR, 'salesapp\\scripts', 'Train.csv')
    bigmart_train = data_ingestion.load_data(train_csv_path)
    train_data = data_preprocessing.preprocess_data(bigmart_train)
    model = model_training.train_model(train_data)
    inference.prediction(test_data, model)
    print("Model Evaluation completed successfully.")

def run_pipeline(request):
    print("RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR\n\n\n\n\n")
    if request.method == 'POST':
        # Extracting user input
        item_weight = float(request.POST.get('item_weight', 0))
        item_fat_content = request.POST.get('item_fat_content', '')
        item_visibility = float(request.POST.get('item_visibility', 0))
        item_type = request.POST.get('item_type', '')
        item_mrp = float(request.POST.get('item_mrp', 0))
        outlet_size = request.POST.get('outlet_size', '')
        outlet_location_type = request.POST.get('outlet_location_type', '')
        outlet_type = request.POST.get('outlet_type', '')

        # Create a dictionary to hold user input
        user_input_data = {
            'Item_Weight': item_weight,
            'Item_Fat_Content': item_fat_content,
            'Item_Visibility': item_visibility,
            'Item_Type': item_type,
            'Item_MRP': item_mrp,
            'Outlet_Size': outlet_size,
            'Outlet_Location_Type': outlet_location_type,
            'Outlet_Type': outlet_type
        }
        print("Shit\n\n\n\n\n\n\n\n\n")
        print(user_input_data)

        # Data Ingestion
        train_csv_path = os.path.join(BASE_DIR, 'Sales\\scripts', 'Train.csv')
        test_csv_path = os.path.join(BASE_DIR, 'Sales\\scripts', 'Test.csv')
        bigmart_train = data_ingestion.load_data(train_csv_path)
        bigmart_test = data_ingestion.load_data(test_csv_path)
        print("Data Ingestion completed successfully.")

        # Data Preprocessing
        train_data = data_preprocessing.preprocess_data(bigmart_train)
        user_data = data_preprocessing.preprocess_data(user_input_data)
        print(user_data)
        plot_graphs(train_data)
        print("Data Preprocessing completed successfully.")

        # Model Training
        # model = model_training.train_model(train_data)
        print("Model Training completed successfully.")

        # Model Evaluation and Prediction using user input
        prediction_result = inference.prediction(user_data)

        # Check if prediction_result is a list or a single value
        if isinstance(prediction_result, list):
            prediction_results = prediction_result
        else:
            prediction_results = [prediction_result]

        return render(request, 'index.html', {'prediction_results': prediction_results})

    return HttpResponse("Invalid request method. Please use POST method to submit the form.")
