#-*coding:utf-8*-

from PIL import Image,ImageDraw,ImageFont

filename = '0.jpg'
newfile = 'new.jpg'
mycolor = (255,0,0)

def draw_img(filename,newfile,mycolor,string):
	try:
		img = Image.open(filename)
		draw = ImageDraw.Draw(img)

		x,y = img.size
		fontsize = min(x,y) // 6

		myfont = ImageFont.truetype('Arial.ttf',fontsize)
		draw.text([0.7*x,0.3*y-fontsize],string,fill = mycolor,font = myfont)

		img.save(newfile)
		img.show()

	except Exception as e:
		raise Exception('something error')

if __name__ == "__main__":
    #number = str(raw_input('please input number: '))
    number = str(4)
    draw_img(filename, newfile, mycolor, number)
