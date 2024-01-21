import xlrd

book = xlrd.open_workbook("file_example_XLS_10.xls")

print(f"Quantity of sheets {book.sheets}")
print(f"Names of sheets {book.sheet_names}")
sheet = book.sheet_by_index(0)
print(f"Quantity of columns {sheet.ncols}")
print(f"Quantity of rows {sheet.nrows}")
print(sheet.cell_value(rowx=7, colx=1))

for rx in range(sheet.nrows):
    print(sheet.row(rx))
