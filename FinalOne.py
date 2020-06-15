from CSVreadwrite import *

clkcData = readCSV("CO-PO-MIT/14 Batch IT/4/DB/DB-CLKC.csv")
print(clkcData)

mapStrength = readCSV("Step -2/MappingStrength.csv")
print(mapStrength)

copoMapping = readCSV("Step -2/COPOMapping.csv")
print(copoMapping)
Temp = ['CO/PO/PSO', 'PO1', 'PO2', 'PO3', 'PO4', 'PO5', 'PO6', 'PO7', 'PO8', 'PO9', 'PO10', 'PO11', 'PO12', 'PSO1',
        'PSO2', 'PSO3']
copoMapping.insert(0, Temp)
print(copoMapping)

coAttain = readCSV("Step -2/COAttainment.csv")
print(coAttain)
Temp = ['CO', 'Q. No.', 'Max Marks', 'Average Marks', '% Marks', 'Assessment Average', 'Attendance Average',
        '% Assessment & Attendance', 'University Average', 'Direct Assessment', 'Indirect Assessment',
        'Total Attainment']
coAttain.insert(0, Temp)
print(coAttain)

poPSOAttain = readCSV("Step -2/POPSOAttain.csv")
print(poPSOAttain)
Temp = ['PO/PSO', 'COs', 'Total Session', '% Session', 'Mapping Strength', 'Average of Relevant COs',
        'PO/PSO Attainment']
poPSOAttain.insert(0, Temp)
print(poPSOAttain)

line = ['\n\n']
writeCSV("Step -2/FinalOne.csv", clkcData, mode='w')
writeCSV("Step -2/FinalOne.csv", line, mode='a+')
writeCSV("Step -2/FinalOne.csv", mapStrength, mode='a+')
writeCSV("Step -2/FinalOne.csv", line, mode='a+')
writeCSV("Step -2/FinalOne.csv", copoMapping, mode='a+')
writeCSV("Step -2/FinalOne.csv", line, mode='a+')
writeCSV("Step -2/FinalOne.csv", coAttain, mode='a+')
writeCSV("Step -2/FinalOne.csv", line, mode='a+')
writeCSV("Step -2/FinalOne.csv", poPSOAttain, mode='a+')
writeCSV("Step -2/FinalOne.csv", line, mode='a+')
