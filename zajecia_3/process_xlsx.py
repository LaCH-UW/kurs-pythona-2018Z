import openpyxl

# https://openpyxl.readthedocs.io/en/default/tutorial.html

budget_fname = 'dane/budzet/2017_1.xlsx'
wb = openpyxl.load_workbook(budget_fname)
sheet = wb.worksheets[0]

header_row = list(sheet.rows)[0]
for header_cell in header_row:
    print(header_cell.column, header_cell.row, header_cell.value)

print(sheet['A2'].value)

first_column = list(sheet.columns)[0]
for name_cell in first_column:
    print(name_cell.value)

wb.close()