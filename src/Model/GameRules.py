from King import King

class GameRules:
  def __init__(self):
    pass

  def isInCheck(self, board, kingPos):
    return self.isInDanger( board, kingPos, board.getPiece( kingPos ).getColor() )

  def isInDanger(self, board, currPos, color):
    inDanger = False

    for y in range(0,board.getNumRows()):
      for x in range(0,board.getNumCols()):
        pos = ( x, y )
        piece = board.getPiece( pos )

        if piece is None:
          continue
        if piece.getColor() == color:
          continue

        eatMoves = board.getEatMoves( pos )

        for move in eatMoves:
          if currPos in move.getPosPair():
            inDanger = True
            break

    return inDanger

  def isInCheckMate(self, board, kingPos):
    kingColor = board.getPiece( kingPos ).getColor()
    return self.isInCheck( board, kingPos ) and \
           self.isTrapped( board, kingPos, kingColor )

  def isTrapped(self, board, currPos, color):
    moves = board.getAllMoves( currPos )
    currPiece = board.getPiece( currPos )

    isTrapped = True

    for move in moves:
      start, end = move.getPosPair()

      board.move( move )
      inDanger = self.isInDanger( board, end, color )
      board.undo( move )

      if inDanger:
        continue
      else:
        isTrapped = False
        #print ( "KING MOVE AVAILABLE: %s" % ( move ) )
        break

    if isTrapped:
      for y in range(0,board.getNumRows()):
        for x in range(0,board.getNumCols()):
          pos = ( x, y )
          piece = board.getPiece( pos )
          if piece is None:
            continue
          if piece.getColor() != color:
            continue
          if piece == currPiece:
            continue

          moves = board.getAllMoves( pos )

          for move in moves:
            board.move( move )
            inDanger = self.isInDanger( board, currPos, color )
            board.undo( move )

            if inDanger:
              continue
            else:
              isTrapped = False
              #print ( "OTHER MOVE AVAIL: %s" % ( move ) )
              break

    return isTrapped

  def isDraw(self, board, firstKingPos, secondKingPos):
    firstKingColor = board.getPiece( firstKingPos ).getColor()
    secondKingColor = board.getPiece( secondKingPos ).getColor()

    isDraw = False

    firstKingDraw = self.isTrapped( board, firstKingPos, firstKingColor ) and \
           not self.isInCheck( board, firstKingPos ) and \
           self.isLastPiece( board, firstKingPos )

    if firstKingDraw:
      return True

    secondKingDraw = self.isTrapped( board, secondKingPos, secondKingColor ) and \
           not self.isInCheck( board, secondKingPos ) and \
           self.isLastPiece( board, secondKingPos )

    if secondKingDraw:
      return True

    return self.isLastPiece( board, firstKingPos ) and self.isLastPiece( board, secondKingPos )

  def isLastPiece(self, board, kingPos):
    king = board.getPiece( kingPos )

    for y in range(0,board.getNumRows()):
      for x in range(0,board.getNumCols()):
        pos = ( x, y )
        piece = board.getPiece( pos )

        if piece is None:
          continue
        if piece == king:
          continue
        if piece.getColor() == king.getColor():
          return False

    return True
