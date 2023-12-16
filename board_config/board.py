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
        self.white_height = 0
        self.blue_height = 0
        self.white_center = 0
        self.blue_center = 0
        self.white_distance = 0
        self.blue_distance = 0
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


    def is_valid_pos(self, worker):
        return 0 <= self._workers[worker].row < 5 and 0 <= self._workers[worker].column < 5 
        # TODO: also needs to check if other worker is not there

    def is_valid_direction(self, worker, direction):
        """
        Checks if moving in the specified direction is valid for the given worker.
        """
        if direction not in self._valid_directions:
            return False

        x = self._workers[worker].row + self._valid_directions[direction][0]
        y = self._workers[worker].column + self._valid_directions[direction][1]

        if (x < 0 or x >= 5 or y < 0 or y >= 5) or (self.empty_cell(self._positions.pos[x][y]) == False):
            return False
        print("emptuy cell valid direction", self.empty_cell(self._positions.pos[x][y]))
        return self.empty_cell(self._positions.pos[x][y])

    def is_valid_build_direction(self, worker, moved_direction, build_direction):
        """
        Checks if the build direction for the specified worker is valid
        """
        # move the worker
        prev_pos = self._workers[worker]
        prev_row, prev_col = prev_pos.row, prev_pos.column

        curr_row = prev_row + self._valid_directions[moved_direction][0]
        curr_col = prev_col + self._valid_directions[moved_direction][1]

        new_row = curr_row + self._valid_directions[build_direction][0]
        new_col = curr_row + self._valid_directions[build_direction][1]
        print("valid build empty cell", self.empty_cell(self._positions.pos[new_row][new_col]))
        # curr_pos.row = new_row
        # curr_pos.column = new_col
        if (new_row < 0 or new_row >= 5 or new_col < 0 or new_col >= 5):
            return False
        return self.empty_cell(self._positions.pos[new_row][new_col])

        
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
   
    def undo_build(self, worker, direction):
        row = self._workers[worker].row + self._valid_directions[direction][0]
        col = self._workers[worker].column + self._valid_directions[direction][-1]
        self._positions.pos[row][col]._set_height(-1)

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

    def calculate_height_score(self, position1, position2, work_type):
        cell = self._positions.pos[position1.row][position1.column]
        # print("cur cell height 1: ", cell.height)
        cell2 = self._positions.pos[position2.row][position2.column]
        # print("cur cell height 2: ", cell2.height)
        height_total = cell.height + cell2.height
        if work_type == "white":
            self.white_height = height_total
        else:
            self.blue_height = height_total
        # first = self.cells[position1.row][position1.column].building_level
        # print("pos1 cur height: ", first)
        # second = self.cells[position2.row][position2.column].building_level
        # print("pos2 cur height: ", second)
        # third = first + second
        # print("HIEHGT SCORE:", height_total)
    
    def calculate_center_score(self, position1, position2, work_type):

        first = self.center_values.get((position1.row, position1.column), 0)
        second = self.center_values.get((position2.row, position2.column), 0)
        third = first + second
        if work_type == "white":
            self.white_center = third
        else:
            self.blue_center = third
        # print("CENTER SCORE: ", third)
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
                height = self.calculate_height_score(position1, position2, "white")
                # print("Position A: ", position1, "Position B: ", position2)
                center = self.calculate_center_score(position1, position2, "white")
                distance = self.calculate_distance_score(position1, position2, position3, position4, "white")
                # self.score_all(height, center, distance)
                # print(position1, position2)
            elif worker == "Y" or worker == "Z":
                # position1 = self._workers["Y"]
                # position2 = self._workers["Z"]
                height = self.calculate_height_score(position3, position4, "blue")
                # print("Position Y: ", position3, "Position Z: ", position4)
                center = self.calculate_center_score(position3, position4, "blue")
                distance = self.calculate_distance_score(position3, position4, position1, position2, "blue")
                # self.score_all(height, center, distance)

                # print(position1, position2)
        else:
            # Handle the case where the position is out of bounds
            print("Cannot build in the specified direction, position is out of bounds.")


    def empty_cell(self, position):
        # is_empty = False 
        if position.height == 3:
            return False # NOT EMPTY
        # print("empty cell position:", type(position))
        # for worker in self._workers.keys():
        #     other = self._workers[worker]
        #     # if position.row == other.row and position.column == other.column:
        #     if position.check_occupatied(self._workers[worker]):
        #         return False
        # print(position)
        # return True
        print(position)
        curr_row = position.row
        curr_col = position.column
        
        if self.cells[curr_row][curr_col].worker is not None:
            print("NOT EMPTY:", curr_row, curr_col)
            return False
        else:
            return True

    def check_valid_move_AND_buid(self, worker):
        # go through steps of moving and building and if it works, true, else false
        can_build = False

        for direction in self._valid_directions.keys():
            if self.is_valid_direction(worker, direction):

                # if the position to build in is free, try building
                for pos in self._positions:
                    if self.empty_cell(pos) == True:
                        # print("imma builf here", self.empty_cell(pos))
                        can_build = True
        return can_build

