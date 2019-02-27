from EatMove import EatMove
from GetMovement import GetMovement

class GetEatMovement(GetMovement):
  def getStepLimit(self, piece):
    return piece.getEatStepLimit()

  def getMovementVectors(self, piece):
    return piece.getEatVectors()

  def checkToAddEat(self, moves, currPos, potentialMove):
    moves.add( EatMove( currPos, potentialMove ) )
    return moves

  def checkToAddMove(self, moves, currPos, potentialMove):
    return moves
