class KeyHandler:
  def __init__(self, Game, MoveController, HintManager):
    self.Game = Game
    self.MoveController = MoveController
    self.HintManager = HintManager

  def handleKeyPress(self, k):
    raise NotImplementedError
