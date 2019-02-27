# This is the base class of a Template Design Pattern and should not
# be instantiated.
class Movement:
  def __init__(self):
    pass

  def getMoves(self, board, pos):
    moves = set()
    piece = board.getPiece( pos )
    currX, currY = pos

    #movementVector = piece.getMovementVectors()
    movementVector = self.getMovementVectors( piece )
    stepLimit = self.getStepLimit( piece )

    for vec in movementVector:
      xDir, yDir = vec
      for numSteps in range(1, stepLimit + 1):
        potentialMove = currX + ( numSteps * xDir ), currY + ( numSteps * yDir )

        if not board.isValidMove( potentialMove ):
          break

        if board.isCollision( potentialMove ):
          if board.isOpponentPiece( piece, board.getPiece( potentialMove ) ):
            #moves.add( Move( pos, potentialMove, MoveType.EAT ) )
            moves = self.checkToAddEat( moves, pos, potentialMove )
          break

        #moves.add( Move( pos, potentialMove ) )
        moves = self.checkToAddMove( moves, pos, potentialMove )

    return moves

  def getStepLimit(self, piece):
    pass

  def getMovementVectors(self, piece):
    pass

  def checkToAddEat(self, currPos, potentialMove):
    pass

  def checkToAddMove(self, currPos, potentialMove):
    pass
