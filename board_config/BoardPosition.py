from .Position import Positions

class BoardPosition:
    """
    board position class is a representation of 5x5 grid
    with an iterator that returns the valid neighboring positions
    used to distinguish self and opponent pos
    """
    def __init__(self):
        """
        Initializes positions
        """
        self._opponent_pos = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
        self.pos = [[Positions(x, y) for x in range(0,5)] for y in range(0,5)]

    def __iter__(self):
        self._iter_idex = 0
        return self

    def set_iter_center(self, x, y):
        self._iter_center_x = x
        self._iter_center_y = y

    def __next__(self):
        """ returns the valid neighboring positions"""

        while self._curr_iter_idx < len(self._opponent_pos):
            x = self._iter_center_x + self._opponent_pos[self.iter_idex][0]
            y = self._iter_center_y + self._opponent_pos[self.iter_idex][1]
            self._iter_idex += 1
            if x >= 0 and x < 5 and y >= 0 and y < 5:
                return self.pos[x][y]
        raise StopIteration