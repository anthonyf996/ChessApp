from BoardQuery import BoardQuery

class BoardQueryIsProtected(BoardQuery):
  def __init__(self):
    super().__init__()
    self.default = False

  def shouldSkipPiece(self, subjectPiece, currPiece):
    if currPiece is None or currPiece.getColor() != subjectPiece.getColor():
      return True
    return False

  def query(self, board, subjectPos, currPos):
    for move in board.getCollisionMoves( currPos ):
      if subjectPos == move:
        return True
    return False
