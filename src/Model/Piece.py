class Piece:
  def __init__(self, color, stepLimit ):
    self.pos = None
    self.color = color
    self.movementVectors = set()
    self.stepLimit = stepLimit
    self.hasMoved = False

  def getPos(self):
    return self.pos

  def getColor(self):
    return self.color

  def getMovementVectors(self):
    return self.movementVectors

  def getEatVectors(self):
    return self.getMovementVectors()

  def getEatStepLimit(self):
    return self.getStepLimit()

  def getStepLimit(self):
    return self.stepLimit

  def getHasMoved(self):
    return self.hasMoved

  def setPos(self, pos):
    self.pos = pos

  def setHasMoved(self, b = True):
    self.hasMoved = b

  def getSpecialMoves(self, board, currPos):
    return set()
