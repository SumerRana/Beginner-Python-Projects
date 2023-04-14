w=int(input(" Enter your weight(Kg): ")) #ask user for weight
h=input("Enter your height(cm) or type no for ft: ") #ask user for height or change of unit system

if h=="no": #check if unit has to be changed
	f=input("Enter feet: ") 
	i=input("Enter inches: ")
	h1=(int(f)*12+int(i))*2.54 #convert inch to centimeter
else:
	h1=int(h) #chose height as it is in case of inpput in cm

b=w/((h1/100)**2) #calculate bmi
b= round(b,1) #round off bmi

x=24.5*((h1/100)**2) #find ideal weight in case of overweight
y=w-x 
y=round(y,1)

a=18.5*((h1/100)**2) #find ideal weight in case of underweight
z=a-w
z=round(z,1)

if b<18.5: #check for underweight
	print("Underweight. BMI= "+str(b))
	print("you need to put on "+str(z)+" Kg's")
elif b<25: #check for healthy
	print("healthy. BMI= "+str(b))
elif b<30: #check for overweight
	print("Overweight. BMI= "+str(b))
	print("you need to reduce "+str(y)+" Kg's")
else: #check for obese
	print("Obese. BMI= "+str(b))
	print("you need to reduce "+str(y)+" Kg's")






