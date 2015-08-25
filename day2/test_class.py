class MyInt:
	def __init__(self, x):
		self.x = int(x)
		return self.x

	def __del__(self):
		print("myint's __del__")

class Calculator(MyInt):
	test = 10
	def __init__(self, x):
		self.x = x
		self.test = 5
		print("initial number is {0} and {1} ".format(x, self.test))

	def __add__(self, x):
		print("{0} add {1}".format(self.x, x), end = ' ')
		self.x += x
		print("is {0}".format(self.x))

	def __mul__(self, x):
		print("{0} mul {1}".format(self.x, x), end = ' ')
		self.x *= x
		print("is {0}".format(self.x))

	def __sub__(self, x):
		print("{0} sub {1}".format(self.x, x), end = ' ')
		self.x -= x
		print("is {0}".format(self.x))

	def __truediv__(self, x):
		print("{0} div {1}".format(self.x, x), end = ' ')
		self.x = MyInt.__init__(self, self.x/x)
		print("is {0}".format(self.x))
		



#number = Calculator(12)
#number.__add__(6)
#number.__truediv__(4)

looong = """
The most beutuful Idol is Dasom of Sistar
and Sulhyun of AOA and sunmi of Wondergirs, EXID's Hani!!!
The best Face Announcer is Kim sunsin
"""
print(looong.__repr__())
print(looong)
print(type(looong))
