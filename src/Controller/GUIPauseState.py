from ControllerState import ControllerState
from StateType import StateType

class GUIPauseState(ControllerState):
  def __init__(self, StateManager, View, Model, MoveController, InputController):
    self.StateManager = StateManager
    self.View = View
    self.Model = Model
    self.MoveController = MoveController
    self.InputController = InputController
    self.Board = self.Model.getBoard()
    self.Game = self.Model.getGame()

  def updateView(self):
    self.View.display( self.Board, self.Game,\
                       self.MoveController.getMoves( self.Board ),\
                       self.MoveController.getCurrPos(),\
                       self.MoveController.getPrevPos() )
    self.View.update()

  def pollUserInput(self):
    return self.InputController.pollUserInput()

  def updateModel(self, cursor):
    self.MoveController.handleInput( self.StateManager, self.Board, self.Game, None )

    if not self.Game.getIsPaused():
      #self.StateManager.setState( StateType.MAIN )
      self.StateManager.setPriorState()
