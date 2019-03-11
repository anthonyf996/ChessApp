from ControllerState import ControllerState
from AI import AI
from StateType import StateType
from PieceColor import PieceColor

class GUIAIState(ControllerState):
  def __init__(self, StateManager, View, Model, MoveController, InputController):
    self.StateManager = StateManager
    self.View = View
    self.Model = Model
    self.MoveController = MoveController
    self.InputController = InputController
    self.AI = AI( self.Model.getBoard(), self.Model.getGame(),\
                  self.Model.getGame().getAIColor() )

  def updateView(self):
    self.View.display( self.Model.getBoard(), self.Model.getGame(),\
                       self.MoveController.getMoves( self.Model.getBoard() ),\
                       self.MoveController.getCurrPos() )
    self.View.update()

  def pollUserInput(self):
    pass

  def updateModel(self, cursor):
    move = self.AI.getMove() 
    self.MoveController.performMove( self.Model.getBoard(), self.Model.getGame(),\
                                     move )
    self.Model.update()
    if not self.Model.getGame().getIsAITurn():
      self.StateManager.setState( StateType.MAIN )
