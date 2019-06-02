import time
import csv
import statistics

from file_handling.csv_to_txt import *
from ppg.ppg_features import *
from mathematics.graph import *

def read_live_ppg(no_of_samples, capture_duration):
    temp = []

    # open device file
    fd = open("/sys/bus/iio/devices/iio:device0/in_voltage0_raw", "r")

    for i in range(no_of_samples + 1):
        temp.append(int(fd.read()))
        fd.seek(0, 0)
        time.sleep(capture_duration/no_of_samples)

    return smooth(smooth(temp, 20, "hanning"), 12, "hanning")

def print_live_ppg():
    
    # open device file
    fd = open("/sys/bus/iio/devices/iio:device0/in_voltage0_raw", "r")
    
    while True:
        print(fd.read())
        fd.seek(0, 0)
        time.sleep(15/60)

def capture_raw_ppg():

    ppg_raw_csv_file = "../data/csv/ppg_raw.csv"

    capture_duration = 5
    no_of_samples = 500

    print("Place your finger on the PPG sensor")
    time.sleep(1)

    print("Capturing...")
    ppg_data = read_live_ppg(no_of_samples, capture_duration)

    with open(ppg_raw_csv_file, mode = "a") as ppg_raw_csv:
        ppg_raw_csv_writer = csv.writer(ppg_raw_csv)
        ppg_raw_csv_writer.writerow(ppg_data)

    print("Done")

def capture_ppg():

    # list of files to be handled
    ppg_csv_file = "../data/csv/ppg_train.csv"
    ppg_txt_file = "../data/txt/ppg_train.txt"

    no_of_samples = 500
    capture_duration = 5.0

    n = input("\nMention your state\n1. Active\n2. Drowsy\n3. Inactive\n")
    if int(n) == 1 | int(n) == 2:
        print("\nPlace your finger on the PPG sensor")
        time.sleep(0.5)
        
    print("\nCapturing...")
    ppg_data = read_live_ppg(no_of_samples, capture_duration)
    #print(ppg_data)
         
    print("\nExtracting features...")
    features = get_ppg_features(ppg_data, no_of_samples, capture_duration)
    time.sleep(0.5)

    if int(n) == 1:
        features.append(int(1)) # class - active
    elif int(n) == 2:
        features.append(int(2)) # class - drowsy
    elif int(n) == 3:
        features.append(int(3)) #class - inactive
    
    print("\nWriting to {}...".format(ppg_csv_file))
    time.sleep(0.5)

    with open(ppg_csv_file, mode = "a") as ppg_train_csv:
        ppg_train_csv_writer = csv.writer(ppg_train_csv)
        ppg_train_csv_writer.writerow(features)

    #update_train_data_from_csv(ppg_csv_file, ppg_txt_file)

    print("\nDone.")

def main():
    capture_ppg()
    

if __name__ == '__main__':
    main()