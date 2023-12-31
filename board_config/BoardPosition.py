from .Position import Positions

class BoardPosition:
    """
    Board position class is a representation of a 5x5 grid
    with an iterator that returns the valid neighboring positions
    used to distinguish self and opponent positions
    """

    def __init__(self):
        """
        Initializes positions
        """
        self._opponent_pos = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        self.pos = [[Positions(x, y) for x in range(0, 5)] for y in range(0, 5)]
        self._iter_center_x = 0  # Initialize _iter_center_x
        self._iter_center_y = 0  # Initialize _iter_center_y

    def __iter__(self):
        self._iter_index = 0
        return self

    def set_iter_center(self, x, y):
        self._iter_center_x = x
        self._iter_center_y = y

    def __next__(self):
        """Returns the valid neighboring positions"""
        if self._iter_index < len(self._opponent_pos):
            dx, dy = self._opponent_pos[self._iter_index]
            x = self._iter_center_x + dx
            y = self._iter_center_y + dy
            self._iter_index += 1
            if 0 <= x < 5 and 0 <= y < 5:
                return self.pos[x][y]
            else:
                return self.__next__()  # Recursively try the next index
        else:
            raise StopIteration
