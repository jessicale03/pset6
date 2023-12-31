class Player:
    """
    abstract class for human, AI, and random player to inherit from
    """
    def __init__(self, curr_player_index, board):
        self._board = board
        self._curr_player_index = curr_player_index # 0 or 1
        self._valid_directions = ['n', 'ne', 'e', 'se', 's', 'sw', 'w', 'nw']
        if (self._curr_player_index == 0):
            self._workers = ['A', 'B']
            self._type = 'white'
        else:
            self._type = 'blue'
            self._workers = ['Y', 'Z']

        # TODO: setter for curr_plauer???

    
    def _get_type(self):
        return self._type

    def _set_type(self, index):
        self._curr_player_index = index

    def _get_workers(self):
        return self._workers
    
    def _get_curr_player(self):
        return self._curr_player
    
    def _has_won(self, move):
        print("WE INSIDE HAS_WON")
        for name in self._workers:
            # height_again = self._board.get_height2(name, move)
            height_again = self._board.get_height(name)
            print("height rn of", name, ": ", height_again)
            if height_again == 3:
                return True
            elif len(self.useable_workers()) == 0:
                return True
            return False 
    # def _has_won(self):
    #     for name in self._workers:
    #         if name == 'A' or name == 'B':
    #         # Get the worker's current position
    #             print(name)
    #             worker_pos = self._board._workers[0]
    #         else:
    #             worker_pos = self._workers[1]
    #         # Check if the worker is standing on a level 3 building
    #         if self._board.cells[worker_pos.row][worker_pos.column].building_level == 3:
    #             return True

        # If none of the workers are standing on a level 3 building, return False
        return False

    def useable_workers(self):
        # array of workers that still can move
        useable_workers = []
        for worker in self._workers:
            if self._board.check_valid_move_AND_buid(worker):
                useable_workers.append(worker)
        return useable_workers

    def playable_moves(self, worker):
        playable_moves = []
        print(worker)
        for direction in self._valid_directions:
            # str(direction)
            if self._board.is_valid_direction(worker, direction):
                playable_moves.append(direction)
        return playable_moves

    def playable_build(self, worker, random_move):
        playable_moves = self.playable_moves(worker) # has valid moves
        playable_build = []
        for direction in playable_moves:
            # print(f'playable_build worker {worker}')
            if self._board.is_valid_build_direction(worker, random_move, direction):
                # print(f'playable_build direction array {playable_build}')
                playable_build.append(direction)
        # print(f'playable_build direction array {playable_build}')
        return playable_build

    # def buildable_directions(self, worker):
        # buildable_directions = []
        # for direction in self._valid_directions:
            # if self._board.is_valid_build_direction(worker, direction):
                # buildable_directions.append(direction)
        # return buildable_directions

