from GetMovement import GetMovement

class GetCollisionMovement(GetMovement):
  def getStepLimit(self, piece):
    return piece.getEatStepLimit()

  def getMovementVectors(self, piece):
    return piece.getEatVectors()

  def checkToAddCollision(self, board, moves, currPos, potentialMove):
    moves.add( potentialMove )
    return moves
