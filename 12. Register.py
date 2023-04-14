
list1=[]
i=0
while(True):
	a=input("Want to register?, press y for yes, n for no: ")
	if a=="y" or a=="Y":
		x=input("Enter your name: ")
		y=input("Class: ")
		z=input("Roll no.: ")
		if z.isnumeric()==True:
			if z in list1:
				print("user already exists")
			else:
				list1.append({"Name": x,"Class": y,"Roll no.": z})
				# print(z in list1)
		else: print("roll no. must be NUMBER")
		continue
	else:
		break
print(list1)
 
# print(z not in list1)


# {"Name": x,"Class": y,"Roll no.": z}