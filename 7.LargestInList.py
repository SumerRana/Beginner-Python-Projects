list=[3,54,56,23,7,23,5,8,34,24,54,3,3,3,3,23,23,23]


listq=[]
for x in list:
	if x not in listq:
		listq.append(x)

print(listq)