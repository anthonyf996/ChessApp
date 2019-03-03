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

    firstKingDraw = board.noMovesLeft( firstKingPos ) and \
           not self.isInCheck( board, firstKingPos )

    if firstKingDraw:
      return True

    secondKingDraw = board.noMovesLeft( secondKingPos ) and \
           not self.isInCheck( board, secondKingPos )

    if secondKingDraw:
      return True

    return board.isLastPiece( firstKingPos ) and board.isLastPiece( secondKingPos )
