from board_config.Board import Board, Worker, Cell
from board_moves.Move import Move
from player.Player import HumanPlayer

# def get_player_move(board, current_player):
    # valid_workers = {'A', 'B', 'Y', 'Z'}
    # valid_directions = {'n', 'ne', 'e', 'se', 's', 'sw', 'w', 'nw'}
# 
    # while True:
        # tr.y:
            # # worker_symbol = input("Select a worker to move (A, B, Y, Z): ").upper()
            # if worker_symbol not in valid_workers:
                # print("Not a valid worker.")
                # continue
# 
            # # direction = input("Select a direction to move (n, ne, e, se, s, sw, w, nw): ")
            # 
            # if direction not in valid_directions:
                # print("Not a valid direction.")
                # continue
# 
            # # build_direction = input("Select a direction to build (n, ne, e, se, s, sw, w, nw): ")
# 
            # if build_direction not in valid_directions:
                # print("Not a valid direction.")
                # continue
# 
# 
            # Convert directions to row and column changes
            # direction_mapping = {
                # 'n': (-1, 0),
                # 'ne': (-1, 1),
                # 'e': (0, 1),
                # 'se': (1, 1),
                # 's': (1, 0),
                # 'sw': (1, -1),
                # 'w': (0, -1),
                # 'nw': (-1, -1)
            # }
# 
            # from_row, from_col = board.find_worker(worker_symbol)
            # # to_row, to_col = from_row + direction_mapping[direction][0], from_col + direction_mapping[direction][1]
            # # build_row, build_col = to_row + direction_mapping[build_direction][0], to_col + direction_mapping[build_direction][1]
# 
            # Check if the move is valid
            # # if not (0 <= to_row < len(board.cells) and 0 <= to_col < len(board.cells[0]) and board.is_valid_move(to_row, to_col)):
                # print(f"Invalid move direction {direction}. Try again.")
                # continue
# 
            # Check if the build is valid
            # # if not (0 <= build_row < len(board.cells) and 0 <= build_col < len(board.cells[0])):
                # print(f"Invalid build direction {build_direction}. Try again.")
                # continue
# 
            # # return worker_symbol, from_row, from_col, to_row, to_col, build_row, build_col

        # except ValueError:
            # print("Invalid input. Try again.")


# def has_won(board, current_player):
    # Check if any worker of the current player is on a level 3 building
    # for row in range(len(board.cells)):
        # for col in range(len(board.cells[0])):
            # cell = board.cells[row][col]
            # # if cell.worker and cell.worker.symbol == current_player and cell.building_level == 3:
                # return True
    # return False
# 

def main():
    rows, cols = 5, 5
    board = Board(rows, cols)
    # board.initialize()

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