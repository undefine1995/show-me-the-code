#-*coding:utf-8*-

import os, urllib2, re

def get_html(url):
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    html = response.read()

    return html

def find_img(html):
    pattern = re.compile(r'class="BDE_Image" src="(.*?)"',re.S)
    img = re.findall(pattern, html)
    return img

def save(img,filename):
    os.mkdir(filename)
    os.chdir(filename)
    num = 0
    for item in img:
        imgs = urllib2.urlopen(urllib2.Request(item)).read()
        with open(str(num)+'.jpg', 'wb') as fp:
            fp.writelines(imgs)
            num += 1

if __name__ == '__main__':
    url = 'http://tieba.baidu.com/p/2166231880'
    html = get_html(url)
    img = find_img(html)
    save(img, 'images')