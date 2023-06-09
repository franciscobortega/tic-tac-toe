from turtle import Turtle


class Player:
    def __init__(self, piece):
        self.game_piece = piece
        self.turtle = Turtle()

    def draw_circle(self, x_coord, y_coord):
        """Draws the circle shape for the 'O' player"""
        self.turtle.penup()
        self.turtle.goto(x_coord, y_coord)
        self.turtle.dot(125, "white")
        self.turtle.dot(110, "black")

    def draw_cross(self, x_coord, y_coord):
        """Draws the cross shape for the 'X' player"""
        self.turtle.color("white")
        self.turtle.penup()
        self.turtle.goto(x_coord, y_coord)
        self.turtle.pensize(10)
        self.turtle.setheading(45)
        self.turtle.pendown()

        for _ in range(2):
            self.turtle.forward(60)
            self.turtle.backward(120)
            self.turtle.forward(60)
            self.turtle.right(90)

        self.turtle.penup()

    def draw_player_shape(self, current_player, x, y):
        """Calls the corresponding draw function for the current player"""
        if current_player == "X":
            self.draw_cross(x, y)
        else:
            self.draw_circle(x, y)
