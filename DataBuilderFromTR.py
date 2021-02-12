import csv

import xlrd
# S. No.	College Code	College Name	Branch Code	Branch Name	Reg. No.	Year	Seat No.	Student Name	Father Name	Mother Name	Course Name	Course Code	As	Att	MSE	Total	ESE	Total out  100/50	Full_mks	% of Total	Letter Grade	GRADE Point	CREDIT	SGPA SEM 1	SGPA SEM 2	SGPA SEM 3	SGPA SEM 4	SGPA SEM 5	SGPA SEM 6	SGPA SEM 7	SGPA SEM 8	CGPA	FAIL IN(IF ANY)	Mark Sheet No	Remarks
book = xlrd.open_workbook("CO-PO-MIT/16 Batch IT/16TRIT.xls")
with open('16TRIT.csv', 'w', newline='') as file:
    writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL, delimiter=',')
    for i in range(0, 8):
        sheet = book.sheet_by_index(i)
        for row in range(sheet.nrows):  # Iterates over your sheet
            oneRow = sheet.row_values(row)
            print(sheet.name + " " + str(sheet.nrows) + " " + oneRow[3])
            cleanData = []
            if str(oneRow[3]) == '106':
                RegNo = oneRow[5]
                courseCode = oneRow[12]
                assignment = oneRow[13]
                att = oneRow[14]
                midSem = oneRow[15]
                midTotal = oneRow[16]
                endSem = oneRow[17]
                examHeld = oneRow[6]
                examName = sheet.name
                collegeCode = oneRow[1]
                branchCode = oneRow[3]
                semester = i + 1
                cleanData.append(RegNo)
                cleanData.append(courseCode)
                cleanData.append(assignment)
                cleanData.append(att)
                cleanData.append(midSem)
                cleanData.append(midTotal)
                cleanData.append(endSem)
                cleanData.append(examHeld)
                cleanData.append(examName)
                cleanData.append(collegeCode)
                cleanData.append(branchCode)
                cleanData.append(semester)
                print(cleanData)
                writer.writerow(cleanData)
                cleanData.clear()


