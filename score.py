from turtle import Turtle

class Score:
    def __init__(self):
        self.score = 0
        self.pen = Turtle()
        self.pen.color("white")
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(0, 260)  # Top center of the screen
        self.update_display()

    def update_display(self):
        self.pen.clear()
        self.pen.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def score_count(self):
        self.score += 1
        self.update_display()


