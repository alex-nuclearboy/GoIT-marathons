import turtle

# Creating an object of the Turtle class
t = turtle.Turtle()

# Setting the window size
turtle.setup(500, 500)

# Drawing a circle (radius 20 units)
t.circle(20)

# Moving the turtle (30 units forward)
t.forward(30)

# Drawing 5 circles (radius 10 units, 20 units forward)
for _ in range(5):
    t.circle(10)
    t.forward(20)

# Leave the window open
turtle.mainloop()
