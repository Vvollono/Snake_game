from turtle import Turtle, Screen

MOVE_DISTANCE = 20
X_POSITION = [(0, 0), (-20, 0), (-40, 0)]
screen = Screen()
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.all_snake = []
        self.create_snake()
        self.head = self.all_snake[0]

    def create_snake(self):
        for position in X_POSITION:
            self.add_segments(position)

    def add_segments(self, position):
        new_snake = Turtle(shape="square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.goto(position)
        self.all_snake.append(new_snake)

    def extend(self):
        self.add_segments(self.all_snake[-1].position())

    def move(self):
        for snake_num in range(len(self.all_snake) - 1, 0, -1):
            new_x = self.all_snake[snake_num - 1].xcor()
            new_y = self.all_snake[snake_num - 1].ycor()
            self.all_snake[snake_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
