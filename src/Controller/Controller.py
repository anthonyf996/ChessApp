class Controller:
  def __init__(self, View, Model):
    self.View = View
    self.Model = Model
    self.board = Model.getBoard()
    self.currPos = None
    self.currPiece = None
    self.moves = None

  def run(self):
    while True:
      if self.moves is None:
        self.View.display( self.board )
      else:
        self.View.display( self.board, self.moves )

      prevPos = self.currPos
      self.currPos = self.View.getPos( prevPos )
      
      if not self.board.isValidMove( self.currPos ):
        self.currPos = prevPos
        continue
    
      if self.currPos is not None:
        if self.currPiece is not None:
          moves = self.board.getAllMoves( prevPos )

          for m in moves:
            if ( prevPos, self.currPos ) == m.getPosPair():
              self.board.move( m )

          self.currPiece = None
          self.moves = None
        else:
          self.currPiece = self.board.getPiece( self.currPos )
          if self.currPiece is not None:
            self.moves = self.board.getAllMoves( self.currPos )
