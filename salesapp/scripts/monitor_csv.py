import os
import time
import subprocess

csv_file = 'Train.csv'
last_modified = os.path.getmtime(csv_file)

while True:
    current_modified = os.path.getmtime(csv_file)
    if current_modified != last_modified:
        print("CSV file has changed. Retraining model...")
        # Call the main.py script to run the training process
        subprocess.call(["py", "main.py"])
        last_modified = current_modified
    print("Checking for changes...")
    time.sleep(5)  # Check every minute
