n=int(input("Enter the number to find factorial: "))
f=1
while(True):
	if n>1:
		f=f*n*(n-1)
		n-=2
		continue
		print("fd")
	elif n<=1:
		print("factorial is"+str(f))
		t=input("Press y to find another factorial n to exit: ")
		if t=="y":
			n=int(input("Enter the number to find factorial: "))
			f=1
			continue
		else:
			break
		
