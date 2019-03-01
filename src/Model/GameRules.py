from King import King

class GameRules:
  def __init__(self):
    self.TURN_COUNT_FOR_DRAW = 50

  def isInCheck(self, board, kingPos):
    return board.isInDanger( kingPos )

  def isInCheckMate(self, board, kingPos):
    kingColor = board.getPiece( kingPos ).getColor()
    return self.isInCheck( board, kingPos ) and \
           board.isKingTrapped( kingPos )

  def isDraw(self, board, game, firstKingPos, secondKingPos):
    if game.getTurnCount() // 2 >= self.TURN_COUNT_FOR_DRAW:
      return True

    firstKingColor = board.getPiece( firstKingPos ).getColor()
    secondKingColor = board.getPiece( secondKingPos ).getColor()

    isDraw = False

    firstKingDraw = board.isKingTrapped( firstKingPos ) and \
           not self.isInCheck( board, firstKingPos ) and \
           board.isLastPiece( firstKingPos )

    if firstKingDraw:
      return True

    secondKingDraw = board.isKingTrapped( secondKingPos ) and \
           not self.isInCheck( board, secondKingPos ) and \
           board.isLastPiece( secondKingPos )

    if secondKingDraw:
      return True

    return board.isLastPiece( firstKingPos ) and board.isLastPiece( secondKingPos )

