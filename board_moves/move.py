class Move():
    """ Move class that executes a move """
    def __init__(self, worker, move_direction, build_direction:
        self._worker = worker
        self._m_dir = move_direction
        self._b_dir = build_direction
        self._direction_mapping = {
        'n': (-1, 0),
        'ne': (-1, 1),
        'e': (0, 1),
        'se': (1, 1),
        's': (1, 0),
        'sw': (1, -1),
        'w': (0, -1),
        'nw': (-1, -1)
        }
        self.reverse = {'nw': 'se', 'n': 's', 'ne': 'sw', 'w': 'e', 'e': 'w','sw': 'ne', 's': 'n', 'se': 'nw'}

    def execute_move(self, board):
        """Runs the required command"""
        board.move(self._worker, self._m_dir)
        if not self._b_dir == None:
            board.build(self._worker, self._b_dir)
