import datetime
import time
import random

dt = datetime.datetime(2015,8,9,00,00,00)
dt_delta = datetime.timedelta(minutes=1)
random_num=['','','','',]

with open('date.txt','a+') as f:
	while (dt.day<20):
		dt_str = dt.strftime("%Y%m%d")
		for i in range(4):
			random_num = random.randint(1000,9999)
		dt_str_with_all = dt.strftime("%Y%m%d %H:%M")
		f.write(str(dt_str_with_all) + "_" + str(random_num) + "\n")
		dt = dt + dt_delta          
