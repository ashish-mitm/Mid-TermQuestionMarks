import math

from CSVreadwrite import *

pos = []
cosDict = {}
cosINpo = []
posINco = dict()
totalSession = 0
coWithSession = {}
poSessions = {}
data = readCSV("Step -1/CLKC.csv")

# CO - PO Dictionary
for i in range(1, 7):
    cosDict['CO' + str(i)] = data[i][3].split(',')

# Total Session
for i in range(1,7):
    totalSession += int(data[i][6])

# Co - Session Dictionary
for i in range(1,7):
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
    temp = math.ceil((poSessions.get(po)/totalSession)*100)
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


print(pos)
print(cosDict)
print(posINco)
print(coWithSession)
print(poSessions)
print(posINco_copy)

# Simple list to save
step2List = ["PO/PSO", "COs", "Total Session", "%Session", "Mapping Strength"]

# Save it to Step -2
with open('Step -2/POMapping.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(step2List)
    step2List.clear()
    for key, value in posINco.items():
        step2List.append(key)
        step2List.extend((value))
        writer.writerow(step2List)
        step2List.clear()
       # writer.writerow([key, value])