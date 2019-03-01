class View:
  def __init__(self):
    pass

  def display(self, board, game, moves = None):
    print( board.toString( game, moves ) )

    if game.getIsCheckMate():
      self.displayCheckMate( game.getInCheckMate() )
    elif game.getIsDraw():
      kings = board.getKingsPair()
      self.displayDraw( *kings )
    elif game.getIsCheck():
      self.displayCheck( game.getInCheck() )

  def displayCheck(self, piece):
    print ( "Check at %s [ %s ]" % ( piece.getPos(), piece.getColor() ) )

  def displayCheckMate(self, piece):
    print ( "CheckMate at %s [ %s ]" % ( piece.getPos(), piece.getColor() ) )

  def displayDraw(self, lightKing, darkKing):
    print ( "Draw at %s and %s" % ( lightKing.getPos(), darkKing.getPos() ) )
