from turtle import Turtle,Screen
import random

screen = Screen()
screen.setup(width = 500,height = 400)
user_bet = screen.textinput(title = "Make you bet",prompt = "Which turtle will win the race, Enter the colour:" )
colors = ["red","orange","green","yellow","blue","purple"]
y_position = [-70,-40,-10,20,50,80]
all_turtle =[]

for turtle_index in range(0,6):
    tim = Turtle(shape="turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x=-230,y=y_position[turtle_index])
    all_turtle.append(tim)



if user_bet:
    is_game_on = True

while is_game_on:

    for turtle in all_turtle:
        if turtle.xcor()>230:
            is_game_on = False
            if user_bet==turtle.pencolor():
                print(f"You guessed the turtle,It was : {turtle.pencolor()}")
            else:
                print(f"Better luck next time,It was : {turtle.pencolor()}")

        pace = random.randint(1,10)
        turtle.forward(pace)

screen.exitonclick()