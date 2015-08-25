for i in range(2,9,3):
	for j in range(2,10):
		for k in range(0,3):
			num = i+k
		#	print("%sX%s=%2s"% (str(num) , str(j), str(num*j)),end=" ") if num<10 else None
			print('{0}X{1}={2:2s}'.format(str(num), str(j), str(num*j)), end=" ") if num<10 else None
		print()
	print()
