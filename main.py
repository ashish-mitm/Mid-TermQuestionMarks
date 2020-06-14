# read csv file as a list of lists
import csv
from CSVreadwrite import readCSV, writeCSV


#with open('Final_TR_table_2014_18_107.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
#   csv_reader = reader(read_obj)
    # Pass reader object to list() to get a list of lists
#   list_of_rows = list(csv_reader)
#14IT CourseCode
#courseCode=['11101','011101P','11102','011102P','21101','021101P','021103P','21202','021202P','31201','031201P','31411','031411P','41301','041301P','41302','041302P','41404','041404P','41503','041503P','51301','051301P','51402','51403','051403P','51409','051409P','51505','051505P','51511','51513','51516','051516P','51606','51614','051614P','51617','051617P','61201','061201P','61502','061502P','61603','061603P','61604','061604P','61606','61808','61809','061809P','61810','61814','61818','061825P','211101','211202','211303','211405','221201','221201P','231101','231101P','241205','241301','241306']
#15IT courseCode
courseCode =['011101','011101P','011102','011102P','021101','021101P','021103P','021202','021202P','031201','031201P','031411','031411P','041301','041301P','041302','041302P','041404','041404P','051301','051301P','051402','051403','051403P','051409','051409P','051606','051614','051614P','051617','051617P','061201','061201P','061603','061603P','061604','061604P','061606','211101','211202','211303','211405','221201','221201P','231101','231101P','241205','241301','241306']
print(len(courseCode))
#courseCode = readCSV('14-CourseCode.csv')
data = readCSV('15TRIT.csv')
print(len(data))
#print(courseCode[1])
#data.__delitem__(0)
print(courseCode)

for sem in range(1, 9):
    print(sem)
    for code in courseCode:
        print(code)
        D = []
        for i in range(1,len(data)):
            row = data[i]
            if row[10] == '106':
                if row[11] == str(sem):
                    #print(i, sem, row[1])
                   # print(str(row[1]).split()," "+ str(code), str(row[1]).split() == str(code))
                    if str(row[1]) == str(code):
                        D.append(row[0])
                        D.append(row[1])
                        D.append(row[2])
                        D.append(row[3])
                        D.append(row[4])
                        D.append(row[6])
                        #print(D)
                        writeCSV(code+'.csv', D)
                    D.clear()
