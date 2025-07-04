from turtle import Turtle


STARTING_POSITION = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT= 0




class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head  = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_Segment(position)

    def add_Segment(self,position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment )


    def extend(self):
        self.add_Segment(self.segments[-1].position())




    def move(self):
        for seg_num in range(len(self.segments) - 1,0,-1):
            x_cor = self.segments[seg_num - 1].xcor()
            y_cor = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x_cor,y_cor)
         
        self.head.forward(MOVE_DISTANCE)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)