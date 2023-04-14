import matplotlib.pyplot as plt
import numpy as np

arr = float(input("Enter the angle of projection"))
u = float(input("Enter initial velocity"))

thita = np.deg2rad(arr)

rang = ((u*u)*np.sin(2*thita))/9.81
tof = (2*u*np.sin(thita))/9.81
maxh = ((u*np.sin(thita))**2/(2*9.81))

print("Range =",format(rang,".2f"),"m")
print("Time of flight =",format(tof,".2f"),"s")
print("Max height =",format(maxh,".2f"),"m")


#plot


# Creating vectors X and Y
x = np.linspace(0, rang+1, 100)
y = (x*np.tan(thita)*(1-(x/rang)))

plt.ylim(1,rang)

fig = plt.figure(figsize = (10,10))
# Create the plot
plt.plot(x, y)
plt.title("Projectile motion")


# Show the plot
plt.show()

