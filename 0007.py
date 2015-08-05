#-*coding:utf-8*-
#这里我暂时将源文件完全设为python文件
import os, glob, re


def findfile(folder):
	os.chdir(folder)
	lis = glob.glob('*.py')
	return lis

def count(lis):
	lines_num = 0
	null_line = 0
	note_line = 0
	code_line = 0
	for item in lis:
		with open(item) as fp:
			for line in fp:
				lines_num += 1

				if re.match(r'^[\t ]*$', line) != None:
					null_line += 1

				elif re.match(r'^ *#.*$',line) != None:
					note_line += 1

	code_line = lines_num - null_line - note_line

	return lines_num, null_line, note_line, code_line

if __name__ == '__main__':
	lis = findfile('*:\your\path')
	lines_num, null_line, note_line, code_line = count(lis)
	print "sum %s ,null %s ,note %s ,code %s " % (lines_num, null_line, note_line, code_line)