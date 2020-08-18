import turtle
turtle.shape("turtle")
turtle.penup()
size=20
for i in range(30):
    turtle.stamp()
    size=size+3
    turtle.forward(size)
    turtle.right(24)
    
    turtle.done