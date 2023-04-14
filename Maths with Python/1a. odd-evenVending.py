n = int(input("Enter the number:\n"))

if n%2==0:
    print("The number is even")
    for i in range(10):
        num = n + 2*i
        print(f"{num},", end =" ")

else:
    print("The number is odd")
    for i in range(10):
        num = n + 2*i
        print(f"{num},", end =" ")