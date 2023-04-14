import time
from plyer import notification
from datetime import datetime
import tkinter as tk

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300)
canvas1.pack()

n1=0
n2=0
n3=0

x=6
z=12
def hello ():  
    print("chal gaya")
    

    def log(file,n):
        # datetime_str = "31OCT2020231032"
        x = datetime.now()
        date = x.strftime("%x")
        time = x.strftime("%X")
        name=(str(file)+".txt")

        f=open(name,"a")
        t=str(n)+". "+str(date)+"  "+str(time)+"\n"
        f.write(t)
        f.close()


    def eye():
        notification.notify(
            title = 'Eye Exercise',
            message = 'Time to exercise your eyes',
            timeout = 30,
            app_icon = "eye.ico"
        )
        global n1
        n1+=1
        log("eye",n1)
        

    def exercise():
        notification.notify(
            title = 'Physical Exercise',
            message = 'Time for physical exercise',
            timeout = 30,
            app_icon = "dumbbell.ico"
        )
        global n2
        n2+=1
        log("exercise",n2)
        

    def water():
        notification.notify(
            title = 'Drink water',
            message = 'Time to drink some water',
            timeout = 30,
            app_icon = "water-glass.ico"
        )
        global n3
        n3+=1
        log("water",n3)
        

                

    while True:
        time.sleep(z)
        water()

        time.sleep(x)
        eye()

        time.sleep(15)
        exercise()
        
        continue

    # while True:
    #     time.sleep(27)
    #     exercise()
    #     b+=b
    #     break

    # while True:
    #     time.sleep(z)
    #     water()
    #     c+=c
    #     break
    
button1 = tk.Button(text='Click Me',command=hello, bg='brown',fg='white')
canvas1.create_window(150, 150, window=button1)

root.mainloop()

