import xlwt
import xlrd

w=xlwt.Workbook()
ws=w.add_sheet('api')


ws.write(0,0,'test')
ws.write(0,1,'test')
ws.write(0,2,'test')
w.save('d:/apiTest3.xls')
data=xlrd.open_workbook('d:/apiTest3.xls')
table=data.sheet_by_index(0)
print(table.name)
table1=data.sheet_by_name('api')
print(table1.name)
print(table.cell(0,0).value)
table.cell(0,0).value='test1'
print(table.cell(0,0).value)
