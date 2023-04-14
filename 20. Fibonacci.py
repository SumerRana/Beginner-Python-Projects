y="y"
while True:
	if y=="y" or y=="Y":
		n=int(input("Enter the limit: "))

		def nacci(n):
			if n==0:
				return 0
			if n==1:
				return 1
			return (nacci(n-1)+nacci(n-2))

		for i in range(n):
			print(nacci(i), end=", ")

		y=input("\nY to continue\n")
		continue
	else:
		print("Ty")
		break
