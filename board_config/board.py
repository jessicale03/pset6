from .BoardPosition import BoardPosition

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

        self._worker_names = [['A', 'B'], ['Y', 'Z']]
        self._workers = {}
        self._workers['A'] = self._positions.pos[1][3]
        self._workers['B'] = self._positions.pos[3][1]
        self._workers['Y'] = self._positions.pos[1][1]
        self._workers['Z'] = self._positions.pos[3][3]

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

    def is_valid_direction(self, worker, direction):
        x = self._workers[worker].row + self._valid_directions[direction][0]
        y = self._workers[worker].column + self._valid_directions[direction][1]
        if x < 0 or x >= 5 or y < 0 or y >= 5:
            return False
        elif not self.empty_cell(self._positions.pos[x][y]):
            return False
        else:
            return True

    # def is_valid_build_direction(self, worker, direction):

       
    # def move_worker(self, from_row, from_col, to_row, to_col):
        # # self.cells[to_row][to_col].worker = self.cells[from_row][from_col].worker
        # self.cells[from_row][from_col].worker = None

    # def valid_move(self, worker, direction, row):
        # check if the move is within the row and column limits

    # def valid_moveable_workers(self)
    
    def move(self, worker, direction):
      """
      Moves the specified worker
      """
      self._workers[worker] = self._positions.pos[self._workers[worker].row + self._valid_directions[direction][0]][self._workers[worker].column + self._valid_directions[direction][1]]


    def build(self, worker, direction):
        self._positions.pos_arr[self._workers[worker].row + self._direction_dict[direction][0]][self._workers[worker].column + self._direction_dict[direction][1]].height += 1
   
    def undo_build():
        pass

    def undo_move():
        pass

    def get_height(self, worker):
        return self._workers[worker].height

    # def build(self, worker, direction):
        # self.cells[row][col].building_level += 1
        # # # self._positions.pos[self._workers[worker].row + self._valid_directions[direction][0]][self._workers[worker].column+ self._valid_directions[direction][1]].height += 1
    def build(self, worker, direction):
        row = self._workers[worker].row + self._valid_directions[direction][0]
        column = self._workers[worker].column + self._valid_directions[direction][1]

        # Check if the position is within bounds
        if 0 <= row < 5 and 0 <= column < 5:
            self._positions.pos[row][column]._set_height(1)
            # print(self._positions.pos[row][column].height)
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
