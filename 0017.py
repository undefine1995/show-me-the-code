#-*coding:utf-8*-

import xlrd, codecs
from xml.dom import minidom

def xls2dict(filename, sheetname):
    fp = xlrd.open_workbook(filename)
    table = fp.sheet_by_name(sheetname)
    result = {}
    for row in range(table.nrows):
        result[str(int(table.cell(row, 0).value))] = []
        for col in range(1,table.ncols):
            result[str(int(table.cell(row, 0).value))].append(table.cell(row, col).value)

    return result

def create_xml(info, filename):
    doc = minidom.Document()
    #root
    root = doc.createElement('root')
    doc.appendChild(root)
    #student
    student = doc.createElement('student')
    root.appendChild(student)
    #注释
    comment = doc.createComment('\t学生信息表\n    "id" : [名字, 数学, 语文, 英文]')
    student.appendChild(comment)
    #student中text
    text = doc.createTextNode(str(info))
    student.appendChild(text)

    with codecs.open(filename, 'w', 'utf-8') as fp:
        doc.writexml(fp,'\t', '\t', '\n', 'utf-8')


if __name__ == '__main__':
    info = xls2dict('student.xls', 'student')
    create_xml(info, 'test.xml')