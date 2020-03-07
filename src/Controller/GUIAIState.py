from time import sleep
from ControllerState import ControllerState
from AI import AI
from StateType import StateType
from PieceColor import PieceColor

class GUIAIState(ControllerState):
  def __init__(self, StateManager, View, Model, Controller, MoveController, InputController,\
               AI):
    self.StateManager = StateManager
    self.View = View
    self.Model = Model
    self.Controller = Controller
    self.MoveController = MoveController
    self.InputController = InputController
    self.AI = AI
    self.Game = self.Model.getGame()
    #self.AI = AI( self.Model, self.Model.getBoard(), self.Model.getGame(),\
    #              self.Model.getGame().getAIColor() )

  def updateView(self):
    self.View.display( self.Model.getBoard(), self.Model.getGame(),\
                       self.MoveController.getMoves( self.Model.getBoard() ),\
                       self.MoveController.getCurrPos() )
    self.View.update()

  def pollUserInput(self):
    return self.InputController.pollUserInput()

  def updateModel(self, cursor):
    move = self.AI.getMove( self.Model.getGame().getTurnColor() ) 
    self.MoveController.performMove( self.Model.getBoard(), self.Model.getGame(),\
                                     move )
    self.Model.update()

    if self.Game.isGameOver():
      if self.Game.getIsTesting():
        self.updateView()
        self.Controller.reset()
        sleep( 5 )
    else:
      if self.Game.getIsPaused():
        self.StateManager.setState( StateType.PAUSE )
      elif self.Model.getGame().getPlayersEnabled():
        self.StateManager.setState( StateType.MAIN )
