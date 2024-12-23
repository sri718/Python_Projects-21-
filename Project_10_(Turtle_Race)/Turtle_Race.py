import turtle
import time
import random

WID, HIG = 500, 500
COL = ['red','yellow','green','blue','black','purple','pink']

def get_racers():
    while True:
        racers = input("Enter the number of racers (2-7): ")
        if racers.isdigit():
            racers = int(racers)
            if 2 <= racers <= 7:
                return racers
            else:
                print("The number of racers should be between 2 and 10.")
        else:
            print("Please enter a valid number.")

def create_turtles(colours):
    turtles = []
    spacing = WID//(len(colours)+1)
    for i, colour in enumerate(colours):
        racer = turtle.Turtle()
        racer.color(colour)
        racer.shape('turtle')
        racer.left(90)                               # to make turtles face up.
        racer.penup()
        racer.setpos(-WID//2 + (i+1)*spacing, -HIG//2 + 20)
        racer.pendown()
        turtles.append(racer)
    return turtles

def race(colours):
    turtles = create_turtles(colours)
    while True:
        for racer in turtles:
            distance = random.randrange(1,21)
            racer.forward(distance)
            x,y = racer.pos()                        # to get the position of the racer
            if y >= HIG//2 - 10:
                return colours[turtles.index(racer)]
    
def init_turtle():
    screen = turtle.Screen()
    screen.setup(WID, HIG)
    screen.title("Turtle Racing!!!")

racers = get_racers()
init_turtle()
random.shuffle(COL)                                   # shuffle the list.
colours = COL[:racers]
#create_turtles(colours) inside race()
winner = race(colours)
print(f"Winner of the race is {winner.upper()}.")
turtle.done()                                        # to prevent (not responding) in turtle screen.
