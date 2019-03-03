from PieceColor import PieceColor

# This is the base class of a Template Design Pattern and should not
# be instantiated.
class GetMovement:
  def __init__(self):
    pass

  def getMoves(self, board, pos):
    moves = set()
    piece = board.getPiece( pos )
    currX, currY = pos

    movementVector = self.getMovementVectors( piece )
    stepLimit = self.getStepLimit( piece )

    for vec in movementVector:
      xDir, yDir = vec

      if piece.getColor() == PieceColor.LIGHT:
        yDir *= -1

      for numSteps in range(1, stepLimit + 1):
        potentialMove = currX + ( numSteps * xDir ), currY + ( numSteps * yDir )

        if not board.isValidMove( potentialMove ):
          break

        if board.isCollision( potentialMove ):
          moves = self.checkToAddCollision( board, moves, pos, potentialMove )
          if board.isOpponentPiece( piece, board.getPiece( potentialMove ) ):
            moves = self.checkToAddEat( board, moves, pos, potentialMove )
          break

        moves = self.checkToAddMove( board, moves, pos, potentialMove )

    return moves

  def getStepLimit(self, piece):
    raise NotImplementedError

  def getMovementVectors(self, piece):
    raise NotImplementedError

  def checkToAddEat(self, board, moves, currPos, potentialMove):
    return moves

  def checkToAddMove(self, board, moves, currPos, potentialMove):
    return moves

  def checkToAddCollision(self, board, moves, currPos, potentialMove):
    return moves
