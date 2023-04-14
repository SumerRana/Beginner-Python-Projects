import numpy as np
import matplotlib.pyplot as plt


# creating the dataset
data = {}

cont = "y"

while True:
    if cont=="y":
        expa=input("Enter the expanse: ")
        wort=int(input("Enter the amount: "))
        data[expa]=wort
        cont=input("Enter y to add more anything else to get the graph: ")
        continue
    else:
        break
        
expanses = list(data.keys())
Amount = list(data.values())

fig = plt.figure(figsize = (10, 5))

# creating the bar plot
plt.bar(expanses, Amount, color ='maroon',
		width = 0.4)

plt.xlabel("Expanses")
plt.ylabel("Amount")
plt.title("Expanses depiction")
plt.show()
