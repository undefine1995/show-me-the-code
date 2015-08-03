#-*coding:utf-8*-

import a	#0001.py
import sqlite3

result = list(a.main())

def mysave(dbName, lis):
	cx = sqlite3.connect(dbName)
	cur = cx.cursor()

	sql = 'create table test (id integer primary key,val varchar(20) UNIQUE)'

	cur.execute(sql)

	tmp = []
	for i in range(200):
		tmp.append((i,str(lis[i])))	

	for item in tmp:
		cx.execute("insert into test values (?,?)", item)

	cx.commit()

	#cur.execute('select * from test')
	#print cur.fetchall()

if __name__ == '__main__':
		mysave('test.db',result)
