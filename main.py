from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=500, height=400) #width = 500pixel, height = 400pixel
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle do you think will win? Enter a color: ") #adds a popup window

tim = Turtle(shape="turtle")

tim.penup()
tim.goto(x=-230, y=-100) #takes x coordinate and y coordinate amd moves turtle to that position

















screen.exitonclick()
