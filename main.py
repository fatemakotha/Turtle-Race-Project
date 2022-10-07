from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=500, height=400) #width = 500pixel, height = 400pixel
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle do you think will win? Enter a color: ") #adds a popup window
colors = ["red", "orange", "blue", "green", "yellow", "purple"]
y_coordinate = [-70, -40, -10, 20, 50, 80]

for each_turtle in range(0, 6):

    tim = Turtle(shape="turtle")
    tim.color(colors[each_turtle])
    tim.penup()
    tim.goto(x=-230, y=-y_coordinate[each_turtle]) #takes x coordinate and y coordinate amd moves turtle to that position






# jim = Turtle(shape="turtle")
# jim.penup()
# jim.goto(x=-230, y=-70) #takes x coordinate and y coordinate amd moves turtle to that position
















screen.exitonclick()
