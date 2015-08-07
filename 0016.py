#-*coding:utf-8*-

import xlwt

def get_info(filename):
	result = ''
	with open(filename, 'r') as fp:
		for line in fp:
			result += line

	return eval(result)


def list2xls(info):
	fp = xlwt.Workbook()
	table = fp.add_sheet('list2xls', cell_overwrite_ok = True)
	raw = col = 0
	for item in info:
		for i in item:
			table.write(raw, col, i)
			col += 1

		col = 0
		raw += 1

	fp.save('test.xls')

if __name__ == '__main__':
	info = get_info('test.txt')
	print 'please wait 3 seconds'
	list2xls(info)