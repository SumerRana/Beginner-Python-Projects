# num=int(input("Guess the number: "))
i=0

while(True):
	num=int(input("Guess the number: "))
	i+=1
	if i<=4:
		x=5-i
		if num==16:
			print("You guessed it with "+str(x)+" chances remaining")
			break
		if num>16:
			print(str(x)+" chances left. Try going lower")
			# num=int(input("Guess again: "))
		elif num < 16:
			print(str(x)+" chances left. Try going higher")
			# num=int(input("Guess again: "))
		continue
	else:
		print("No more guesses")
		y=input("press y to retry or n to exit: ")
		if y=="y":
			i=0
			continue
		else:
			break
	break
