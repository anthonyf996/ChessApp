from Move import Move
from Movement import Movement

class SimpleMovement(Movement):
  def getStepLimit(self, piece):
    return piece.getStepLimit()

  def getMovementVectors(self, piece):
    return piece.getMovementVectors()

  def checkToAddEat(self, moves, currPos, potentialMove):
    return moves

  def checkToAddMove(self, moves, currPos, potentialMove):
    moves.add( Move( currPos, potentialMove ) )

    return moves
