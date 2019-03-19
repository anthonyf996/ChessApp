from ControllerState import ControllerState
from StateType import StateType

class ConsoleMainState(ControllerState):
  def __init__(self, StateManager, View, Model, MoveController, InputController,\
                 HintManager):
    self.StateManager = StateManager
    self.View = View
    self.Model = Model
    self.MoveController = MoveController
    self.InputController = InputController
    self.HintManager = HintManager
    self.Game = self.Model.getGame()

  def updateView(self):
    hint = self.HintManager.getHint()
    hintStart, hintEnd = None, None
    if hint is not None:
      hintStart, hintEnd = hint.getStartPos(), hint.getEndPos()

    self.View.display( self.Model.getBoard(), self.Model.getGame(),\
                       self.MoveController.getMoves( self.Model.getBoard() ),\
                       self.MoveController.getPrevPos(),\
                       hintStart, hintEnd )

  def pollUserInput(self):
    resp = None
    if self.Game.getPlayersEnabled():
      resp = self.InputController.pollUserInput()
    return resp

  def updateModel(self, pos):
    success = self.MoveController.handleInput( self.StateManager, self.Model.getBoard(),\
                                     self.Model.getGame(), pos )
    if success:
      self.HintManager.clearHint()

    self.Model.update()

    if not self.Game.isGameOver():
      if self.Game.getPlayersEnabled():
        if self.Game.getIsAIEnabled() and self.Game.getIsAITurn():
          self.StateManager.setState( StateType.AI )
      else:
        self.StateManager.setState( StateType.AI )
