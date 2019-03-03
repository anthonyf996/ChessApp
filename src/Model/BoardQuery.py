# This class is a base class of a Template Method pattern for
# checking every piece in the board against a particular query.
class BoardQuery:
  def __init__(self):
    self.default = False

  def queryBoard(self, board, subjectPos):
    subjectPiece = board.getPiece( subjectPos )

    for y in range(0,board.getNumRows()):
      for x in range(0,board.getNumCols()):
        currPos = ( x, y )
        currPiece = board.getPiece( currPos )

        if self.shouldSkipPiece( subjectPiece, currPiece ):
          continue

        if self.query( board, subjectPos, currPos ):
          return not self.default

    return self.default

  def shouldSkipPiece(self, subjectPiece, currPiece):
    raise NotImplementedError

  def query(self, board, subjectPos, currPos):
    raise NotImplementedError
