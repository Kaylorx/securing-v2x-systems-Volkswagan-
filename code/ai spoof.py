import serial
import numpy as np
import joblib  # For saving/loading models
from sklearn.ensemble import IsolationForest

# Initialize serial connection to Arduino
ser = serial.Serial('/dev/ttyUSB0', 9600)  # Adjust COM port for your setup

# Load or train the anomaly detection model
try:
    model = joblib.load('v2x_anomaly_model.pkl')  # Load pre-trained model
except FileNotFoundError:
    print("Training new anomaly detection model...")
    # Generate synthetic normal data for training
    normal_data = np.random.normal(size=(100, 3))
    model = IsolationForest(contamination=0.1)
    model.fit(normal_data)
    joblib.dump(model, 'v2x_anomaly_model.pkl')  # Save the trained model

# Process data from Arduino
def process_data(data_line):
    try:
        speed, latitude, longitude = map(float, data_line.split(','))
        data = np.array([[speed, latitude, longitude]])
        prediction = model.predict(data)
        if prediction[0] == -1:
            print("Spoofing Attack Detected! Data:", data_line)
        else:
            print("Normal Data:", data_line)
    except ValueError:
        print("Error parsing data:", data_line)

while True:
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').strip()
        process_data(line)
