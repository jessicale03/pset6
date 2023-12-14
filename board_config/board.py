from .BoardPosition import BoardPosition
from .Position import Positions
from player.Player import Player

class Worker:
    def __init__(self, symbol):
        self.symbol = symbol

class Cell:
    def __init__(self):
        self.building_level = 0
        self.worker = None

class Board:
    def __init__(self):
        self.cells = [[Cell() for _ in range(5)] for _ in range(5)]
        # self.initialize()
        self._positions = BoardPosition()
        self.center_values = {(2, 2): 2, (1, 1): 1, (1, 2): 1, (1, 3): 1, (2, 1): 1, (2, 3): 1, (3, 1): 1, (3, 2): 1, (3, 3): 1}

        self._worker_names = [['A', 'B'], ['Y', 'Z']]
        # self._workers = {}
        # self._workers['A'] = self._positions.pos[1][3]
        # self._workers['B'] = self._positions.pos[3][1]
        # self._workers['Y'] = self._positions.pos[1][1]
        # self._workers['Z'] = self._positions.pos[3][3]
        #Positions(row, column)
        self._workers = {
            'A': Positions(3, 1),  # Starting position for worker 'A'
            'B': Positions(1, 3),  # Starting position for worker 'B'
            'Y': Positions(1, 1),
            'Z': Positions(3, 3)
        }

        self._iter_idex = None
        self._iter_center_x = 0
        self._iter_center_y = 0

        self._valid_directions = {'nw': [-1,-1], 'n': [-1,0], 'ne': [-1,1], 'w': [0,-1], 'e': [0,1], 'sw': [1,-1], 's': [1,0], 'se': [1,1]}

    def __str__(self):
        board_str_lst = []
        for row in range(0, 5):
            board_str_lst.append('+--+--+--+--+--+\n')
            for column in range(0, 5):
                board_str_lst.append('|')
    
                cell = self._positions.pos[row][column]
    
                # Append the building height with a space before it
                board_str_lst.append(f"{cell.height}")
    
                has_worker = False
                for p in range(0, 2):
                    for w in range(0, 2):
                        worker_name = self._worker_names[p][w]
                        if self._workers[worker_name].row == row and self._workers  [worker_name].column == column:
                            # Append the worker name with a space before it
                            board_str_lst.append(f"{worker_name}")
                            has_worker = True
                if not has_worker:
                    board_str_lst.append(' ')
            board_str_lst.append('| ')
                
            board_str_lst.append('\n')
        board_str_lst.append('+--+--+--+--+--+\n')
        return ''.join(board_str_lst)

    # def find_worker(self, worker_symbol):
        # for row in range(len(self.cells)):
            # for col in range(len(self.cells[0])):
                # # if self.cells[row][col].worker and self.cells[row][col].worker.symbol == worker_symbol:
                    # return row, col
        # return None, None

    def is_valid_pos(self, worker):
        return 0 <= self._workers[worker].row < 5 and 0 <= self._workers[worker].column < 5 
        # TODO: also needs to check if other worker is not there

    # def is_valid_direction(self, worker, direction):
    #     x = self._workers[worker].row + self._valid_directions[direction][0]
    #     y = self._workers[worker].column + self._valid_directions[direction][1]
    #     if x < 0 or x >= 5 or y < 0 or y >= 5:
    #         return False
    #     elif not self.empty_cell(self._positions.pos[x][y]):
    #         return False
    #     else:
    #         return True

    def is_valid_direction(self, worker, direction):
        """
        Checks if moving in the specified direction is valid for the given worker.
        """
        # Current position of the worker
        curr_pos = self._workers[worker]
        curr_row, curr_col = curr_pos.row, curr_pos.column

        # Calculate the new position
        new_row = curr_row + self._valid_directions[direction][0]
        new_col = curr_col + self._valid_directions[direction][1]

        # Check if the new position is within board boundaries
        if not (0 <= new_row < 5 and 0 <= new_col < 5):
            return False

        # Check if the target cell is empty (no worker present and not at max height)
        target_cell = self.cells[new_row][new_col]
        if target_cell.worker is not None or target_cell.building_level == 4:
            return False

        # Additional game rules can be checked here (e.g., height difference)

        return True

    # def is_valid_build_direction(self, worker, direction):

       
    # def move_worker(self, from_row, from_col, to_row, to_col):
        # # self.cells[to_row][to_col].worker = self.cells[from_row][from_col].worker
        # self.cells[from_row][from_col].worker = None

    # def valid_move(self, worker, direction, row):
        # check if the move is within the row and column limits

    # def valid_moveable_workers(self)
    
    # def move(self, worker, direction):
    #   """
    #   Moves the specified worker
    #   """
    #   self._workers[worker] = self._positions.pos[self._workers[worker].row + self._valid_directions[direction][0]][self._workers[worker].column + self._valid_directions[direction][1]]
    # def move(self, worker, direction):
    #     """
    #     Moves the specified worker.
    #     """
    #     # Current position
    #     curr_row = self._workers[worker].row
    #     curr_col = self._workers[worker].column
    #     # print("current row: ", curr_row, "current col: ", curr_col)

    #     # Calculate new position
    #     new_row = curr_row + self._valid_directions[direction][0]
    #     new_col = curr_col + self._valid_directions[direction][1]
    #     print("new row: ", new_row, "new column: ", new_col)

    #     # Move worker on the board
    #     worker_move = self._positions.pos[curr_row][curr_col].worker 
    #     self._positions.pos[new_row][new_col].worker = worker_move
    #     self._positions.pos[curr_row][curr_col].worker = None  # Remove worker from current cell
    #     # self._positions.pos[new_row][new_col].worker = worker  # Place worker in new cell
        
    #     # Update worker's position in _workers
    #     self._workers[worker] = self._positions.pos[new_row][new_col]
    def move(self, worker, direction):
        """
        Moves the specified worker.
        """
        # Current position
        curr_pos = self._workers[worker]
        curr_row, curr_col = curr_pos.row, curr_pos.column

        # Calculate new position
        new_row = curr_row + self._valid_directions[direction][0]
        new_col = curr_col + self._valid_directions[direction][1]

        # Check for valid move within board boundaries
        if 0 <= new_row < 5 and 0 <= new_col < 5:
            # Update worker's position in _workers
            
            curr_pos.row = new_row
            curr_pos.column = new_col

            # Update the board cells
            self.cells[curr_row][curr_col].worker = None  # Remove worker from current cell
            self.cells[new_row][new_col].worker = worker  # Place worker in new cell
            # position_rn = self.cells[new_row][new_col]
            # position_rn = self._positions.pos[new_row][new_col]
            # worker2 = "A"
            # position_other = self._positions.pos[0]
            # position_rn = self._workers[worker]
            # position_other = self._workers["A"]
            # row, col, height = self.parse_position_string(position_rn)
            # print ("current position of", worker, "worker: ", position_rn.row)
            # print ("current position of", worker2, "worker: ", position_other)
        else:
            print("Invalid move. Outside of board boundaries.")
    def parse_position_string(self, position_str):
        # Extract the numerical parts of the string
        parts = position_str.strip("()").split(" ")
        row_col = parts[0].split(",")
        row = int(row_col[0])
        col = int(row_col[1])
        height = int(parts[1].split(":")[1])

        return row, col, height
    # def build(self, worker, direction):
    #     self._positions.pos_arr[self._workers[worker].row + self._direction_dict[direction][0]][self._workers[worker].column + self._direction_dict[direction][1]].height += 1
    # def build(self, worker, direction):
    #     """
    #     Builds on the specified direction from the worker's position.
    #     """
    #     # Worker's current position
    #     print("directions: ", direction)
    #     curr_row = self._workers[worker].row
    #     curr_col = self._workers[worker].column

    #     # Calculate building position
    #     build_row = curr_row + self._valid_directions[direction][0]
    #     build_col = curr_col + self._valid_directions[direction][1]

    #     # Increment building height
    #     print("previous height: ", self._positions.pos[build_row][build_col].height)
    #     self._positions.pos[build_row][build_col].height += 1
   
    def undo_build():
        pass

    def undo_move():
        pass

    # def get_height(self, worker):
        # return self._workers[worker].height
        # return self._workers[worker]._get_height()
        return self._positions.pos[row][column]._get_height()

    def get_height(self, worker):
        row = self._workers[worker].row #+ self._valid_directions[direction][0]
        column = self._workers[worker].column #+ self._valid_directions[direction][1]
        return self._positions.pos[row][column]._get_height()
    # def build(self, worker, direction):
        # self.cells[row][col].building_level += 1
        # # # self._positions.pos[self._workers[worker].row + self._valid_directions[direction][0]][self._workers[worker].column+ self._valid_directions[direction][1]].height += 1
    
    def has_won(self, worker):
        row = self._workers[worker].row 
        column = self._workers[worker].column 
        height = self._positions.pos[row][column]._get_height()
        if height == 3:
            return True
    def calculate_height_score(self, position1, position2):
        first = self.cells[position1.row][position1.column].building_level
        second = self.cells[position2.row][position2.column].building_level
        third = first + second
        print("HIEHGT SCORE:", third)
    
    def calculate_center_score(self, position1, position2):
        first = self.center_values.get((position1.row, position1.column), 0)
        second = self.center_values.get((position2.row, position2.column), 0)
        third = first + second
        print("CENTER SCORE: ", third)
        # return sum(self.center_values.get((pos.row, pos.column), 0) for pos in positions)

        # return sum(self.cells[pos.row][pos.column].building_level for pos in positions)
    def build(self, worker, direction):
        # print("directions: ", direction)
        # print("This is cur worker: ", worker)
        row = self._workers[worker].row + self._valid_directions[direction][0]
        column = self._workers[worker].column + self._valid_directions[direction][1]

        # Check if the position is within bounds
        if 0 <= row < 5 and 0 <= column < 5:
            self._positions.pos[row][column]._set_height(1)
            self._workers[worker]._set_height(1)
            # current_positions = layer.get_worker_positions()
            # print("current pos: ", current_positions)
            # if self._positions.pos[row][column]._get_height() == 3:
            #     return True

            # print(f'build function height: {self._positions.pos[row][column]._get_height()}')
            # print(self._positions.pos[row][column].height)
            position1 = self._workers["A"]
            position2 = self._workers["B"]
            position3 = self._workers["Y"]
            position4 = self._workers["Z"]
            if worker == "A" or worker == "B":
                # position1 = self._workers["A"]
                # position2 = self._workers["B"]
                self.calculate_height_score(position1, position2)
                self.calculate_center_score(position1, position2)
                self.calculate_distance_score(position1, position2, position3, position4)
                # print(position1, position2)
            elif worker == "Y" or worker == "Z":
                # position1 = self._workers["Y"]
                # position2 = self._workers["Z"]
                self.calculate_height_score(position3, position4)
                self.calculate_center_score(position3, position4)
                self.calculate_distance_score(position3, position4, position1, position2)
                # print(position1, position2)
        else:
            # Handle the case where the position is out of bounds
            print("Cannot build in the specified direction, position is out of bounds.")

   
