from StateManager import StateManager
from StateType import StateType

class ControllerStateManager(StateManager):
  def __init__(self, View, Model, MoveController, InputController, AI, HintManager):
    super().__init__()
    self.View = View
    self.Model = Model
    self.MoveController = MoveController
    self.InputController = InputController 
    self.AI = AI
    self.HintManager = HintManager

  def reset(self):
    raise NotImplementedError

  def updateView(self):
    self.currState.updateView()

  def pollUserInput(self):
    return self.currState.pollUserInput()

  def updateModel(self, cursor):
    self.currState.updateModel( cursor )
