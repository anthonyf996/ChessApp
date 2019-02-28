from SimpleMove import SimpleMove
from GetMovement import GetMovement

class GetSimpleMovement(GetMovement):
  def getStepLimit(self, piece):
    return piece.getStepLimit()

  def getMovementVectors(self, piece):
    return piece.getMovementVectors()

  def checkToAddMove(self, board, moves, currPos, potentialMove):
    moves.add( SimpleMove( board, currPos, potentialMove ) )

    return moves
