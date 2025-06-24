
from turtle import Turtle
import random
from score import Score

# x = range(-300,301)
# y = range(-300,301)

# tim = Turtle()
# tim.hideturtle()
# tim.penup()

# tim.goto(random.choice(x), random.choice(y))
# tim.dot(10, "blue")

score = Score()


class Food:
    def __init__(self):
        self.turtle = Turtle()
        self.turtle.penup()
        self.turtle.hideturtle()
        self.place_food()

    def place_food(self):
        grid_x = random.randint(-6, 6) * 40  # -280 to +280 in steps of 20
        grid_y = random.randint(-6, 6) * 40
        self.turtle.goto(grid_x, grid_y)
        self.turtle.dot(15, "red")

        # random_x = random.randint(-300, 300)
        # random_y = random.randint(-300, 300)
        # self.turtle.goto(random_x, random_y)
        # self.turtle.dot(15, "blue")

    # def new_food(self, xcor, ycor):
    #
    #     # if (tim.xcor() == xcor and tim.ycor() == ycor):
    #     #     tim.dot(10,"black")
    #     if tim.distance(xcor, ycor) < 7:
    #         tim.dot(10, "black")  # Visually mark it "eaten"

    def check_if_eaten(self, xcor, ycor):
        if self.turtle.distance(xcor, ycor) < 40:
            self.turtle.dot(20, "black")  # optional visual
            self.place_food()  # move to new location
            score.score_count()

            return True
        else:
            return False