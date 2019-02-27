from SimpleMove import SimpleMove
from GetMovement import GetMovement

class GetSimpleMovement(GetMovement):
  def getStepLimit(self, piece):
    return piece.getStepLimit()

  def getMovementVectors(self, piece):
    return piece.getMovementVectors()

  def checkToAddEat(self, moves, currPos, potentialMove):
    return moves

  def checkToAddMove(self, moves, currPos, potentialMove):
    moves.add( SimpleMove( currPos, potentialMove ) )

    return moves
