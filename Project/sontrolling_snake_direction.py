#Import Turtle Graphics Module
import turtle

WIDTH = 500
HEIGHT = 500
DELAY = 400 # (miliseconds)

offsets = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}

def go_up():
    global snake_direction
    if snake_direction != "down":
        snake_direction = "up"
        
def go_right():
    global snake_direction
    if snake_direction != "left":
        snake_direction = "right"
        
def go_down():
    global snake_direction
    if snake_direction != "up":
        snake_direction = "down"
        
def go_left():
    global snake_direction
    if snake_direction != "right":
        snake_direction = "left"
        
        
        
def move_snake():
    stamper.clearstamps()  # Removes all other stamps
    
    new_head = snake[-1].copy()
    new_head[0] += offsets[snake_direction][0]
    new_head[1] += offsets[snake_direction][1]
    
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

#Event Handlers
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_right, "Right")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")

#Creat a turtle to do your bidding
stamper = turtle.Turtle()
stamper.shape("square")
stamper.penup()

#Snack Representation
snake = [[0, 0], [20, 0], [40, 0], [60, 0]]
snake_direction = "up"

#Draw snake for the first time
for segment in snake:
    stamper.goto(segment[0], segment[1])
    stamper.stamp()
    
#Set animation in motion
move_snake()

#Finidh nicely
turtle.done()