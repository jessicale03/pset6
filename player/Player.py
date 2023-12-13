class Player:
    """
    abstract class for human, AI, and random player to inherit from
    """
    def __init__(self, curr_player_index, board):
        self._board = board
        self._curr_player_index = curr_player_index # 0 or 1
        if (self._curr_player_index == 0):
            self._workers = ['A', 'B']
            self._type = 'white'
        else:
            self._color = 'blue'
            self._workers = ['Y', 'Z']

    
    def _get_type(self):
        return self._type
    
    def _get_workers(self):
        return self._workers
    
    def _get_curr_player(self):
        return self._curr_player
    
    def _has_won(self):
        for name in self._workers:
            if self._board.get_height(name) == 3:
                return True
            elif len(self.useable_workers()) == 0:
                return True
            return False 

    def useable_workers(self):
        # array of workers that still can move
        useable_workers = []
        for worker in self._workers:
            if self._board.check_valid_move_AND_buid(worker):
                useable_workers.append(worker)
        return useable_workers
