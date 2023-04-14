from fractions import Fraction

a=Fraction(input('Enter first fraction: '))
oper = input("Enter your operation i.e +, -, *, /: \n")
b=Fraction(input('Enter second fraction: '))

def add(a,b):
    sum = a+b
    print(f'Sum is: {sum}')
    
def sub(a,b):
    dif = a-b
    print(f'Difference is: {dif}')
    
def mul(a,b):
    pro = a*b
    print(f'Product is: {pro}')
    
def div(a,b):
    rat = a/b
    print(f'Ratio is: {rat}')
    
if oper == "+":
    add(a,b)
    
elif oper == "-":
    sub(a,b)
    
elif oper == "*":
    mul(a,b)
    
else:
    div(a,b)