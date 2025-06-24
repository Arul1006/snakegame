import time

from food import Food
from turtle import Turtle, Screen


screen = Screen()
# screen.setup(width=600, height=600)
# screen.bgcolor("black")
# screen.title("My Snake Game")
# screen.tracer(0)


# starting_positions = [(0, 0), (-5, 0), (-10, 0)]
# segments = []


food = Food()


# def left():
#     if self.segments[0].heading() != 0:
#         self.segments[0].setheading(180)
#
# def right():
#     if self.segments[0].heading() != 180:
#         self.segments[0].setheading(0)
#
# def up():
#     if self.segments[0].heading() != 270:
#         self.segments[0].setheading(90)
#
# def down():
#     if self.segments[0].heading() != 90:
#         self.segments[0].setheading(270)



# for position in starting_positions:
#     new_segment = Turtle("square")
#     new_segment.shapesize(stretch_wid=0.5, stretch_len=0.5)
#     new_segment.color("white")
#     new_segment.penup()
#     new_segment.goto(position)
#     segments.append(new_segment)

# screen.listen()
# screen.onkey(up, "Up")
# screen.onkey(down, "Down")
# screen.onkey(left, "Left")
# screen.onkey(right, "Right")
class Snake:
    def __init__(self):
        self.starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        self.segments = []
        for position in self.starting_positions:
            self.add_segment(position)

        # for position in self.starting_positions:
        #     self.new_segment = Turtle("square")
        #     self.new_segment.shapesize(stretch_wid=0.5, stretch_len=0.5)
        #     self.new_segment.color("white")
        #     self.new_segment.penup()
        #     self.new_segment.goto(position)
        #     self.segments.append(self.new_segment)

        def left():
            if self.segments[0].heading() != 0:
                self.segments[0].setheading(180)

        def right():
            if self.segments[0].heading() != 180:
                self.segments[0].setheading(0)

        def up():
            if self.segments[0].heading() != 270:
                self.segments[0].setheading(90)

        def down():
            if self.segments[0].heading() != 90:
                self.segments[0].setheading(270)

        screen.listen()
        screen.onkey(up, "Up")
        screen.onkey(down, "Down")
        screen.onkey(left, "Left")
        screen.onkey(right, "Right")

    def add_segment(self,coordinates):

        # for position in self.starting_positions:
        self.new_segment = Turtle("square")
        self.new_segment.shapesize(stretch_wid=1, stretch_len=1)
        self.new_segment.color("white")
        self.new_segment.penup()
        # self.new_segment.speed(9)
        self.new_segment.goto(coordinates)
        self.segments.append(self.new_segment)

    def game_over(self):
        pen = Turtle()
        pen.color("white")
        pen.penup()
        pen.hideturtle()
        pen.goto(0, 0)
        pen.write("GAME OVER", align="center", font=("Arial", 30, "normal"))

    def move(self):

        game_is_on = True
        while game_is_on:

            if (abs(self.segments[0].xcor()) >= 295 or abs(self.segments[0].ycor()) >= 295 ):
                self.game_over()
                game_is_on = False

            head = self.segments[0]
            for segment in self.segments[1:]:
                if head.distance(segment) < 10:
                    game_is_on = False
                    self.game_over()

            for seg in self.segments:
                time.sleep(0.1)
                screen.update()


                for seg_num in range(len(self.segments) - 1, 0, -1):
                    new_x = self.segments[seg_num - 1].xcor()
                    new_y = self.segments[seg_num - 1].ycor()
                    self.segments[seg_num].goto(new_x, new_y)

                self.segments[0].forward(20)
                # segments[0].left(90)

            if food.check_if_eaten(self.segments[0].xcor(), self.segments[0].ycor()) :
               self.add_segment((int(self.segments[seg_num - 3].xcor()), int(self.segments[seg_num - 3].ycor())))

            # score.score_count()
                # if (segments[0].xcor() == tim.xcor() and segments[0].ycor == tim.ycor()) :





