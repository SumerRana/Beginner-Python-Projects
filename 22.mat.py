import matplotlib.pyplot as plt
import numpy as np

# x=[2,6,6,8,11,9]
# y=[3,6,8,9,7,13]

x=np.linspace(-40,40,1000)
y=x**7+1

fig = plt.figure(figsize = (10, 5))

plt.plot(x,y)
plt.xlabel("x-axis")

plt.ylabel("-axis")
plt.show()