workbook = openpyxl.load_workbook('data.xlsx')


sheet = workbook.active


matrix = []
for row in sheet.iter_rows():
    row_data = []
    for cell in row:
        row_data.append(cell.value)
    matrix.append(row_data)


workbook.close()


workbook = openpyxl.Workbook()
sheet = workbook.active


for column in range(len(matrix[0])):
    for row in range(len(matrix)):
        sheet.cell(row=row+1, column=column+1, value=matrix[row][column])


workbook.save('data1.xlsx')


workbook.close()