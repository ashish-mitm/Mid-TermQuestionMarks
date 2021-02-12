import csv
import os
from csv import reader


def readCSV(file):
    with open(file, 'r') as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)
        # Pass reader object to list() to get a list of lists
        list_of_rows = list(csv_reader)
        return list_of_rows


def writeCSV(file, data, mode='a+'):
    with open(file, mode, newline='') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL,delimiter=',')
        #for d in data:
        wr.writerow(data)


def readDir(name):
    with os.scandir(name) as entries:
        allfiles = []
        for entry in entries:
            allfiles.append(entry.name)
            # print(entry.name)
        return allfiles
