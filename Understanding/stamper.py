#Import Turtle Graphics Module
import turtle

WIDTH = 500
HEIGHT = 500

#Create a window where we will do our drawing
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Stamper")
screen.bgcolor("cyan")

#Creat a turtle to do your bidding
stamper = turtle.Turtle()
stamper.shape("square")
stamper.color("red")
stamper.shapesize(50 / 20)
stamper.stamp()
stamper.penup()
stamper.shapesize(10 / 20)
stamper.goto(100, 100)
stamper.stamp()

turtle.done()