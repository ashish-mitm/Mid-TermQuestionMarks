import os
import random
import time

from CSVreadwrite import readDir, readCSV, writeCSV

path = "Result-15/TH/Th New"
infopath = "Result-15/ThInfoMarks- 15/Info5thsem- 15"
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
    cleanData.append("Assumed Internal")

    cleanData.append("Internal Marks")
    cleanData.append("End Sem")
    writeCSV(infopath + "/" + 'Info' + file, cleanData)
    for row in data:
        # print(row)
        cleanData.clear()
        mm = row[4]
        if str(mm).isdecimal():
            v = int(mm)
            if 29 <= v <= 30:
                v = v - 10
            elif 27 <= v <= 28:
                v = v - 9
            elif 20 < v <= 26:
                v = v - 8
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
            cleanData.append(row[2])
            cleanData.append(row[3])
            cleanData.extend(N)
            # Save Assumed IA marks
            cleanData.append(v)

            cleanData.append(row[4])
            cleanData.append(row[5])
            writeCSV(infopath + "/" + 'Info' + file, cleanData)
            print(c, N, R, cleanData)
