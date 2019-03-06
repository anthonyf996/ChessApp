from ControllerState import ControllerState
from StateType import StateType

class ConsolePieceUpgradeState(ControllerState):
  def __init__(self, StateManager, View, MoveController, InputController, Board, Game):
    self.StateManager = StateManager
    self.View = View
    self.MoveController = MoveController
    self.InputController = InputController
    self.Board = Board
    self.Game = Game
    self.clear()

  def clear(self):
    self.move = None
    self.pieceUpgradeCommand = None
    self.color = None
    self.upgradeType = None

  def update(self, move, pieceUpgradeCommand, color):
    self.move = move
    self.pieceUpgradeCommand = pieceUpgradeCommand
    self.color = color

  def updateView(self):
    pass

  def pollUserInput(self):
    pass

  def updateModel(self, cursor):
    self.upgradeType = self.View.promptUpgradeType()
    if self.upgradeType is not None:
      self.pieceUpgradeCommand.setUpgradeType( self.upgradeType )
      self.MoveController.performMove( self.Board, self.Game, self.move )
      self.clear()
      self.StateManager.setState( StateType.MAIN )
