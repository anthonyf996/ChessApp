from BoardQuery import BoardQuery

class BoardQueryNoMovesLeft(BoardQuery):
  def __init__(self):
    super().__init__()
    self.default = True

  def shouldSkipPiece(self, subjectPiece, currPiece):
    if currPiece is None or subjectPiece is not None and currPiece.getColor() != subjectPiece.getColor():
      return True
    return False

  def query(self, board, subjectPos, currPos):
    for move in board.getAllMoves( currPos ):
      if not board.stillInCheckAfterMove( board.getPiece( subjectPos ), move ):
        return True
    return False
