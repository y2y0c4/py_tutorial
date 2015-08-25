import random

class lotto:
	lotto_base = []
	def __init__(self, num):
		self.lotto_base = list(range(1,num+1))

	def get_numbers(self): 
		lotto_base = self.lotto_base
		selected_nums = 0
		while (selected_nums<7 ):
			num = random.choice(lotto_base)
			selected_nums += 1
			if(selected_nums == 7):
				print("Bonus number is {0}".format(num))
				lotto_base.remove(num)
			else:
				print("{0}'s number is {1}".format(selected_nums, num))
				lotto_base.remove(num)	 

num = input("Input Maximum Number >> ")
try:
	do_lotto = lotto(int(num))
	do_lotto.get_numbers()
except ValueError:
	print("Wrong Value")