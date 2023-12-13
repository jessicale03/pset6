from .Game import Santorini

def main():
    rows, cols = 5, 5
    board = Board(rows, cols)

    turn = 1
    current_player = 'A'

    while True:
        # Check for win condition at the start of the turn
        if has_won(board, current_player):
            board.print_board(turn, current_player)
            print(f"Player {current_player} wins!")
            break

        # board.print_board(turn, current_player)
        print(board)

        worker_symbol, from_row, from_col, to_row, to_col, build_row, build_col = get_player_move(board, current_player)

        board.move_worker(from_row, from_col, to_row, to_col)
        board.build(build_row, build_col)

        # Check for win condition after the move
        if has_won(board, current_player):
            board.print_board(turn, current_player)
            print(f"Player {current_player} wins!")
            break

        # Switch player for the next turn
        current_player = 'B' if current_player == 'A' else 'A'

        turn += 1


if __name__ == "__main__":
    main()