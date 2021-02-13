import csv

from CSVreadwrite import readCSV, writeCSV


def find(target):
    for i, lst in enumerate(target):
        for j, color in enumerate(lst):
            if color == 'CO':
                return i, j
    return None, None


Data = readCSV("CO-PO-MIT/15 Batch IT/8/XML/FinalOne.csv")
courseName = readCSV("CO-PO-MIT/16 Batch IT/CourseCode-SubjectName.csv")

len = len(courseName)
cCode = Data.__getitem__(1)[0]
cName = ""
for i in range(len):
    if Data[2][0] == courseName.__getitem__(i)[0]:
        cName = courseName.__getitem__(i)[1]

len = Data.__len__()
beginData = 0
for i in range(len):
    #print(Data.__getitem__(i)[0])
    if Data.__getitem__(i)[0] == 'CO':
        #print(Data.__getitem__(i)[0])
        beginData = i+1
#print(beginData)
# print(cName+" "+str(cCode))
COAttainment = []
for i in range(0, 6):
    COAttainment.append([cName,cCode,Data[beginData+i][0],round(float(Data[beginData+i][9])*0.03,2), round(float(Data[beginData+i][10])*0.03,2), round(float(Data[beginData+i][11])*0.03,2)])
print(COAttainment)

writeCSV("CO-PO-MIT/16 Batch IT/CoAttainment15BatchAllSubjectIT.csv",COAttainment)

PoAt=[cName,cCode,'-','-','-','-','-','-','-','-','-','-','-','-','-','-','-',]
poIndex = {'PO1':2,'PO2':3,'PO3':4,'PO4':5,'PO5':6,'PO6':7,'PO7':8,'PO8':9,'PO9':10,'PO10':11,'PO11':12,'PO12':13,'PSO1':14,'PSO2':15,'PSO3':16}
PoAttainments = Data[beginData+8:len-1]
print(PoAttainments)
for p in PoAttainments:
    v =""
    if " " in p[0]:
        v = poIndex[p[0].strip()]
    else:
        v = poIndex[p[0]]
    PoAt.__setitem__(v,round(float(p[6])*0.03,2))
print(PoAt)

with open("CO-PO-MIT/16 Batch IT/PoPSOAttainment15BatchAllSubjectIT.csv", "a+", newline='') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL, delimiter=',')
    wr.writerow(PoAt)

#PoS = PoAttainments[1][0].split('.')[0]
#print(PoAttainments)
#print(PoS)