# Import the turtle graphics module to draw on the screen
import turtle

# Create a drawing object (the "pen" or "turtle") controlled by the variable 't'
t = turtle.Pen()

# Move forward 100 pixels (draws the bottom side of the rectangle)
t.forward(100)

# Turn left 90 degrees to face upwards
t.left(90)

# Move forward 50 pixels (draws the right side of the rectangle)
t.forward(50)

# Turn left 90 degrees to face left
t.left(90)

# Move forward 100 pixels (draws the top side of the rectangle)
t.forward(100)

# Turn left 90 degrees to face downwards
t.left(90)

# Move forward 50 pixels (draws the left side, closing the rectangle)
t.forward(50)