n = int(input("Enter the number: "))
num = int(input("Enter the number of multiples: "))
out = 0
def multiple (a, b): 
    for i in range(b):
        out = ((a)*(i+1))
        print(out, end="\n")
        
multiple(n,num)
