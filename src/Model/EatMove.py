from SimpleMove import SimpleMove
from MoveType import MoveType

class EatMove(SimpleMove):
  def __init__(self, board, startPos, endPos):
    super().__init__(board, startPos, endPos)

  def getMoveType(self):
    return MoveType.EAT
