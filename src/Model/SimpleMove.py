from Move import Move

class SimpleMove(Move):
  def __init__(self, board, startPos, endPos):
    super().__init__(board, startPos, endPos)
    self.prevHasMoved = None
    self.prevStartPiece = None
    self.prevEndPiece = None

  def execute(self):
    self.prevStartPiece = self.board.getPiece( self.startPos )
    self.prevEndPiece = self.board.getPiece( self.endPos )
    self.prevHasMoved = self.prevStartPiece.getHasMoved()

    self.board.addPiece( self.endPos, self.board.getPiece( self.startPos ) )
    self.board.removePiece( self.startPos )

    self.board.getPiece( self.endPos ).setHasMoved( True )
    
  def undo(self):
    self.board.addPiece( self.startPos, self.prevStartPiece )
    self.board.addPiece( self.endPos, self.prevEndPiece )
    self.prevStartPiece.setHasMoved( self.prevHasMoved )
