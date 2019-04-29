import csv
import time
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report, confusion_matrix
from capture import read_live_ppg
from ppg.ppg_features import *

def live_test(mlp_obj: MLPClassifier):
    
    #sampling_rate = 15
    capture_duration = 5.0
    no_of_samples = 100 * capture_duration
    
    while True:
        temp_data = read_live_ppg(no_of_samples, capture_duration)
        temp_features = [get_ppg_features(temp_data, no_of_samples, capture_duration)]

        #print(temp_features)

        output = mlp_obj.predict(temp_features)
        
        if output == ['1']:
            print("Active")
        elif output == ['2']:
            print("Drowsy")
        elif output == ['3']:
            print("Inactive")

def train_ppg():

    DATA = []

    # convert the data contained in the csv file, into matrix
    with open("../data/csv/ppg_train.csv", "r") as ppg_train_csv:
        ppg_train_csv_reader = csv.reader(ppg_train_csv)
        line_count = 0
        for row in ppg_train_csv_reader:
            if line_count == 0:
                print("Extracting headers...")
                time.sleep(0.5)
                print(row)
            else:
                DATA.append(row)
            line_count += 1
    
    
    time.sleep(0.5)
    #print("DATA = ", DATA)

    no_of_features = 6
    no_of_classes = 1

    n = no_of_features + no_of_classes

    X = []
    y = []

    for row in DATA:
        X.append(row[0 : (n - 1)])
        y.append(row[n - 1])

    #print("X = ", X)
    #print("Y = ", y)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    scaler = StandardScaler()
    scaler.fit(X_train)

    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)

    print("Training the neural network...")

    mlp = MLPClassifier(hidden_layer_sizes=(10, 10, 10), max_iter=1000)
    mlp.fit(X_train, y_train)

    predictions = mlp.predict(X_test)
    print(predictions)
    
    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test,predictions))

    print("\nClassification Report:")
    print(classification_report(y_test,predictions, target_names=["Active", "Drowsy", "Inactive"]))

    print("Starting live test...")
    time.sleep(0.5)
    live_test(mlp)  


def train_mpu6050():
    print("TODO")

def main():
    train_ppg()

if __name__=="__main__":
    main()