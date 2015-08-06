#-*coding:utf-8*-

X = set()
with open('filtered_words.txt', 'r') as fp:
    for line in fp:
    	X.add(line.strip('\n'))

def judge(_str):
	if _str in X:
		print 'Freedom'
	else:
		print 'Human Rights'

if __name__ == '__main__':
	text = raw_input('input>')
	judge(text)