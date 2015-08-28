import sqlite3
import datetime
import time
import random

class dt:
	def __init__(self):
		self.dt_now = datetime.datetime.now()
		self.dt_delta = datetime.timedelta(minutes=1)
	def make(self):
		while True:
			self.dt_now =self.dt_now +self.dt_delta
			file_name = self.dt_now.strftime("%Y%m%d.txt")
			date_time = self.dt_now.strftime("%Y%m%d%H%M")
	
			d1=random.randint(0,9999)
			d2=random.randint(0,9999)
			d3=random.randint(0,9999)
	
			data = "{0},{1:04d}, {2:04d}, {3:04d}".format(date_time,d1,d2,d3)
			with open(file_name,'+a') as f:
				f.write(data+"\n")
			
			if(self.dt_now.day==29):
				break

if __name__=="__main__":
	d = dt()
	d.make()
