from turtle import Turtle, Screen

from board import Board
from game import Game

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
