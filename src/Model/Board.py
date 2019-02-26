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
      return self.getPiece( pos ) == None

  def getMoves(self, pos):
    moves = set()

    piece = self.getPiece( pos )
    currX, currY = pos

    movementVectors = piece.getMovementVectors().union( piece.getExtraMoves() )

    for vec in movementVectors:
      xDir, yDir = vec
      for numSteps in range(1, piece.getStepLimit() + 1):
        x = currX + ( numSteps * xDir )
        y = currY + ( numSteps * yDir )

        if not self.isValidMove( ( x, y ) ):
          break

        moves.add( ( x, y ) )

    return moves

  def move(self, startPos, endPos):
    self.addPiece( endPos, self.getPiece( startPos ) )
    self.removePiece( startPos )
    self.getPiece( endPos ).setHasMoved()
