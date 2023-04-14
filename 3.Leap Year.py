x=int(input("Enter the year \n"))

if x%4==0:
	if x%400==0:
		print("Yes")
	elif x%100==0:
		print("NO")
	else:
		print("Yes")
else:
	print("No")

