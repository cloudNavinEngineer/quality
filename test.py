__author__ = 'Vivek'
from xlrd import open_workbook
book = open_workbook('NIH_NICCL_06M_SubjectManagement140528AY.xls')
sheet = book.sheet_by_index(1)
# dictionary created to store column values
abc = {}
i=0
for a in sheet.col(0):
    abc[i] = a.value
    i=i+1

# display all the values
print abc
