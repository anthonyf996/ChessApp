from ControllerState import ControllerState
from StateType import StateType

class PieceUpgradeState(ControllerState):
  def __init__(self, StateManager, View, MoveController, Board, Game):
    self.StateManager = StateManager
    self.View = View
    self.MoveController = MoveController
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
    self.View.showUpgradeMenu( self.color )
    self.View.update()

  def updateModel(self, cursor):
    self.upgradeType = self.View.promptUpgradeType( cursor )
    if self.upgradeType is not None:
      self.View.removeUpgradeMenu()
      self.pieceUpgradeCommand.setUpgradeType( self.upgradeType )
      self.MoveController.performMove( self.Board, self.Game, self.move )
      self.clear()
      #self.Controller.setState( self.Controller.getState( StateType.MAIN ) )
      self.StateManager.setState( StateType.MAIN )
