import chess
import chess.svg

import ChatGPT as gpt


def main():
    while True:
        user_input = input("Input: ")
        if not start_game(user_input):
            talk_to_chatGPT(user_input)


def start_game(user_input):
    ui = user_input.lower().split(" ")
    conditions = ["start", "chess", "game", "play"]
    if len(list(set(ui).intersection(set(conditions)))) >= 2 and "chess" in ui:
        play_game()
        return True


def talk_to_chatGPT(user_input):
    print(gpt.chatGPTRequest(user_input))


def user_move(chess_board, move):
    while True:
        move_on_board = chess.Move.from_uci(move)
        if chess_board.is_legal(move_on_board):
            chess_board.push(move_on_board)
            print(chess_board)
            break
        else:
            print("Illegal move!")
            print("Move must be in UCI format i.e 'e2e4' ")
            print(chess_board)


def play_game():
    chess_board = chess.Board()
    print("Sure! Let's play a game.")
    print(chess_board)
    player = 1
    while True:
        move = input("Input: ")
        if "stop" in move or ("end" in move and "game" in move):
            break

        if chess_board.is_stalemate():
            print("The game tied")
            print(chess_board.outcome())
            break

        if chess_board.is_game_over():
            print("The game is over")
            print(chess_board.outcome())

        if player == 1:
            user_move(chess_board, move)

        else:
            # TODO: mudel siia
            print("here is computer move")


if __name__ == "__main__":
    main()
