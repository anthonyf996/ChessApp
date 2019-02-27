from EatMove import EatMove
from GetMovement import GetMovement

class GetEatMovement(GetMovement):
  def getStepLimit(self, piece):
    return piece.getEatStepLimit()

  def getMovementVectors(self, piece):
    return piece.getEatVectors()

  def checkToAddEat(self, board, moves, currPos, potentialMove):
    moves.add( EatMove( board, currPos, potentialMove ) )
    return moves

  def checkToAddMove(self, board, moves, currPos, potentialMove):
    return moves
