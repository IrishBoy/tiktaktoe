import os
import random
from sys import platform as _platform
from game import GameSettings
from minmax import Minimax

x = 0
player_score = 0
computer_score = 0

print("\n============== AI Tic Tac Toe ===============\n")
print("\n")
print("HARD TO BEAT")
print(":(")


while True:

    board = GameSettings()

    if x == 0:
        minimax = Minimax()
        print("\n============== Round 1 ===============\n")
    else:
        print(f"\n============== Round {x + 1} ================\n")

    board.show_board()

    while not board.complete_board():
        player = "X"
        player_movee = input("\nNext Move: ")

        if player_movee.isdigit():
            player_move = int(player_movee) - 1
        else:
            print("\n -- Error :: Invalid Input , Game Terminated -- ")
            break

        if player_move not in board.available_moves():
            print("\n-- Error :: Invalid Move, Try Again -- ")
            continue

        board.make_move(player_move, player)
        print("\n======== You Played ========\n")
        board.show_board()

        print("\n======== I played ========\n")

        if board.complete_board():
            break

        player = board.set_enemy(player)
        computer_move = minimax.determine(board, player)
        board.make_move(computer_move, player)
        print("")
        board.show_board()

    print("")
    print("Winner : ", board.winner())

    x += 1

    if board.winner() == "X":
        player_score += 1
        print(f"Score : Player => {player_score}  AI => {computer_score}")
    elif board.winner() == "O":
        computer_score += 1
        print(f"Score : Player => {player_score}  AI => {computer_score}")
    else:
        print(f"Score : Player => {player_score}  AI => {computer_score}")

    print("\n")
    answer = input("\n Do you want to play again? (y/n) ")

    if answer == "n":
        print("\nThanks for playing, human..")
        print("\n\nFinal Score : \n\n")
        print(f"Player => {player_score}\nAI => {computer_score}")
        break
        os._exit(1)
    else:
        print("\n again:(..")