#    def undo_build_from_worker(self, worker_name, direction):
        # pass

    def empty_cell(self, position):
        is_empty = False 
        if position.height == 4:
            return is_empty
        
        for worker in self._workers.keys():
            other = self._workers[worker]
            if position.row == other.row and position.column == other.column:
                return is_empty

        return True

    def check_valid_move_AND_buid(self, worker):
        # go through steps of moving and building and if it works, true, else false
        can_build = False

        for direction in self._valid_directions.keys():
            if self.is_valid_direction(worker, direction):
                # self._workers[worker] = self._positions.pos[self._workers[worker].r + self._valid_directions[m_dir][0]][self._workers[worker].c + self._valid_directions[m_dir][1]]
                # # self._positions.iter_center(self._workers[worker].row, self._workers[worker].column)

                # if the position to build in is free, try building
                for pos in self._positions:
                    if self.empty_cell(pos):
                        # self._workers[worker] = self._positions.pos[self._workers[worker].r - self._direction_dict[m_dir][0]][self._workers[worker].c - self._valid_directions[mo_dir][1]]
                        can_build = True
        return can_build

# curr_pos = self._workers[worker]




    def calculate_distance_score(self, player_pos1, player_pos2, opp_pos1, opp_pos2):
        # Calculate minimum distance for each player worker to any opponent worker
        min_distance_player_pos1 = min(
            self.manhattan_distance(player_pos1, opp_pos1),
            self.manhattan_distance(player_pos1, opp_pos2)
        )
        min_distance_player_pos2 = min(
            self.manhattan_distance(player_pos2, opp_pos1),
            self.manhattan_distance(player_pos2, opp_pos2)
        )

        # The distance score is 8 minus the sum of these minimum distances
        distance_score = 8 - (min_distance_player_pos1 + min_distance_player_pos2)
        print("DISTANCE SCORE: ", distance_score)
        return distance_score

    def manhattan_distance(self, pos1, pos2):
        return abs(pos1.row - pos2.row) + abs(pos1.column - pos2.column)