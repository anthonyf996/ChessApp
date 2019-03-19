class KeyHandler:
  def __init__(self, Game, HintManager):
    self.Game = Game
    self.HintManager = HintManager

  def handleKeyPress(self, k):
    raise NotImplementedError