# curr_pos = self._workers[worker]
    def calculate_distance_score(self, player_pos1, player_pos2, opp_pos1, opp_pos2, work_type):
        # Calculate minimum distance for each player worker to any opponent worker
        if work_type == "white":          
            min_distance_player_pos1 = min(
                self.manhattan_distance(player_pos1, opp_pos2),
                self.manhattan_distance(player_pos2, opp_pos2)
            )
            min_distance_player_pos2 = min(
                self.manhattan_distance(player_pos2, opp_pos1),
                self.manhattan_distance(player_pos1, opp_pos1)
            )

            distance_score = 8 - (min_distance_player_pos1 + min_distance_player_pos2)
            self.white_distance = distance_score
            print("WHITE DISTANCE: ", self.white_distance)
            return distance_score
        
        if work_type == "blue":
            min_distance_player_pos1 = min(
            self.manhattan_distance(player_pos2, opp_pos1),
            self.manhattan_distance(player_pos1, opp_pos1)
            )
            min_distance_player_pos2 = min(
                self.manhattan_distance(player_pos2, opp_pos2),
                self.manhattan_distance(player_pos1, opp_pos2)
            )
            distance_score = 8 - (min_distance_player_pos1 + min_distance_player_pos2)
            self.blue_distance = distance_score
            print("BLUE DISTANCE:", self.blue_distance)
            return distance_score
        # The distance score is 8 minus the sum of these minimum distances

    
    def manhattan_distance(self, pos1, pos2):
        return abs(pos1.row - pos2.row) + abs(pos1.column - pos2.column)
    # def score_all(self, height, center, distance):

    #     return (height, center, distance)

    def get_blue_scores(self):
        return self.blue_height, self.blue_center, self.blue_distance
    
    def get_white_scores(self):
        return self.white_height, self.white_center, self.white_distance


    # def calculate_distance_score(self, player_pos1, player_pos2, opp_pos1, opp_pos2):
    #     # Calculate minimum distance for each player worker to any opponent worker
        
    #     print("A row:", player_pos1.row, "A column: ", player_pos1.column)

    #     cell = self._positions.pos[player_pos1.column][player_pos1.row]
    #     # test = self._positions.pos[player_pos1.column][player_pos1.row]
    #     cell2 = self._positions.pos[player_pos2.column][player_pos2.row]
    #     cell3 = self._positions.pos[opp_pos1.column][opp_pos1.row]
    #     cell4 = self._positions.pos[opp_pos2.column][opp_pos2.row]

    #     print("cells pos in distance: ", cell, cell2, cell3, cell4)
    #     # print("trest", test)
        
    #     min_distance_player_pos1 = min(
    #         self.manhattan_distance(cell, cell3),
    #         self.manhattan_distance(cell, cell4)
    #     )
    #     min_distance_player_pos2 = min(
    #         self.manhattan_distance(cell2, cell3),
    #         self.manhattan_distance(cell2, cell4)
    #     )

    #     # The distance score is 8 minus the sum of these minimum distances
    #     distance_score = 8 - (min_distance_player_pos1 + min_distance_player_pos2)
    #     print("DISTANCE SCORE: ", distance_score)
    #     return distance_score

    # def manhattan_distance(self, pos1, pos2):
    #     return abs(pos1.row - pos2.row) + abs(pos1.column - pos2.column)