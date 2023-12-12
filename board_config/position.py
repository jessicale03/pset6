class Positions:
    """
    base class for positions on the board
    """
    def __init__(self, row, column):
        self._row = row
        self._column = column
        self._height = height

    # private variables
    def _get_row(self):
        return self._row

    def _get_column(self):
        return self._column

    def _get_height(self):
        return self._height
    
    # assignment properities
    row = property(fget=_get_row, doc='row number')
    column = property(fget=_get_column, doc='column number')
    height = property(fget=_get_height, doc='height number')

    # format self string
    def __str__(self):
      return '(' + str(self._row) + ',' + str(self._column) + ') h:' + str(self._height)
   
   # checking if the position is already occupied
   def check_occupatied(self, position):
    if self.column == position.column and self.row == position.row:
         return True
    else:
        return False