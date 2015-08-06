#-*coding:utf-8*-

import re

def get_filtered_words(filename):
	X = ''
	with open(filename, 'r') as f:
		for line in f:
			X += line.strip('\n')+'|'

	return X.strip('|')
			

def sub_text(x, text):
	match = re.findall(x,text)
	#print match
	for item in match:
		text = text.replace(item, '**')

	return text

if __name__ == '__main__':
	text = ''
	x = get_filtered_words('filtered_words.txt')
	with open("test.txt", 'r') as fp:
		for line in fp:
			text += sub_text(x, line)

	with open("test.txt", 'w') as fp:
		fp.writelines(text)