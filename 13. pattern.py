i=0
y="y"
while True:
	n=int(input("Enter the number: "))
	b=bool(int(input("Enter 1 for upright, 0 for upside down patter: ")))
	a=n
	i=0
	p=""
	if y=="y" or y=="Y":
		if b==True:
			while True:
				if i<n:
					i+=1
					p=p+"*"
					print(p)
					continue
				else:
					break

		else:
			while True:
				if i<n:
					i+=1
					p=a* "*"
					print(p)
					a-=1
					continue
				else:
					break
		y=input("Enter y to start again n to STOP: ")
		
		continue
	else:
		print("Thank You")
		break