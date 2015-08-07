#-*coding:utf-8*-

import xlrd, codecs
from xml.dom import minidom
import pprint
#pprint.pprint(dir(xlrd))
def get_info(filename, sheetname):
	fp = xlrd.open_workbook(filename)
	table = fp.sheet_by_name(sheetname)
	result = {}
	for row in range(table.nrows):
		result[int(table.cell(row,0).value)] = table.cell(row,1).value

	return result

def creat_xml(info, filename):
	doc = minidom.Document()
	root = doc.createElement('root')
	doc.appendChild(root)

	city = doc.createElement('city')
	root.appendChild(city)

	comm = doc.createComment('城市信息')
	city.appendChild(comm)

	content = doc.createTextNode(str(info))
	city.appendChild(content)

	with codecs.open(filename, 'w' ,'utf-8') as fp:
		doc.writexml(fp,'\t', '\t', '\n', 'utf-8')

if __name__ == '__main__':
	info = get_info('city.xls','city')
	creat_xml(info, 'test.xml')