from Move import Move

class SimpleMove(Move):
  def __init__(self, startPos, endPos):
    super().__init__(startPos, endPos)
    self.prevHasMoved = None
    self.prevStartPiece = None
    self.prevEndPiece = None

  def perform(self, board):
    self.prevStartPiece = board.getPiece( self.startPos )
    self.prevEndPiece = board.getPiece( self.endPos )
    self.prevHasMoved = self.prevStartPiece.getHasMoved()

    board.addPiece( self.endPos, board.getPiece( self.startPos ) )
    board.removePiece( self.startPos )

    board.getPiece( self.endPos ).setHasMoved( True )
    
  def undo(self, board):
    board.addPiece( self.startPos, self.prevStartPiece )
    board.addPiece( self.endPos, self.prevEndPiece )
    self.prevStartPiece.setHasMoved( self.prevHasMoved )
