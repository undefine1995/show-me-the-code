#-*coding:utf-8*-

#计算平均成绩
import xlrd

def get_aver(filename, sheetname):
	fp = xlrd.open_workbook(filename)
	table = fp.sheet_by_name(sheetname)
	num = table.nrows
	sum = 0
	for row in range(num):
		sum += (table.cell(row, 2).value)

	return (sum/num)

if __name__ == '__main__':
	print(get_aver('20.xls', 'Worksheet'))