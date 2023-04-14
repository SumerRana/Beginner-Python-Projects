n1=int(input("Enter the first number: "))
o=input("Enter the operator: ")


if o=="+" or o=="-" or o=="*" or o=="/":
	n2=int(input("Enter the second number: "))
	if o=='+':
		if (n1==56 and n2==9) or (n1==9 and n2==56):
			print("The sum is 77")
		else:
			summ=n1+n2
			print("The sum is "+str(summ))
	elif o=='-':
		dif=n1-n2
		print("The difference is "+str(dif))
	elif o=="*":
		if (n1==45 and n2==3) or (n1==3 and n2==45):
			print("The Product is 555")
		else:
			prod=n1*n2
			print("The Product is "+str(prod))
	else:
		if n1==56 and n2==6:
			print("The ratio is 4")
		else:
			rat=n1/n2
			print("The ratio is "+str(rat))
else:
	print("Please inupur valid operator")