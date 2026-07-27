import turtle
import random

# Setup
tu = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("🌈 Enhanced Fractal Tree")
tu.pensize(2)
tu.speed(0)  # Fastest speed
tu.left(90)
tu.color("green")

# List of colors for different effects
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "cyan", "magenta"]

def draw_star(x, y, size):
    """Draw a small star for decoration"""
    tu.penup()
    tu.goto(x, y)
    tu.pendown()
    tu.color(random.choice(colors))
    tu.begin_fill()
    for _ in range(5):
        tu.forward(size)
        tu.right(144)
    tu.end_fill()

def tree(i, thickness):
    if i < 10:
        # Add random flowers at branch tips
        if random.random() > 0.5:
            tu.color(random.choice(colors))
            tu.begin_fill()
            tu.circle(3)
            tu.end_fill()
        return
    else:
        # Random color for branches
        branch_color = random.choice(["brown", "sienna", "peru", "saddle brown"])
        tu.color(branch_color)
        
        # Vary the thickness based on branch size
        tu.pensize(thickness)
        
        # Draw the branch
        tu.forward(i)
        
        # Draw random leaves along the branch
        if i > 30:
            pos = tu.position()
            heading = tu.heading()
            tu.right(90)
            tu.penup()
            tu.forward(5)
            tu.pendown()
            tu.color(random.choice(colors))
            tu.dot(random.randint(2, 5))
            tu.penup()
            tu.goto(pos)
            tu.setheading(heading)
            tu.pendown()
        
        # Recursive branches
        tu.left(30)
        tree(3*i/4, thickness * 0.7)
        
        tu.right(60)
        tree(3*i/4, thickness * 0.7)
        
        tu.left(30)
        
        # Add some sparkle effect
        if i > 40:
            tu.color("yellow")
            tu.dot(2)
        
        tu.backward(i)

def draw_ground():
    """Draw a gradient-like ground"""
    tu.penup()
    tu.goto(-400, -200)
    tu.pendown()
    tu.color("dark green")
    tu.begin_fill()
    for x in range(-400, 401, 10):
        tu.goto(x, -200 + abs(x) * 0.1)
    tu.goto(400, -250)
    tu.goto(-400, -250)
    tu.goto(-400, -200)
    tu.end_fill()

def draw_stars():
    """Draw stars in the background"""
    tu.penup()
    for _ in range(50):
        x = random.randint(-400, 400)
        y = random.randint(0, 300)
        size = random.randint(1, 3)
        tu.goto(x, y)
        tu.dot(size, random.choice(["white", "yellow", "light yellow"]))

def draw_moon():
    """Draw a moon"""
    tu.penup()
    tu.goto(300, 250)
    tu.color("light yellow")
    tu.begin_fill()
    tu.circle(30)
    tu.end_fill()
    tu.color("yellow")
    tu.penup()
    tu.goto(290, 260)
    tu.dot(25, "white")

# Main drawing sequence
tu.speed(0)

# Draw background elements
draw_stars()
draw_moon()
draw_ground()

# Position the turtle for the tree
tu.penup()
tu.goto(0, -200)
tu.pendown()
tu.setheading(90)

# Draw the tree with initial thickness
tree(100, 10)

# Add some falling leaves animation
for _ in range(20):
    x = random.randint(-200, 200)
    y = random.randint(-100, 200)
    tu.penup()
    tu.goto(x, y)
    tu.pendown()
    tu.color(random.choice(colors))
    tu.begin_fill()
    tu.circle(random.randint(2, 5))
    tu.end_fill()
    
    # Make leaves fall a bit
    for _ in range(5):
        tu.clear()  # This is just for effect - in a real animation you'd need more code
        # But for simplicity, we'll just draw the leaves

# Add a title
tu.penup()
tu.goto(0, 300)
tu.color("white")
tu.write("🌳 Enchanted Tree 🌳", align="center", font=("Arial", 20, "bold"))

# Hide turtle and finish
tu.hideturtle()
turtle.done()