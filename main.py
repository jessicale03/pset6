from Game import Santorini
import sys

def main():
    argv_params = [['human', 'heuristic', 'random'], ['human', 'heuristic', 'random'], ['on', 'off'], ['on', 'off']]

    parameters = ['human', 'human', 'off', 'off']

    for i in range(1, len(sys.argv)):
        if (sys.argv[i] not in argv_params[i-1]):
           sys.exit('Invalid command line argument: ' + sys.argv[i])

        parameters[i-1] = sys.argv[i]

    white_type = parameters[0]
    blue_type = parameters[1]

    game = Santorini(white_type, blue_type)
    print(game._board)

    # turn = 1
    # current_player = 'A'

    # while True:
    #     # Check for win condition at the start of the turn
    #     if board.has_won(board, current_player):
    #         board.print_board(turn, current_player)
    #         print(f"Player {current_player} wins!")
    #         break

    #     # board.print_board(turn, current_player)
    #     print(board)

    #     worker_symbol, from_row, from_col, to_row, to_col, build_row, build_col = get_player_move(board, current_player)

    #     board.move_worker(from_row, from_col, to_row, to_col)
    #     board.build(build_row, build_col)

    #     # Check for win condition after the move
    #     if has_won(board, current_player):
    #         board.print_board(turn, current_player)
    #         print(f"Player {current_player} wins!")
    #         break

    #     # Switch player for the next turn
    #     current_player = 'B' if current_player == 'A' else 'A'

    #     turn += 1


if __name__ == "__main__":
    main()