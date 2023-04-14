i=0
n=10
while True:
	if n<101:
		while True:
			if i<n:
				i+=1
				if i<10:
					print("0"+str(i),end=" ")
				else:
					print(i,end=" ")
				continue
			else:
				n+=10
				print("\n")
				break
		continue
	else:
		break

