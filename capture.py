import time
import csv
import statistics

def update_train_data_from_csv(csv_file, txt_file):

    ppg_csv_file = csv_file
    ppg_txt_file = txt_file

    no_of_samples = 0
    no_of_features = 0
    no_of_classes = 1

    print("Updating txt from csv...")
    time.sleep(0.5)

    print("Extracting metadata...")
    time.sleep(0.5)

    with open(ppg_csv_file, "r") as csv_file_fd:
        csv_reader = csv.reader(csv_file_fd)

        # exclude the labels row
        no_of_samples = sum(1 for row in csv_reader) - 1

    with open(ppg_csv_file, "r") as csv_file_fd:
        csv_reader = csv.reader(csv_file_fd)
        
        for row in csv_reader:
            for col in row:
                no_of_features += 1
            break

    no_of_features -= no_of_classes

    #print("No of samples = {}".format(no_of_samples))
    #print("No of features = {}".format(no_of_features))
    #print("No of classes = {}".format(no_of_classes))

    header = [no_of_samples, no_of_features, no_of_classes]

    print("Extracting data...")
    time.sleep(0.5)

    print("Writing to txt file...")
    time.sleep(0.5)

    with open(ppg_txt_file, "w") as txt_file_fd:
        for i in header:
            txt_file_fd.write(str(i) + " ")
        txt_file_fd.write("\n")

        with open(ppg_csv_file, "r") as csv_file_fd:
            csv_reader = csv.reader(csv_file_fd)
            for row in csv_reader:
                if not row[0].isalpha():
                    for i in row[0 : len(row) - 1]:
                        txt_file_fd.write(str(i) + " ")
                    txt_file_fd.write("\n")
                    txt_file_fd.write(str(row[-1]))
                    txt_file_fd.write("\n")


def capture_ppg():

    # list of files to be handled
    ppg_csv_file = "csv/ppg_train.csv"
    ppg_txt_file = "nn/ppg_train.txt"

    # open device file
    fd = open("/sys/bus/iio/devices/iio:device0/in_voltage0_raw", "r")

    no_of_samples = 500
    capture_duration = 5.0

    n = input("Mention your state\n1. Drowsy\n2. Active\n")

    print("Place your finger on the PPG sensor")
    time.sleep(0.5)

    ppg_data = []

    print("Capturing...")

    for i in range(no_of_samples + 1):
        ppg_data.append(int(fd.read()))
        fd.seek(0, 0)
        time.sleep(capture_duration/no_of_samples)

    #print(ppg_data)

    print("Extracting features...")
    mean = statistics.mean(ppg_data)
    var = statistics.variance(ppg_data, mean)

    time.sleep(0.5)

    #print("mean = ", format(mean))
    #print("var = ",format(var))

    features = [mean, var]

    if int(n) == 1:
        features.append(int(1))
    else:
        features.append(int(0))
    
    print("Writing to {}...".format(ppg_csv_file))
    time.sleep(0.5)

    with open(ppg_csv_file, mode = "a") as ppg_train_csv:
        ppg_train_csv_writer = csv.writer(ppg_train_csv)
        ppg_train_csv_writer.writerow(features)

    update_train_data_from_csv(ppg_csv_file, ppg_txt_file)

    print("Done.")

def capture_mpu6050():

    # list of files to be handled
    mpu6050_csv_file = "csv/mpu6050_train.csv"
    mpu6050_txt_file = "nn/mpu6050_txt.csv"

    # open device file
    #fd = open("/dev/i2c-1", "rw")

    no_of_samples = 500
    capture_duration = 5.0

    n = input("Mention your motion state\n1. Abnormal\n2. OK\n")

    mpu6050_acc_x = []
    mpu6050_acc_y = []
    mpu6050_acc_z = []
    mpu6050_gyro_x = []
    mpu6050_gyro_y = []
    mpu6050_gyro_z = []

    print("Capturing...")

    mpu6050_data = [statistics.mean(mpu6050_acc_x),
                    statistics.mean(mpu6050_acc_y),
                    statistics.mean(mpu6050_acc_z),
                    statistics.mean(mpu6050_gyro_x),
                    statistics.mean(mpu6050_gyro_y),
                    statistics.mean(mpu6050_gyro_z)]

    #print(mpu6050_data)

    if int(n) == 1:
        mpu6050_data.append(int(1))
    else:
        mpu6050_data.append(int(0))
    
    print("Writing to {}...".format(mpu6050_csv_file))
    time.sleep(0.5)

    with open(mpu6050_csv_file, mode = "a") as mpu6050_train_csv:
        mpu6050_train_csv_writer = csv.writer(mpu6050_train_csv)
        mpu6050_train_csv_writer.writerow(mpu6050_data)

    #update_train_data_from_csv(mpu6050_csv_file, mpu6050_txt_file)

    print("Done.")



def main():
    capture_ppg()
    

if __name__ == '__main__':
    main()