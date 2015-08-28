import sqlite3

conn = sqlite3.connect('test.db')

cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS lover")

cursor.execute('''CREATE TABLE lover(
		name VARCHAR(20),
		age INT(10),
		sex VARCHAR(20),
		birth DATE,
		death DATE,
		phon VARCHAR(20))''')

data = {
	"name":"Dasom",
	"age":22,
	"sex":"female",
	"birth":"1990-06-08",
	"death":"NULL",
	"phone":"010-1010-1010"
}

que="INSERT INTO lover VALUES('{name}',{age},'{sex}','{birth}','{death}','{phone}')".format_map(data)
#print(que)
cursor.execute(que)
conn.commit()

cursor.execute('select * from lover')
#conn.commit()
print(cursor.fetchone())
