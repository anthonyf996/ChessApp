from MoveType import MoveType
from Move import Move
from Movement import Movement

class EatMovement(Movement):
  def getStepLimit(self, piece):
    return piece.getEatStepLimit()

  def getMovementVectors(self, piece):
    return piece.getEatVectors()

  def checkToAddEat(self, moves, currPos, potentialMove):
    moves.add( Move( currPos, potentialMove, MoveType.EAT ) )
    return moves

  def checkToAddMove(self, moves, currPos, potentialMove):
    return moves
