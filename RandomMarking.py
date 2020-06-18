import csv
import os
import random
import time

from CSVreadwrite import readDir, readCSV, writeCSV

# path = "Result-14/TH/7thsem"
# infopath = "Result-14/ThInfoMarks- 14/Info7thsem- 14"
# path = "CO-PO-MIT/EC-8th-CN/"
# infopath = "CO-PO-MIT/EC-8th-CN/"
#path = "OOP/CE-15"
#infopath = "OOP/OOP-Marks-15/"

path = "FIT/16/2nd Sem/"
infopath = "FIT/16/2nd Sem/"

allfiles = readDir(path)
# print(allfiles)
for file in allfiles:
    data = readCSV(path + "/" + file)
    cleanData = []
    cleanData.append("Reg No")
    cleanData.append("Course Code")
    cleanData.append("Ass")
    cleanData.append("Att")
    cleanData.append("Q1")
    cleanData.append("Q2")
    cleanData.append("Q3")
    cleanData.append("Q4")
    cleanData.append("Q5")
    # Assumed Internal Marks If  Assessment is not known
    # cleanData.append("Assumed Internal")

    cleanData.append("Internal Marks")
    cleanData.append("End Sem")
    # writeCSV(infopath + "/" + 'Info' + file, cleanData, mode= 'w')
    with open(infopath + "/" + 'Info' + file, 'w', newline='') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(cleanData)

    for row in data:
        # print(row)
        cleanData.clear()
        mm = row[4]

        assAtt = []
        if str(mm).isdecimal():
            v = int(mm)
            # Use this block only if assessment and attendance marks are not known
            """
                 if 29 <= v <= 30:
                     v = v - 10
                     assAtt.append(5)
                     assAtt.append(5)
                 elif 27 <= v <= 28:
                     v = v - 9
                     assAtt.extend(random.sample(range(4, 6), 2))
                 elif 20 < v <= 26:
                     v = v - 8
                     assAtt.append(4)
                     assAtt.append(4)
                 elif v <= 20:
                     v = v - 7
                     assAtt.extend(random.sample(range(3, 5), 2))
             """
            N = []
            R = -1
            c = 0
            while R != v:
                c += 1
                N.clear()
                for j in range(1, 6):
                    N.append(random.randint(0, 4))
                R = sum(N)
            cleanData.append(row[0])
            cleanData.append(row[1])
            # Use below block only when Assessment and Attendance marks are ot known
            # print(assAtt)
            # cleanData.append(str(assAtt[0]))
            # cleanData.append(str(assAtt[1]))
            ####################
            cleanData.append(row[2])
            cleanData.append(row[3])
            cleanData.extend(N)
            # Save Assumed IA marks
            #cleanData.append(v)

            cleanData.append(row[4])
            cleanData.append(row[5])
            # writeCSV(infopath + "/" + 'Info' + file, cleanData, mode= 'a+')
            with open(infopath + "/" + 'Info' + file, 'a+', newline='') as myfile:
                wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
                wr.writerow(cleanData)
            print(c, N, R, cleanData)
