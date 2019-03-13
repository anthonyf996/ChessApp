from ControllerState import ControllerState
from StateType import StateType

class GUIMainState(ControllerState):
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
    pos = None
    if self.Game.getPlayersEnabled():
      pos = self.View.getPosPairFromCursor( cursor )
    self.MoveController.handleInput( self.StateManager, self.Board,\
                                     self.Game, pos )
    self.Model.update()

    if not self.Game.isGameOver():
      if self.Game.getPlayersEnabled():
        if self.Game.getIsAIEnabled() and self.Game.getIsAITurn():
          self.StateManager.setState( StateType.AI )
      else:
        self.StateManager.setState( StateType.AI )
