import csv
import time

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