import turtle
import random
from pygame import mixer

screen = turtle.Screen()
screen.title("Catch The Meteor")
screen.bgpic("uzay.gif")
screen.addshape("meteor.gif")
FONT = ("Arial", 20, "normal")

score = 0
game_over = False

turtle_list = []
score_turtle = turtle.Turtle()
countdown_turtle = turtle.Turtle()

def setup_score_turtle():
    score_turtle.hideturtle()
    score_turtle.color("red")
    score_turtle.penup()
    y = screen.window_height() / 2 * 0.9
    score_turtle.goto(0, y)
    score_turtle.write(arg="Score: 0", align="center", font=FONT)


grid_size = 10
def make_turtle(x, y):
    t = turtle.Turtle()
    t.penup()
    t.shape("meteor.gif")
    t.goto(x * grid_size, y * grid_size)
    t.hideturtle()

    def handle_click(x, y):
        global score
        score += 1
        score_turtle.clear()
        score_turtle.write(arg=f"Score: {score}", align="center", font=FONT)
        mixer.Sound("click.wav").play()


    t.onclick(handle_click)
    turtle_list.append(t)


x_coordinates = [-20, -10, 0, 10, 20]
y_coordinates = [20, 10, 0, -10]

def setup_turtles():
    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x, y)

def hide_turtles():
    for t in turtle_list:
        t.hideturtle()

def show_turtles_randomly():
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_turtles_randomly, 500)


def countdown(time):
    global game_over
    countdown_turtle.hideturtle()
    countdown_turtle.color("red")
    countdown_turtle.penup()
    y = screen.window_height() / 2 * 0.9 - 30
    countdown_turtle.goto(0, y)

    countdown_turtle.clear()
    if time > 0:
        countdown_turtle.write(arg=f"Time: {time}", align="center", font=FONT)
        screen.ontimer(lambda: countdown(time - 1), 1000)
    else:
        game_over = True
        hide_turtles()
        countdown_turtle.clear()
        countdown_turtle.write(arg="Game Over!", align="center", font=FONT)
        mixer.Sound("gameover.wav").play()


def start_game():
    mixer.init()
    turtle.tracer(0)
    setup_score_turtle()
    setup_turtles()
    hide_turtles()
    show_turtles_randomly()
    countdown(15)
    turtle.tracer(1)


start_game()
turtle.mainloop()
