from turtle import Turtle


class Board:
    def __init__(self):
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

        # Draws horizontal and vertical lines for game
        self.turtle = Turtle()
        self.turtle.speed("fastest")
        self.draw_y(-100)
        self.draw_y(100)
        self.draw_x(-100)
        self.draw_x(100)

        self.current_player = ""

    def draw_y(self, x_cor):
        """Draws vertical lines of tic-tac-toe board starting from the provided x coordinate"""
        self.turtle.penup()
        self.turtle.color("white")
        self.turtle.hideturtle()
        self.turtle.setpos(x_cor, -300)
        self.turtle.setheading(90)
        self.turtle.pendown()
        self.turtle.forward(600)

    def draw_x(self, y_cor):
        """Draws horizontal lines of tic-tac-toe board starting from the provided y coordinate"""
        self.turtle.penup()
        self.turtle.color("white")
        self.turtle.hideturtle()
        self.turtle.setpos(-300, y_cor)
        self.turtle.setheading(0)
        self.turtle.pendown()
        self.turtle.forward(600)

    def display(self):
        """Displays the current board in the console, taken from exercise for debugging"""
        bottom_border = f"-{'-+' * 3}\n"
        row_1 = f"|{self.board[0][0]}|{self.board[0][1]}|{self.board[0][2]}|\n"
        row_2 = f"|{self.board[1][0]}|{self.board[1][1]}|{self.board[1][2]}|\n"
        row_3 = f"|{self.board[2][0]}|{self.board[2][1]}|{self.board[2][2]}|\n"
        return f"{row_3}{bottom_border}{row_2}{bottom_border}{row_1}{bottom_border}"

    def make_move(self, player_piece, row_input, column_input):
        """Appends current player's move to 2D array"""

        # Checks if current square has already been occupied
        # recursively calls itself until an empty square is clicked
        if self.is_not_available(row_input, column_input):
            self.make_move(player_piece, row_input, column_input)
        else:
            self.board[row_input][column_input] = player_piece

    def is_full(self):
        """Returns true if board is full, false if otherwise"""
        for row in self.board:
            for element in row:
                if element == " ":
                    return False
        return True

    def is_not_available(self, row, column):
        """Returns true if board square is not empty, false if otherwise"""
        if self.board[row][column] != " ":
            print("\tThat position is already taken!")
            print("\tPlease make another selection.")
            return True
        return False

    def three_in_a_row(self, current_piece):
        """Returns true if 3 squares in a row, column, or diagonal have the same value, false if otherwise"""
        self.current_player = current_piece

        # three in a row
        for row in self.board:
            if all(element == current_piece for element in row):
                return True

        # three in a column
        for column in range(len(self.board[0])):
            if all(row[column] == current_piece for row in self.board):
                return True

        # three in a diagonal
        left_diagonal = []
        right_diagonal = []
        for element in range(len(self.board)):
            left_diagonal.append(self.board[element][element])
            right_diagonal.append(self.board[element][len(self.board) - element - 1])

        if all(element == current_piece for element in left_diagonal) or all(
                element == current_piece for element in right_diagonal):
            return True

        # no three in a row found
        return False

    def game_over(self):
        """Displays winning player"""

        self.turtle.hideturtle()
        self.turtle.penup()

        # Draw rectangle for message
        self.turtle.goto(-200, -100)
        self.turtle.pendown()
        self.turtle.begin_fill()
        self.turtle.color("black")
        self.turtle.forward(400)
        self.turtle.left(90)
        self.turtle.forward(200)
        self.turtle.left(90)
        self.turtle.forward(400)
        self.turtle.left(90)
        self.turtle.forward(200)
        self.turtle.left(90)
        self.turtle.end_fill()

        # Draw message
        self.turtle.penup()
        self.turtle.home()
        self.turtle.color("white")
        if self.is_full():
            self.turtle.write("It's a Draw!", align="center", font=("Courier", 20, "normal"))
        else:
            self.turtle.write(f"Player {self.current_player} won!", align="center", font=("Courier", 20, "normal"))
