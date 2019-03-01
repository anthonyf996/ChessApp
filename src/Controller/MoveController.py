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

  def handleInput(self, board, game, pos):
    if board.isValidMove( pos ):
      self.updatePos( pos )
      self.checkToMove( board, game )

  def updatePos(self, pos):
    self.prevPos = self.currPos
    self.currPos = pos

  def checkToMove(self, board, game):
    if self.currPos is not None:
      if self.currPiece is not None:
        moves = board.getAllMoves( self.prevPos )

        if not game.isGameOver():
          if not game.getTurnsEnabled() or self.currPiece.getColor() == game.getTurnColor():
            for m in moves:
              if ( self.prevPos, self.currPos ) == m.getPosPair():
                board.move( m )
                if board.isInDanger( board.getKing( self.currPiece.getColor() ).getPos() ):
                  board.undo( m )
                else:
                  game.advanceTurn()
                break

        self.currPiece = None
        self.moves = None
      else:
        self.currPiece = board.getPiece( self.currPos )
        if self.currPiece is not None:
          self.moves = board.getAllMoves( self.currPos )
