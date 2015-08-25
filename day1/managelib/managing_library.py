
data = input("input lists>>>")
data = data.replace('[','');data = data.replace(']','')
splited_data = data.split(',')
total_len = len(splited_data)
each_index = int(total_len/3)
data_list = []
print(splited_data,each_index)
for i in range(0,total_len,3):
	data_list.append({'name':splited_data[i],'author':splited_data[i+1],'price':splited_data[i+2]})	
print(data_list)
with open("data.txt","w") as f:
	f.write("[\n")
	for i in range(len(data_list)):
		f.write("\t"+str(data_list[i]));f.write(',\n')
	f.write("\n]")
	
with open("data.txt","r") as f:
	read_data = f.read()
	print(read_data)
