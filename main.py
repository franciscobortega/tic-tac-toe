from turtle import Screen
from board import Board
from game import Game
from player import Player

# Initialize screen
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Tic Tac Toe")
screen.bgcolor("black")
screen.tracer(0)

# initial class instances, 'X' player always goes first
player = Player("X")
board = Board()
game = Game()

screen.update()
screen.listen()


def next_move(x, y):
    # calculates values to be added to 2D matrix
    row = int((y + 300) // 200)
    col = int((x + 300) // 200)

    if not board.is_not_available(row, col):
        # coordinates for center of square that was clicked
        x_coord = col * 200 - 200
        y_coord = row * 200 - 200

        # Validate and append player move to 2D matrix and display move on GUI
        board.make_move(game.current_player, row, col)
        player.draw_player_shape(game.current_player, x_coord, y_coord)
        print(board.display())

        # Determine if game has ended with winner or a draw
        if board.three_in_a_row(game.current_player):
            print(f"Player {game.current_player} won!")
            board.game_over()
            screen.update()
            screen.exitonclick()
        elif board.is_full():
            print("It's a draw!")
            board.game_over()
            screen.exitonclick()

        game.alternate_player()


screen.onclick(next_move)
screen.mainloop()
