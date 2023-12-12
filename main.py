class Worker:
    def __init__(self, symbol):
        self.symbol = symbol

class Cell:
    def __init__(self):
        self.building_level = 0
        self.worker = None

class Board:
    def __init__(self, rows, cols):
        self.cells = [[Cell() for _ in range(cols)] for _ in range(rows)]
        self.initialize()

    def initialize(self):
        # Set up the starting configuration of the board
        self.cells[1][1].worker = Worker('Y')
        self.cells[1][3].worker = Worker('B')
        self.cells[3][1].worker = Worker('A')
        self.cells[3][3].worker = Worker('Z')

        # Set up the initial building levels
        self.cells[1][1].building_level = 0
        self.cells[1][2].building_level = 0
        self.cells[1][3].building_level = 0
        self.cells[1][4].building_level = 0
        self.cells[2][1].building_level = 0
        self.cells[2][2].building_level = 0
        self.cells[2][3].building_level = 0
        self.cells[2][4].building_level = 0
        self.cells[3][1].building_level = 0
        self.cells[3][2].building_level = 0
        self.cells[3][3].building_level = 0
        self.cells[3][4].building_level = 0
        self.cells[4][1].building_level = 0
        self.cells[4][2].building_level = 0
        self.cells[4][3].building_level = 0
        self.cells[4][4].building_level = 0

    def print_board(self, turn, current_player):
        print(f"Turn: {turn}, {current_player} (AB)")
        for row in range(len(self.cells)):
            print("+--+--+--+--+--+")
            for col in range(len(self.cells[0])):
                cell = self.cells[row][col]
                if cell.worker:
                    print(f"|{cell.building_level if cell.building_level > 0 else ' '}{cell.worker.symbol}", end="")
                else:
                    print(f"|{cell.building_level} ", end="")
            print("|")
        print("+--+--+--+--+--+")

    def find_worker(self, worker_symbol):
        for row in range(len(self.cells)):
            for col in range(len(self.cells[0])):
                if self.cells[row][col].worker and self.cells[row][col].worker.symbol == worker_symbol:
                    return row, col
        return None, None

    def is_valid_move(self, row, col):
        return 0 <= row < len(self.cells) and 0 <= col < len(self.cells[0]) and not self.cells[row][col].worker

    def move_worker(self, from_row, from_col, to_row, to_col):
        self.cells[to_row][to_col].worker = self.cells[from_row][from_col].worker
        self.cells[from_row][from_col].worker = None

    def build(self, row, col):
        self.cells[row][col].building_level += 1


def get_player_move(board, current_player):
    while True:
        try:
            worker_symbol = input("Select a worker to move (A, B, Y, Z): ").upper()
            direction = input("Select a direction to move (n, ne, e, se, s, sw, w, nw): ")
            build_direction = input("Select a direction to build (n, ne, e, se, s, sw, w, nw): ")

            # Convert directions to row and column changes
            direction_mapping = {
                'n': (-1, 0),
                'ne': (-1, 1),
                'e': (0, 1),
                'se': (1, 1),
                's': (1, 0),
                'sw': (1, -1),
                'w': (0, -1),
                'nw': (-1, -1)
            }

            from_row, from_col = board.find_worker(worker_symbol)
            to_row, to_col = from_row + direction_mapping[direction][0], from_col + direction_mapping[direction][1]
            build_row, build_col = to_row + direction_mapping[build_direction][0], to_col + direction_mapping[build_direction][1]

            # Check if the move is valid
            if not (0 <= to_row < len(board.cells) and 0 <= to_col < len(board.cells[0]) and board.is_valid_move(to_row, to_col)):
                print(f"Invalid move direction {direction}. Try again.")
                continue

            # Check if the build is valid
            if not (0 <= build_row < len(board.cells) and 0 <= build_col < len(board.cells[0])):
                print(f"Invalid build direction {build_direction}. Try again.")
                continue

            return worker_symbol, from_row, from_col, to_row, to_col, build_row, build_col

        except ValueError:
            print("Invalid input. Try again.")


def has_won(board, current_player):
    # Check if any worker of the current player is on a level 3 building
    for row in range(len(board.cells)):
        for col in range(len(board.cells[0])):
            cell = board.cells[row][col]
            if cell.worker and cell.worker.symbol == current_player and cell.building_level == 3:
                return True
    return False


def main():
    rows, cols = 5, 5
    board = Board(rows, cols)
    board.initialize()

    turn = 1
    current_player = 'A'

    while True:
        # Check for win condition at the start of the turn
        if has_won(board, current_player):
            board.print_board(turn, current_player)
            print(f"Player {current_player} wins!")
            break

        board.print_board(turn, current_player)

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


if __name__ == "__main__":
    main()