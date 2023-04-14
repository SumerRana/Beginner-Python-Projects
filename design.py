import turtle
import colorsys
t=turtle.Turtle()
S=turtle.Screen()
S.bgcolor("black")
t.speed(0)
for i in range(3000):
	c=colorsys.hsv_to_rgb(i*0.1,1,0.6)
	t.color(c)
	t.circle(i*0.6)
	t.right(4)
	t.forward(1)

