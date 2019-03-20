class KeyHandler:
  def __init__(self, Board, Game, MoveController, HintManager):
    self.Board = Board
    self.Game = Game
    self.MoveController = MoveController
    self.HintManager = HintManager

  def handleKeyPress(self, k):
    raise NotImplementedError
