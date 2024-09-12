import turtle

turtle.speed(10)

turtle.color('red')


turtle.penup()
turtle.goto(-50, 0)
turtle.pendown()
turtle.forward(25)

turtle.right(80)
turtle.forward(50)
turtle.right(40)
turtle.forward(75)

turtle.right(140)  # Adjusted angle to make the line connect
turtle.forward(25)
turtle.right(40)  # Adjusted angle for smooth connection
turtle.forward(50)

turtle.left(40)
turtle.forward(50)

turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.forward(25)

turtle.right(80)
turtle.forward(50)
turtle.right(40)
turtle.forward(75)

turtle.right(140)  # Adjusted angle to make the line connect
turtle.forward(25)
turtle.right(40)  # Adjusted angle for smooth connection
turtle.forward(50)

turtle.left(40)
turtle.forward(50)


turtle.penup()
turtle.goto(-50, 50)
turtle.pendown()
turtle.forward(25)

turtle.right(80)
turtle.forward(50)
turtle.right(40)
turtle.forward(75)

turtle.right(140)  # Adjusted angle to make the line connect
turtle.forward(25)
turtle.right(40)  # Adjusted angle for smooth connection
turtle.forward(50)

turtle.left(40)
turtle.forward(50)


turtle.mainloop()
