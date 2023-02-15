from turtle import Turtle
# turtle heading info
# 0 - east
# 90 - north
# 180 - west
# 270 - south
class Snake:
    def __init__(self)->None:
        self.segments = []

        for i in range(3):
            segment = Turtle()
            if (i == 0):
                segment.shape("arrow")
                segment.color("white")
            else:
                segment.shape("square")
                segment.color("green")

            segment.penup()
            segment.setheading(0)
            segment.setx(-20 * i)
            self.segments.append(segment)

    def get_segments(self):
        return self.segments

    # start at the tail and work our way up the list
    # also need to account for direction
    def move(self, direction):
        # -1 cause lists start at 0
        # also -1 so we loop last to first
        for i in range(len(self.segments) - 1, 0, -1):
            # get postion of segment
            x = self.segments[i-1].xcor()
            y = self.segments[i-1].ycor()
            self.segments[i].goto(x, y)

        self.segments[0].setheading(direction)
        self.segments[0].forward(20)

    
    # we need to add the new segment to the end
    # also need to get the direction of the last segment
    # and set the direction of the new segment to that of the last
    # also need to offset by segment size (20px) on X or Y depending on direction
    def add_segment(self, direction):
        num_segments = len(self.segments) - 1

        segment = Turtle("square")
        segment.color("green")
        segment.penup()
        segment.setheading(direction)

        # EAST
        if (direction == 0):
            segment.setx(self.segments[num_segments].xcor() - 20)
            segment.sety(self.segments[num_segments].ycor())
        # SOUTH
        elif (direction == 270):
            segment.setx(self.segments[num_segments].xcor())
            segment.sety(self.segments[num_segments].ycor() + 20)
        # WEST
        elif (direction == 180):
            segment.setx(self.segments[num_segments].xcor() + 20)
            segment.sety(self.segments[num_segments].ycor())
        # NORTH
        elif (direction == 90):
            segment.setx(self.segments[num_segments].xcor())
            segment.sety(self.segments[num_segments].ycor() - 20)

        # ADD OUR NEW SEGMENT
        self.segments.append(segment)

    # dont forget to return the value...
    def check_collision(self, direction):
        did_collide = False

        for segment in self.segments[1:]:
            # EAST
            if (direction == 0):
                if (segment.distance(self.segments[0].xcor() + 30, self.segments[0].ycor()) <= 19):
                    did_collide = True
             # SOUTH
            elif (direction == 270):
                if (segment.distance(self.segments[0].xcor(), self.segments[0].ycor() - 30) <= 19):
                    did_collide = True
            # WEST
            elif (direction == 180):
                if (segment.distance(self.segments[0].xcor() - 30, self.segments[0].ycor()) <= 19):
                    did_collide = True
            # NORTH
            elif (direction == 90):
                if (segment.distance(self.segments[0].xcor(), self.segments[0].ycor() + 30) <= 19):
                    did_collide = True
        
        return did_collide