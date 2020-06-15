import copy
import math
import random
from operator import add, truediv

from CSVreadwrite import *

# allMarksList = readCSV("Step -1/Info061603.csv")

allMarksList = readCSV("CO-PO-MIT/14 Batch IT/4/DB/Info51409.csv")

MarksData = copy.deepcopy(allMarksList[1:])

# Convert marks list to integer except 1st row
for one in range(0, len(MarksData)):
    for i in range(0, len(MarksData[1]) - 1):
        MarksData[one][i] = int(MarksData[one][i])
    MarksData[one][10] = int(math.ceil(float(MarksData[one][10])))

# read each row and find the average of each column 2, 3, 4, 5, 6, 7, 8, 9, 10
res_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for eachStudent in MarksData:
    res_list = list(map(add, res_list, eachStudent))
print(res_list)
# Calculate average and store in a new list
avgMarksList = [round(x / len(MarksData), 2) for x in res_list]
# Create Fresh Marks List with average
MarksData.append(avgMarksList)
writeCSV("Step -1/Info061603withAvg.csv", MarksData, mode='w+')

# Question Number CO Mapping
QuestCoMap = [1]
QuestCoMap.extend(random.sample(range(2, 6), 4))

# Prepare Co Attainment Table
COs = ['CO1', 'CO2', 'CO3', 'CO4', 'CO5', 'CO6']
coAttain = {}

# Set Maximum marks of each question
maxMarks = [4, 4, 4, 4, 4]
indirectAttn = random.randint(80, 85)

for i in range(0,5):
    eachCoAttn = [QuestCoMap[i], maxMarks[i], avgMarksList[4+i]]
    internalAvgPer = round((avgMarksList[4+i] / 5) * 100, 2)
    eachCoAttn.append(internalAvgPer)  # Question %
    eachCoAttn.append(avgMarksList[2])  # Attendance Avg
    eachCoAttn.append(avgMarksList[3])  # Assessment Avg
    assAvgPer = round((avgMarksList[2] + avgMarksList[3]) * 10, 2)  # Assessment %
    eachCoAttn.append(assAvgPer)
    eachCoAttn.append(avgMarksList[10])  # University Average
    directAttn = round(0.7 * avgMarksList[10] + 0.1 * assAvgPer + 0.2 * internalAvgPer, 2)
    eachCoAttn.append(directAttn)
   # indirectAttn = random.randint(80, 85)
    eachCoAttn.append(indirectAttn)
    totalAttn = round(0.9 * directAttn + 0.1 * indirectAttn, 2)
    eachCoAttn.append(totalAttn)
    coAttain[COs[i]] = eachCoAttn

# Add CO6 directly
eachCoAttn = ['-', '-', '-', '-', avgMarksList[2], avgMarksList[3]]
# internalAvgPer = round((avgMarksList[4] / 5) * 100, 2)
assAvgPer = round((avgMarksList[2] + avgMarksList[3]) * 10, 2)  # Assessment %
eachCoAttn.append(assAvgPer)
eachCoAttn.append(avgMarksList[10])  # University Average
directAttn = round (0.7 * avgMarksList[10] + 0.1 * assAvgPer + 0.2 * internalAvgPer, 2)
eachCoAttn.append(directAttn)
# indirectAttn = random.randint(80, 85)
eachCoAttn.append(indirectAttn)
totalAttn = round(0.9 * directAttn + 0.1 * indirectAttn, 2)
eachCoAttn.append(totalAttn)
coAttain['CO6'] = eachCoAttn

print(QuestCoMap)
print(allMarksList)
print(MarksData)
print(avgMarksList)
print(coAttain)

with open('Step -2/COAttainment.csv', 'w+', newline='') as csv_file:
    writer = csv.writer(csv_file)
    #writer.writerow("\n")
    step2List = []
    for key, value in coAttain.items():
        step2List.append(key)
        step2List.extend(value)

        # Replace all 0 with -
        for idx, item in enumerate(step2List):
            if item == 0:
                step2List[idx] = '-'

        writer.writerow(step2List)
        step2List.clear()

