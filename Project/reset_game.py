# Import Turtle Graphics Module
import turtle
import random

WIDTH = 500
HEIGHT = 500
DELAY = 100  # (milliseconds)
FOOD_SIZE = 10

offsets = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}

#Optimised way to do the follwoing four functions on line #114-117
def bind_direction_keys():
    screen.onkey(lambda: set_snake_direction("up"), "Up")
    screen.onkey(lambda: set_snake_direction("left"), "Left")
    screen.onkey(lambda: set_snake_direction("down"), "Down")
    screen.onkey(lambda: set_snake_direction("right"), "Right")
  
# Optimised way to do functions in line #40-58  
def set_snake_direction(direction):
    global snake_direction
    if direction == "up":
        if snake_direction != "down":  # No self-collision by pressing the wrong key
            snake_direction = "up"
    elif direction == "left":
        if snake_direction != "right":  # No self-collision by pressing the wrong key
            snake_direction = "left"
    elif direction == "down":
        if snake_direction != "up":  # No self-collision by pressing the wrong key
            snake_direction = "down"
    elif direction == "right":
        if snake_direction != "left":  # No self-collision by pressing the wrong key
            snake_direction = "right"

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

def game_loop():
    stamper.clearstamps()

    new_head = snake[-1].copy()
    new_head[0] += offsets[snake_direction][0]
    new_head[1] += offsets[snake_direction][1]

    # Collision check
    if (new_head in snake or
        new_head[0] < -WIDTH/2 or new_head[0] > WIDTH/2 or
        new_head[1] < -HEIGHT/2 or new_head[1] > HEIGHT/2):
        reset()
        
    else:
        #Add new head to snake body
        snake.append(new_head)

        #Check food collision
        if not food_collision():
            snake.pop(0)

        #Draw snack for first time
        for segment in snake:
            stamper.goto(segment[0], segment[1])
            stamper.stamp()

        #Refresh Screen
        screen.title(f"Snake Game. Score: {score}")
        screen.update()
        
        turtle.ontimer(game_loop, DELAY)

def food_collision():
    global food_pos, score
    if get_distance(snake[-1], food_pos) < 20:
        score += 1
        food_pos = get_random_food_pos()
        food.goto(food_pos)
        return True  # FIXED
    return False

def get_random_food_pos():
    x = random.randint(int(-WIDTH/2 + FOOD_SIZE), int(WIDTH/2 - FOOD_SIZE))
    y = random.randint(int(-HEIGHT/2 + FOOD_SIZE), int(HEIGHT/2 - FOOD_SIZE))
    return (x, y)

def get_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    return ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5

def reset():
    global score, snake, snake_direction, food_pos
    score = 0
    snake = [[0, 0], [20, 0], [40, 0], [60, 0]]
    snake_direction = "up"
    food_pos = get_random_food_pos()
    food.goto(food_pos)
    game_loop()
    
# Screen setup
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Snake")
screen.bgcolor("pink")
screen.tracer(0)

# Controls
screen.listen()

# Now for lines #131-134, we simply replace them with bind_direction_keys()
screen.onkey(go_up, "Up")
screen.onkey(go_right, "Right")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")

# Snake drawer
stamper = turtle.Turtle()
stamper.shape("square")
stamper.penup()

# Food
food = turtle.Turtle()
food.shape("circle")
food.shapesize(FOOD_SIZE / 20)
food.penup()


# Start game
reset()

turtle.done()