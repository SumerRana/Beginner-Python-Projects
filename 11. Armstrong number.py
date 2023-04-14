n=input("Enter two digit number the number to check Armstrong")
a=int(n[0:1])
b=int(n[1:2])
y="y"
while(True):
	if y=="y":
		if (a**2+b**2)==int(n):
			print("yes")
			y=input("y to try again")
		else:
			print("No")
			y=input("y to try again")
		continue
	else:
		break