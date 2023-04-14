import matplotlib.pyplot as plt
import numpy as np

n = 100 #int(input("Enter number of terms: "))

series = [1,1]
a=1
b=1
ratio=[1,2]

for i in range(n):
    c=a+b
    series.append(c)
    a=b
    b=c
    ratio.append(b/a)
    
print(len(series))
print(len(ratio))


#Creating vectors X and Y
x= (np.linspace(1, n+2, n+2))
y = np.array(ratio)


fig = plt.figure(figsize = (10,10))
# Create the plot
plt.plot(x, y)
plt.title("Golden ratio in Fibonacci series")


# Show the plot
plt.show()
    