
def DrawDiamond(height):
	a = []
	if(height<22):
		index=0
		for i in range(1,height+1,2):
			a.append('')
			for j in range(height-int(i/2)):
				a[index]+=" "

			for j in range(i):
				a[index]+="*"
			index+=1
			
		a.append('-')
		for i in range(len(a)):
			if(a[i]!='-'):
				print(a[i]);
			else:
				a.reverse()
				for i in range(len(a)):
					if(a[i]=='-'):
						None
					elif(i==1):
						None
					else:
						print(a[i])
	else:
		print("It's too long")
