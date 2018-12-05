import xlrd
# z dokumentacją nie ma szału...
# https://github.com/python-excel/tutorial/raw/master/python-excel.pdf
# https://xlrd.readthedocs.io/en/latest/
# ale głównie należy wołać help() i dir() na czym się da...

absence_fname = 'dane/zus/2013.xls'
wb = xlrd.open_workbook(absence_fname)
sheet = wb.sheet_by_index(0)

for i in range(sheet.nrows):
    for cell in sheet.row(i):
        if cell.value == 'OGÓŁEM':
            start_row = i
            break

for i in range(start_row, start_row + 5):
    for cell in sheet.row(i):
        print(cell.value)
