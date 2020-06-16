import math
from operator import add, truediv
import clkcMarksFilePath

from CSVreadwrite import *

Cos = ['CO1', 'CO2', 'CO3', 'CO4', 'CO5', 'CO6']
POsPSOs_Original = ['PO1', 'PO2', 'PO3', 'PO4', 'PO5', 'PO6', 'PO7', 'PO8', 'PO9', 'PO10', 'PO11', 'PO12', 'PSO1',
                    'PSO2', 'PSO3']
avg_divider = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
pos = []
cosDict = {}
cosINpo = []
posINco = dict()
totalSession = 0
coWithSession = {}
poSessions = {}
#data = readCSV("Step -1/CLKC.csv")
data = readCSV(clkcMarksFilePath.clkcFilePath)
# CO - PO Dictionary
for i in range(1, 7):
    cosDict['CO' + str(i)] = data[i][3].split(',')
#print(cosDict)
# Total Session
for i in range(1, 7):
    totalSession += int(data[i][6])

# Co - Session Dictionary
for i in range(1, 7):
    coWithSession[data[i][1]] = data[i][6]

# List of POs and PSO
pos.extend(data[1][3].split(','))
pos.extend(data[2][3].split(','))
pos.extend(data[3][3].split(','))
pos.extend(data[4][3].split(','))
pos.extend(data[5][3].split(','))
pos.extend(data[6][3].split(','))
pos = list(dict.fromkeys(pos))
list.sort(pos)

print(pos)
# Looking for POs in Dictionary : To be Printed in Column 0 and 1
# print(pos)
for po in pos:
    cosINpo.clear()
    for co in cosDict:
        temp = cosDict[co]
        # print(temp)
        if po in temp:
            # print(po)
            cosINpo.append(co)
        # print(cosINpo)
    posINco[po] = cosINpo.copy()
    # print(posINco)
    # input("Press Enter to continue...")
posINco_Original = posINco.copy()
posINco_copy = posINco.copy()
for po in posINco:
    temp = posINco_copy.get(po)
    temp = ','.join(temp)
    posINco_copy[po] = list(temp.split())

# Co total Session for POs : To be Printed in Column 2
for po in posINco:
    temp = posINco[po]
    m = 0
    for co in temp:
        m += int(coWithSession[co])
    poSessions[po] = m

# % Session : To be printed in column 3
posINco = posINco_copy.copy()
for po in posINco:
    temp = math.ceil((poSessions.get(po) / totalSession) * 100)
    posINco[po].append(str(poSessions.get(po)))
    posINco[po].append(str(temp))
    if temp >= 40:
        posINco[po].append('3')
    elif 25 <= temp < 40:
        posINco[po].append('2')
    elif 5 <= temp < 25:
        posINco[po].append('1')
    else:
        posINco[po].append('-')
attn = {}
# Co-PO Mapping Table
for co in Cos:
    L = []
    K = []
    for po in POsPSOs_Original:
        if po in posINco_Original:
            temp = posINco_Original[po]
            # print(temp)
            if co in temp:
                L.append(int(posINco_copy.get(po)[3]))
                K.append(1)
            else:
                L.append(0)
                K.append(0)
                # print(co,temp)
        else:
            L.append(0)
            K.append(0)
    attn[co] = L.copy()
    L.clear()
    avg_divider = list(map(add, avg_divider, K))
    K.clear()
    # print(attn)
# CO-PO strength Average attn Average
res_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
avg_list = []
for co in Cos:
    temp = attn[co]
    res_list = list(map(add, res_list, temp))
# totalCOsForAvg = 6
# newList = [x / totalCOsForAvg for x in res_list]
# avgListCOPO = list(map(truediv, res_list, avg_divider))
print(res_list)
for i in range(0, len(avg_divider)):
    if avg_divider[i] != 0:
        res_list[i] /= avg_divider[i]
avgListCOPO = res_list.copy()
print(res_list)
print(avg_divider)
# print(avgListCOPO)

attn['AVG'] = avgListCOPO

print(pos)
print(cosDict)
print(posINco_Original)
print(posINco)
print(coWithSession)
print(poSessions)
print(posINco_copy)
print(attn)

# Simple list to save
step2List = ["PO/PSO", "COs", "Total Session", "%Session", "Mapping Strength"]

# Save it to Step -2
with open('Step -2/MappingStrength.csv', 'w+', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(step2List)
    step2List.clear()
    for key, value in posINco.items():
        step2List.append(key)
        step2List.extend((value))
        writer.writerow(step2List)
        step2List.clear()
    # writer.writerow([key, value])

with open('Step -2/COPOMapping.csv', 'w+', newline='') as csv_file:
    writer = csv.writer(csv_file)
    # writer.writerow("\n")
    step2List = []
    for key, value in attn.items():
        step2List.append(key)
        step2List.extend(value)

        # Replace all 0 with -
        for idx, item in enumerate(step2List):
            if item == 0:
                step2List[idx] = '-'

        writer.writerow(step2List)
        step2List.clear()
