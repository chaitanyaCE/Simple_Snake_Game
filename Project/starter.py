#Import Turtle Graphics Module
import turtle

WIDTH = 500
HEIGHT = 500
DELAY = 20 #miliseconds

def move_turtle():
    my_turtle.forward(1)
    my_turtle.right(1)
    screen.update()
    screen.ontimer(move_turtle, DELAY)
    

#Create a window where we will do our drawing
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Program Title")
screen.bgcolor("cyan")
screen.tracer(0) #truns off the automatic animation

#Creat a turtle to do your bidding
my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.color("red")

#Set animation in motion
move_turtle()

turtle.done()