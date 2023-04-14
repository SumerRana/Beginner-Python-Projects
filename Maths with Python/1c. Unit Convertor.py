unit=int(input("Enter the unit\nPress 1 mass\nPress 2 for Length\nPress 3 for Temperature\n"))
inp=int(input("Enter the input\n"))
out = 0

def ml(n, num):
    o= n*num
    return o

def FtoC(F):
    C = (F-32)(9/5)
    return C

def CtoF(C):
    F = (9*C/5)+32
    return F
    
if unit==1:
    way=int(input("Enter 1 for Kg to lbs\n2 for lbs to Kg\n"))
    if way==1:
        print(ml(inp,2.2))
    else:
        print(ml(inp,0.45))
        
elif unit==2:
    way=int(input("Enter 1 for Km to Mi\nEnter 2 for Mi to Km\n"))
    if way==1:
        print(ml(inp, 0.62))
    else:
        print(ml(inp, 1.6))

else:
    way=int(input("Enter 1 for °C to °F\nEnter 2 for °F to °C\n"))
    if way==1:
        print(CtoF(inp))
    else:
        print(FtoC(inp))