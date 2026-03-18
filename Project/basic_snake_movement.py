#Import Turtle Graphics Module
import turtle

WIDTH = 500
HEIGHT = 500
DELAY = 400 # (miliseconds)

def move_snake():
    stamper.clearstamps()  # Removes all other stamps
    
    new_head = snake[-1].copy()
    new_head[0] += 20
    
    #Add the head to the snake body
    snake.append(new_head)
    snake.pop(0)
    
    #Draw snake for the first time
    for segment in snake:
        stamper.goto(segment[0], segment[1])
        stamper.stamp()
        
    # Render Screen
    screen.update()
    
    # Rinse and repeat
    turtle.ontimer(move_snake, DELAY)


#Create a window where we will do our drawing
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Snake")
screen.bgcolor("pink")
screen.tracer(0)

#Creat a turtle to do your bidding
stamper = turtle.Turtle()
stamper.shape("square")
stamper.penup()

#Snack Representation
snake = [[0, 0], [20, 0], [40, 0], [60, 0]]

#Draw snake for the first time
for segment in snake:
    stamper.goto(segment[0], segment[1])
    stamper.stamp()
    
#Set animation in motion
move_snake()


#Finidh nicely
turtle.done()