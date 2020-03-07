from BoardQuery import BoardQuery

class BoardQueryIsInDanger(BoardQuery):
  def __init__(self):
    super().__init__()
    self.default = False

  def shouldSkipPiece(self, subjectPiece, currPiece):
    if currPiece is None or subjectPiece is not None and currPiece.getColor() == subjectPiece.getColor():
      return True
    return False

  def query(self, board, subjectPos, currPos):
    for move in board.getEatMoves( currPos ):
      if subjectPos in move.getPosPair():
        return True
    return False
