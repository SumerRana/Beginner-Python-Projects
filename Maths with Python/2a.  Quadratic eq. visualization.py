import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
# make data

x=np.linspace(-40,40,1000)
y=a*x*x+b*x+c

    

# plot
# fig, ax = plt.subplots()

# ax.plot(x, y, linewidth=2.0)

# ax.set(xlim=(0, 8), xticks=np.arange(1, 80),
#        ylim=(0, 8), yticks=np.arange(1, 80))

# plt.show()

# Plot that works

fig = plt.figure(figsize = (10, 5))

plt.plot(x,y)
plt.xlabel("x-axis")

plt.ylabel("-axis")
plt.show()