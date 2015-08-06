#-*coding:utf-8*-

import Image, ImageDraw, ImageFont, ImageFilter
import string, random

def random_string(num):
    #生成验证码
    return ''.join(random.choice(string.ascii_uppercase+string.digits) for x in range(num))

def create_img(text,
    size = (120, 30),
    type = 'jpg',
    mode = 'RGB',
    draw_line = True,
    draw_point = True,
    num_lines = (9,15),
    chance_points = 15,
    bg_color = (225, 225, 225),
    fg_color = (0, 0, 225),
    font_size = 18,
    font_type = 'Arial.ttf'
    ):
    width, height = size
    img = Image.new(mode, size, bg_color)
    draw = ImageDraw.Draw(img)

    #画线(用数目)
    if draw_line:
        num = random.randint(*num_lines)
        for i in range(num):
            begin = (random.randint(0, width), random.randint(0, height))
            end = (random.randint(0,width), random.randint(0, height))
            draw.line([begin, end], fill = (0, 0, 0))

    #画点(用几率)
    if draw_point:
        chance = min(100, max(0, int(chance_points)))
        for x in range(width):
            for y in range(height):
                tmp = random.randint(0, 100)
                if tmp >= 100 - chance:
                    draw.point((x, y), fill = (0, 0, 0))

    #写入字符
    myfont = ImageFont.truetype(font_type, font_size)
    draw.text((0.4*width, 0.4*height), text, fill = fg_color)

    #图像处理
    params = [1 - float(random.randint(1, 2)) / 100, 0, 0, 0, 1 - float(random.randint(1, 10)) / 100, 
    float(random.randint(1, 2)) / 500,
    0.001,
    float(random.randint(1, 2)) / 500
    ]
    #旋转
    img = img.transform(size, Image.PERSPECTIVE, params)
    #边界加强
    img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)

    return img

if __name__ == '__main__':
    str = random_string(4)
    code_img = create_img(str)
    code_img.save('1.jpg')

