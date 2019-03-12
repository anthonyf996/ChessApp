from ControllerState import ControllerState
from StateType import StateType

class ConsoleMainState(ControllerState):
  def __init__(self, StateManager, View, Model, MoveController, InputController):
    self.StateManager = StateManager
    self.View = View
    self.Model = Model
    self.MoveController = MoveController
    self.InputController = InputController
    self.Game = self.Model.getGame()

  def updateView(self):
    self.View.display( self.Model.getBoard(), self.Model.getGame(),\
                       self.MoveController.getMoves( self.Model.getBoard() ) )

  def pollUserInput(self):
    return self.InputController.pollUserInput()

  def updateModel(self, pos):
    self.MoveController.handleInput( self.StateManager, self.Model.getBoard(),\
                                     self.Model.getGame(), pos )
    self.Model.update()

    if not self.Game.isGameOver() and self.Game.getIsAIEnabled() and\
      self.Game.getIsAITurn():
      self.StateManager.setState( StateType.AI )
