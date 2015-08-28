import sqlite3
import db_test2

conn = sqlite3.connect("tmp.db")
cursor=conn.cursor()
cursor.execute("DROP TABLE IF EXISTS tmp")
cursor.execute('''CREATE TABLE tmp(
		date VARCHAR(20),
		temp VARCHAR(20),
		humi VARCHAR(20),
		asto VARCHAR(20))''')


with open('20150828.txt','r') as f:
	lines = f.readlines()

for line in lines:
	each_item = line.split(',')
	que="INSERT INTO tmp VALUES('{0}','{1}','{2}','{3}');".format(each_item[0],each_item[1],each_item[2],each_item[3])
	cursor.execute(que)
	conn.commit()

cursor.execute('select * from tmp')
print(cursor.fetchall())
conn.close()
			
	
