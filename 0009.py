#-*coding:utf-8*-

#爬自己博客首页将链接存为md格式：http://undefine1995.github.io/
import re, urllib, urllib2

def openurl(url):
	req = urllib2.Request(url)
	response = urllib2.urlopen(req)
	page = response.read()

	return page

def find_link(page):
	pattern = re.compile('<a href="(.*?)"',re.S)
	link = re.findall(pattern,page)
	return link

def saveas(filename, link):
	with open(filename,'w') as fp:
		for item in link:
			fp.writelines(str(item) + '<br>')


if __name__ == '__main__':
	page = openurl('http://undefine1995.github.io/')
	link = find_link(page)
	saveas('link.md', link)