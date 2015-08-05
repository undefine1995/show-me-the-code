#-*coding:utf-8*-

#爬自己博客将正文存为md格式：http://undefine1995.github.io/2015/05/31/wuyuemo/
import re, urllib, urllib2

def openurl(url):
	req = urllib2.Request(url)
	response = urllib2.urlopen(req)
	page = response.read()

	return page

def find_content(page):
	 pattern = re.compile('<h1 class="article-title".*?>(.*?)</h1>',re.S)
	 title = re.findall(pattern,page)
	 title = re.sub(r' ','',str(title[0]))
	 #print title

	 pattern = re.compile('<div class="article-entry.*?>(.*?)</div>',re.S)
	 content = re.findall(pattern,page)
	 content = re.sub(r' ','',str(content[0]))
	 #print content

	 return (title, content)

def saveas(filename, title, content):
	with open(filename,'w') as fp:
		fp.writelines('<h1>' + title + '</h1>')
		fp.writelines(content)


if __name__ == '__main__':
	page = openurl('http://undefine1995.github.io/2015/05/31/wuyuemo/')
	title, content = find_content(page)
	saveas('article.md', title, content)