y="y"
while True:
	if y=="y" or y=="Y":
		n=int(input("Enter the number:\n"))
		i=1
		while True:
			i+=1
			if i<(n-1):
				if n%i!=0:
					continue
				else:
					print(str(n)+" is a composite number.\n\n\n")
					break
			elif i==n:
				print(str(n)+" is a prime number.\n\n\n")
				break
		y=input("Enter y to try another number any other key to end:\n")
		continue
	else:
		print("Thank you!")
		break