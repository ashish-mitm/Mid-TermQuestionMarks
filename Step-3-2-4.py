import re

from CSVreadwrite import *

# Read Mapping Strength File
mappingStrength = readCSV("Step -2/MappingStrength.csv")
mappingStrength = mappingStrength[1:]
print(mappingStrength)

# Read Co Attainment File
coAttainTable = readCSV("Step -2/COAttainment.csv")
print(coAttainTable)

coAttainDict = {}
for y in coAttainTable:
    coAttainDict[y[0]] = y[11]

print(coAttainDict)

for i in range(0, len(mappingStrength)):
    allCOsToPOs = mappingStrength[i][1].split(",")
    print(allCOsToPOs)
    strengthTotal = 0.0
    k = 0
    for co in allCOsToPOs:
        strengthTotal += float(coAttainDict.get(co))
        k += 1
    mappingStrength[i].append(round(strengthTotal / k, 2))
    poPSOAttain = round(int(mappingStrength[i][4]) / 3 * (strengthTotal / k), 2)
    mappingStrength[i].append(poPSOAttain)
print(mappingStrength)

writeCSV("Step -2/POPSOAttain.csv", mappingStrength, mode='w')

# pos = readCSV("Step -2/MappingStrength.csv")
# pos = pos[1:]
popsoList = []
for p in mappingStrength:
    popsoList.append(p[0])
print(popsoList)

temp = re.findall(r'\d+', str(popsoList))
res = list(map(int, temp))
print(res)

mappingStrengthPOPSOAttain = [['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                              ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', ]]

