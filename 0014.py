#-*coding:utf-8*-

import xlwt

def get_info(filename):
	result = ''
	with open(filename, 'r') as fp:
		for line in fp:
			result += line

	return eval(result)

def dict2xls(info):
	file = xlwt.Workbook()
	table = file.add_sheet('test', cell_overwrite_ok = True)
	raw = col = 0
	for item in info:
		table.write(raw,col,item)
		for it in info[item]:
			col += 1
			table.write(raw,col,str(it).decode())
		col = 0
		raw += 1

	file.save('test.xls')

if __name__ == '__main__':
	info = get_info('test.txt')
	print 'please wait 3 seconds'
	dict2xls(info)