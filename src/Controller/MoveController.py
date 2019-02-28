class MoveController:
  def __init__(self):
    self.currPos = None
    self.prevPos = None
    self.currPiece = None
    self.moves = None

  def getCurrPos(self):
    return self.currPos

  def getMoves(self):
    return self.moves

  def handleInput(self, board, pos):
    if board.isValidMove( pos ):
      self.updatePos( pos )
      self.checkToMove( board )

  def updatePos(self, pos):
    self.prevPos = self.currPos
    self.currPos = pos

  def checkToMove(self, board):
    if self.currPos is not None:
      if self.currPiece is not None:
        moves = board.getAllMoves( self.prevPos )

        for m in moves:
          if ( self.prevPos, self.currPos ) == m.getPosPair():
            board.move( m )
            break

        self.currPiece = None
        self.moves = None
      else:
        self.currPiece = board.getPiece( self.currPos )
        if self.currPiece is not None:
          self.moves = board.getAllMoves( self.currPos )
