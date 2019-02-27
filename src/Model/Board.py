from GetSimpleMovement import GetSimpleMovement
from GetEatMovement import GetEatMovement

class Board:
  def __init__(self, numRows, numCols):
    self.numRows = numRows
    self.numCols = numCols
    self.board = self.initBoard()

  def initBoard(self):
    board = []
    for y in range(0, self.numRows):
      row = []
      for x in range(0, self.numCols):
        row.append( None )
      board.append( row )

    return board

  def addPiece(self, pos, piece):
    x, y = pos
    self.board[ y ][ x ] = piece

  def removePiece(self, pos):
    x, y = pos
    self.board[ y ][ x ] = None

  def getPiece(self, pos):
    x, y = pos
    return self.board[ y ][ x ]

  def isValidMove(self, pos):
    x, y = pos
    if 0 <= y < self.numRows and 0 <= x < self.numCols:
      return True

  def isCollision(self, pos):
    return self.getPiece( pos ) != None

  def isOpponentPiece(self, currPiece, otherPiece):
    return currPiece.getColor() != otherPiece.getColor()

  def getMoves(self, pos):
    return GetSimpleMovement().getMoves( self, pos )

  def getEatMoves(self, pos):
    return GetEatMovement().getMoves( self, pos )

  def move(self, move):
    """
    startPos, endPos = move.getPosPair()
    self.addPiece( endPos, self.getPiece( startPos ) )
    self.removePiece( startPos )
    self.getPiece( endPos ).setHasMoved()
    """
    move.perform( self )

  def undo(self, move):
    move.undo( self )
