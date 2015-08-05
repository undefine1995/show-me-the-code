#-*coding:utf-8*-
#存在问题,数字的小数点
#单词出现次数相同问题已解决

import re, glob

word_dict = {}

def get_name():
	lis = glob.glob('*.txt')
	if not lis:
		raise Exception('have no file')
	return lis

def num_of_words():
	lis = get_name()

	for item in lis:
		line_list = []
		
		with open(item, 'r') as fp:
			
			for line in fp:
				match = re.findall(r'[^a-zA-Z0-9]', line)

			for i in match:
				line = line.replace(i, ' ')
			line_list = line.split()

			for item in line_list:
				if item not in word_dict:
					word_dict[item] = 1
				else:
					word_dict[item] += 1

def main():
	num_of_words()
	result = {}
	for item in word_dict:
		if not result.get(word_dict[item], None):
			tmp = []
			tmp.append(item)
			result[word_dict[item]] = tmp
		else:
			tmp = []
			for i in result[word_dict[item]]:
				tmp.append(i)
			tmp.append(item)

			result[word_dict[item]] = tmp

	print (max(result), result[max(result)])

if __name__ == '__main__':
	main()
