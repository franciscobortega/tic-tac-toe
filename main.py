from turtle import Turtle, Screen


class Player:
    def __init__(self, piece):
        self.game_piece = piece
        # self.player_name = name


class Board:
    def __init__(self):
        # self.board = [[" ", " ", " "], [" ", "X", " "], ["X", "O", "O"]]
        # self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.board = [[" ", "X", " "], [" ", "X", "X"], ["O", " ", "X"]]

    def __str__(self):
        """Prints the board."""
        bottom_border = f"-{'-+' * 3}\n"
        row_1 = f"|{self.board[0][0]}|{self.board[0][1]}|{self.board[0][2]}|\n"
        row_2 = f"|{self.board[1][0]}|{self.board[1][1]}|{self.board[1][2]}|\n"
        row_3 = f"|{self.board[2][0]}|{self.board[2][1]}|{self.board[2][2]}|\n"
        return f"{row_1}{bottom_border}{row_2}{bottom_border}{row_3}{bottom_border}"

    def display(self):
        pass

    # def add_move(self, move):
    #     self.moves.append(move)
    def print_board(self):
        print(self.board)

    def make_move(self, player_piece):
        row_input = int(input("Which row would you like to place your piece in?: "))
        column_input = int(input("Which column would you like to place your piece in?: "))

        if self.is_not_available(row_input, column_input):
            self.make_move(player_piece)
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
        if self.board[row][column] != " ":
            print("\tThat position is already taken!")
            print("\tPlease make another selection.")
            return True
        return False

    def three_in_a_row(self, current_piece):
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


class Game:
    def __init__(self):
        self.board = Board()
        self.player_1 = Player("X")
        self.player_2 = Player("O")
        self.current_player = self.player_1.game_piece

    def print_board(self):
        print(self.board)

    def alternate_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"


game = Game()
board = Board()
game.print_board()

print(board.is_full())

game_not_over = True
while game_not_over:

    if board.is_full():
        game_not_over = False
        print("It's a draw!")
        continue

    print(f"Player {game.current_player}: ", end="")
    board.make_move(game.current_player)
    print(board.board)

    # check if 3 in a row
    if board.three_in_a_row(game.current_player):
        game_not_over = False
        print(f"{game.current_player} won!")
        continue

    game.alternate_player()
