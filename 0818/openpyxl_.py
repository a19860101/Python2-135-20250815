import openpyxl

wb = openpyxl.Workbook()
ws = wb.active

ws.append(['日期','標題','作者'])
ws.append(['0816','asdfas;dlfkjas;ldfkjas','dfasdfasdf'])
ws.append(['0818','dfasdfsdfdf','dfdffe321r2r32456254'])

wb.save('test.xlsx')