class View:
  def __init__(self):
    pass

  def display(self, board, game, moves = None):
    self.displayBoard( board, game, moves )

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

  def displayBoard(self, board, game = None, moves = None):
    moveArr = board.getMovesEndPos( moves )

    s = ""
    for y in range(0,board.numRows):
      for x in range(0,board.numCols):
        pos = ( x, y )
        p = board.getPiece( pos )

        if pos in moveArr:
          if p is None:
            s += "||||||||||"
          else:
            s += self.pieceToStr( board, game, p ).replace( " ", "|" )
        elif p is None:
          s += "|         "
        else:
            s += self.pieceToStr( board, game, p )
      s += "|\n"

    print( s )

  def pieceToStr(self, board, game, piece):
    if  game.getIsCheckMate() and piece == game.getInCheckMate():
      return "|{{{{%s}}}}" % ( str( piece ) )
    elif game.getIsDraw() and piece in board.getKingsPair():
      return "|((((%s))))" % ( str( piece ) )
    elif game.getIsCheck() and piece == game.getInCheck():
      return "|<<<<%s>>>>" % ( str( piece ) )
    else:
      return "|    %s    " % ( str( piece ) )
