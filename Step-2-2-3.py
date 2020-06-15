import copy
import math
import random
from operator import add, truediv

from CSVreadwrite import *

allMarksList = readCSV("Step -1/Info061603.csv")

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

print(QuestCoMap)
print(allMarksList)
print(MarksData)
print(avgMarksList)
