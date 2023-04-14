n1=int(input("Enter lower limit: "))
n2=int(input("Enter upper limit: "))
i=1
n=n1+1
while True:
	i+=1
	if n<n2:
		if i<n:
			if n%i!=0:
				continue
			else:
				n+=1
				i=1
				continue
		else:
			print(n)
			n+=1
			i=1
			continue
	else:
		break	