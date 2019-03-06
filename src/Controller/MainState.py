from ControllerState import ControllerState

class MainState(ControllerState):
  def __init__(self, StateManager, View, Model, MoveController):
    self.StateManager = StateManager
    self.View = View
    self.Model = Model
    self.MoveController = MoveController

  def updateView(self):
    self.View.display( self.Model.getBoard(), self.Model.getGame(),\
                       self.MoveController.getMoves( self.Model.getBoard() ),\
                       self.MoveController.getCurrPos() )
    self.View.update()

  def updateModel(self, cursor):
    pos = self.View.getPosPairFromCursor( cursor )
    self.MoveController.handleInput( self.StateManager, self.Model.getBoard(),\
                                     self.Model.getGame(), pos )
    self.Model.update()