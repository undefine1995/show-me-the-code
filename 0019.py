#-*coding:utf-8*-
#python3

import xlrd, codecs
from xml.dom import minidom

def xls2dict(filename, sheetname):
    fp = xlrd.open_workbook(filename)
    table = fp.sheet_by_name(sheetname)
    result = []
    for row in range(table.nrows):
        result.append([])
        for col in range(table.ncols):
            result[row].append(table.cell(row, col).value)

    return result

def create_xml(info, filename):
    doc = minidom.Document()
    #root
    root = doc.createElement('root')
    doc.appendChild(root)
    #student
    student = doc.createElement('number')
    root.appendChild(student)
    #注释
    comment = doc.createComment('数字信息')
    student.appendChild(comment)
    #student中text
    text = doc.createTextNode(str(info))
    student.appendChild(text)

    with codecs.open(filename, 'w', 'utf-8') as fp:
        doc.writexml(fp,'\t', '\t', '\n', 'utf-8')


if __name__ == '__main__':
    info = xls2dict('numbers.xls', 'numbers')
    create_xml(info, 'test.xml')