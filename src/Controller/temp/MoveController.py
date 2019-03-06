class MoveController:
  def __init__(self):
    self.reset()

  def reset(self):
    self.currPos = None
    self.currPiece = None

  def getCurrPos(self):
    return self.currPos

  def getMoves(self, board):
    if self.currPiece is not None:
      return board.getAllMoves( self.currPos )
    return set()

  def handleInput(self, board, game, pos):
    if self.isValidMove( board, pos ):
      self.updatePos( pos )
      if self.readyToMove( game ):
        self.performMove( board, game, self.getMove( board ) )
      self.toggleCurrPiece( board )

  def isValidMove(self, board, pos):
    if pos is not None:
      if board.isValidMove( pos ):
        return True

    return False

  def updatePos(self, pos):
    if self.currPos is not None and self.currPiece is None:    
      self.currPos = None
    else:
      self.currPos = pos

  def readyToMove(self, game):
    if self.currPiece is not None:
      return self.canMove( game )

    return False
  
  def canMove(self, game):
    if not game.isGameOver():
      if not game.getTurnsEnabled() or self.currPiece.getColor() == game.getTurnColor():
        return True
      elif game.getTurnsEnabled():
        print( "%s's turn!" % ( game.getTurnColor() ) )

    return False

  def performMove(self, board, game, move):
    if move is not None:
      successful = board.move( move )
      if successful:
        print( move )
        game.advanceTurn()

  def toggleCurrPiece(self, board):
    if self.currPiece is None:
      if self.currPos is not None:
        self.currPiece = board.getPiece( self.currPos )
    else:
      self.currPiece = None
      self.currPos = None

  def getMove(self, board):
    for move in board.getAllMoves( self.currPiece.getPos() ):
      if ( self.currPiece.getPos(), self.currPos ) == move.getPosPair():
        return move

    return None