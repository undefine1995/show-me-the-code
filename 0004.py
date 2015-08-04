#-*coding:utf-8*-

import re

filename = 'text.txt'
#words_num = 0
word_dict = {}

def num_of_words(filename):

	lines_list = []
	words_num = 0

	with open(filename, 'r') as fp:
		for line in fp:
			match = re.findall(r'[^a-zA-Z0-9]+',line)

		for i in match:
			line = line.replace(i, ' ')
		lines_list = line.split()
		words_num += len(lines_list)

		for i in lines_list:
			if i not in word_dict:
				word_dict[i] = 1
			else:
				word_dict[i] += 1
	return words_num
if __name__ == '__main__':
	print num_of_words(filename)
	#print words_num