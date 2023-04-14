y="y"
while True:
	if y=="y" or y=="Y":

		def getdate():
			import datetime
			return datetime.datetime.now()

		u=int(input("Please enter username: \n1 for Larry\n2 for Rohan\n3 for Hammad\n"))

		if u:
			u=input("Hello Larry\npress 1 for diet\npress 2 for workout\n")
			if u=="1":
				o=int(input("press 1 to write\npress 2 to read\n"))
				if o==1:
					ld=input("What did you eat Larry?\n")
					with open("health_management/LD.txt","a") as l:
						l.write(ld+" at "+str(getdate()))
				elif o==2:
					with open("health_management/LD.txt","r") as l:
						print(l.read())

			elif u=="2":
				o=int(input("press 1 to write\npress 2 to read\n"))
				if o==1:
					ld=input("What exercises did you do Larry?\n")
					with open("health_management/LW.txt","a") as l:
						l.write(ld+" at "+str(getdate()))
				elif o==2:
					with open("health_management/LW.txt","r") as l:
						print(l.read())

		elif u==2:
			u=input("Hello Rohan\npress 1 for diet\npress 2 for workout\n")
			if u=="1":
				o=int(input("press 1 to write\npress 2 to read\n"))
				if o==1:
					ld=input("What did you eat Rohan?\n")
					with open("health_management/RD.txt","a") as l:
						l.write(ld+" at "+str(getdate()))
				elif o==2:
					with open("health_management/RD.txt","r") as l:
						print(l.read())
			elif u=="2":
				o=int(input("press 1 to write\npress 2 to read\n"))
				if o==1:
					ld=input("What exercises did you do Rohan?\n")
					with open("health_management/RW.txt","a") as l:
						l.write(ld+" at "+str(getdate()))
				elif o==2:
					with open("health_management/RW.txt","r") as l:
						print(l.read())
		elif u==3:
			u=input("Hello Hammad\npress 1 for diet\npress 2 for workout\n")
			if u=="1":
				o=int(input("press 1 to write\npress 2 to read\n"))
				if o==1:
					ld=input("What did you eat Hammad?\n")
					with open("health_management/HD.txt","a") as l:
						l.write(ld+" at "+str(getdate()))
				elif o==2:
					with open("health_management/HD.txt","r") as l:
						print(l.read())
			elif u=="2":
				o=int(input("press 1 to write\npress 2 to read\n"))
				if o==1:
					ld=input("What exercises did you do Hammad?\n")
					with open("health_management/HW.txt","a") as l:
						l.write(ld+" at "+str(getdate()))
				elif o==2:
					with open("health_management/HW.txt","r") as l:
						print(l.read())
		y=input("\n\n\nEnter y to start again any other key to quit\n")
		continue
	else:
		print("Thank You!")
