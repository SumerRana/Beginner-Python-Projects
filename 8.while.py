# num=int(input("Guess the number: "))
num=int(input("Guess the number: "))
i=0
while(True):

	i+=1
	if i<5:
		# i+=1
		if num>16:
			print("Try lower")
			num=int(input("Guess again: "))
		elif num < 16:
			print("Try Higher")
			num=int(input("Guess again: "))
		if num==16:
			print("You guessed it")
		else:
			print("")
		continue
		
			print("No more guesses")

	
	break