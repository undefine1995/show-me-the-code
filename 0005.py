#-*coding:utf-8*-

import Image, glob

iphone5 = (1136,640)

def get_name():
	lis = glob.glob('*.jpg')
	return lis

def change(filename, num):
	im = Image.open(filename)
	img = im.resize(iphone5)
	img.save("./"+str(num)+".jpg", 'jpeg')

def main():
	lis = get_name()

	for i in lis:
		num = 0
		change(str(i),num)

if __name__ == '__main__':
	main()