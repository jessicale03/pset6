class Player:
    def __init__(self, curr_player, board):
        self._board = board
        self._curr_player = curr_player
        if (self._curr_player == 0):
            self._workers = ['A', 'B']
            self._color = 'white'
        else:
            self._color = 'blue'
            self._workers = ['Y', 'Z']

    
    def _get_colors(self):
        return self._color
    
    def _get_workers(self):
        return self._workers
    
    def _get_curr_player(self):
        return self._curr_player
    
    def _has_won(self):
        for name in self._workers:
            if self._board.get_height(name) == 3:
                return True
            return False 