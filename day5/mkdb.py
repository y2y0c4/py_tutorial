import sqlite3
import db_test2

class db:
	def __init__(self,db_name):
		self.conn=sqlite3.connect(db_name)
		self.cursor=self.conn.cursor()
	def __del_prev_data__(self):
		self.cursor.execute("DROP TABLE IF EXISTS tmp")
		self.cursor.execute('''CREATE TABLE tmp(
                		date VARCHAR(20),
               		 	temp VARCHAR(20),
		                humi VARCHAR(20),
                		asto VARCHAR(20))''')
	def __write_db__(self, file_name):
		with open(file_name,'r') as f:
        		lines = f.readlines()

		for line in lines:
        		each_item = line.split(',')
        		que="INSERT INTO tmp VALUES('{0}','{1}','{2}','{3}');".format(each_item[0],each_item[1],each_item[2],each_item[3])
        		self.cursor.execute(que)
        		self.conn.commit()

	def __print_result__(self):
		self.cursor.execute('select * from tmp')
		print(self.cursor.fetchall())
	
	def __close__(self):
		self.conn.close()


if __name__=="__main__":
	db_obj = db("tmp.db")
	db_obj.__del_prev_data__()
	db_obj.__write_db__("20150828.txt")
	db_obj.__print_result__()
	db_obj.__close__()
#conn = sqlite3.connect("tmp.db")
#cursor=conn.cursor()
#cursor.execute("DROP TABLE IF EXISTS tmp")
#cursor.execute('''CREATE TABLE tmp(
#		date VARCHAR(20),
#		temp VARCHAR(20),
#		humi VARCHAR(20),
#		asto VARCHAR(20))''')
#

#with open('20150828.txt','r') as f:
#	lines = f.readlines()



#for line in lines:
#	each_item = line.split(',')
#	que="INSERT INTO tmp VALUES('{0}','{1}','{2}','{3}');".format(each_item[0],each_item[1],each_item[2],each_item[3])
#	cursor.execute(que)
#	conn.commit()
#
#cursor.execute('select * from tmp')
#print(cursor.fetchall())
#conn.close()
			
	
