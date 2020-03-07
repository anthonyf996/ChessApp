from ControllerState import ControllerState
from StateType import StateType
from time import sleep

class GUIMainState(ControllerState):
  def __init__(self, StateManager, View, Model, Controller, MoveController, InputController, HintManager):
    self.StateManager = StateManager
    self.View = View
    self.Model = Model
    self.Controller = Controller
    self.MoveController = MoveController
    self.InputController = InputController
    self.HintManager = HintManager
    self.Board = self.Model.getBoard()
    self.Game = self.Model.getGame()

  def updateView(self):
    hint = self.HintManager.getHint()
    hintStart, hintEnd = None, None
    if hint is not None:
      hintStart, hintEnd = hint.getStartPos(), hint.getEndPos()

    self.View.display( self.Board, self.Game,\
                       self.MoveController.getMoves( self.Board ),\
                       self.MoveController.getCurrPos(),\
                       self.MoveController.getPrevPos(),\
                       hintStart, hintEnd )
    self.View.update()

  def pollUserInput(self):
    return self.InputController.pollUserInput()

  def updateModel(self, cursor):
    pos = None
    if self.Game.getPlayersEnabled():
      pos = self.View.getPosPairFromCursor( cursor )
    success = self.MoveController.handleInput( self.StateManager, self.Board,\
                                                 self.Game, pos )
    if success:
      self.HintManager.clearHint()

    self.Model.update()

    if not self.Game.isGameOver():
      if self.Game.getIsPaused():
        self.StateManager.setState( StateType.PAUSE )
      elif self.Game.getPlayersEnabled():
        if self.Game.getIsAIEnabled() and self.Game.getIsAITurn():
          self.StateManager.setState( StateType.AI )
      else:
        self.StateManager.setState( StateType.AI )
    elif self.Game.getIsTesting():
      self.Controller.reset()
      sleep( 5 )
