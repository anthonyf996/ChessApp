from StateManager import StateManager
from StateType import StateType
from MainState import MainState
from PieceUpgradeState import PieceUpgradeState 

class ControllerStateManager(StateManager):
  def __init__(self, View, Model, MoveController):
    super().__init__()
    self.View = View
    self.Model = Model
    self.MoveController = MoveController
    self.states[ StateType.MAIN ] = MainState( self, self.View, self.Model,\
                                               self.MoveController )
    self.states[ StateType.PIECE_UPGRADE ] = PieceUpgradeState( self, self.View,\
                                               self.MoveController, self.Model.getBoard(),\
                                               self.Model.getGame() )
    self.reset()

  def getState(self, key):
    return self.states[ key ]

  def setState(self, key):
    self.currState = self.states[ key ]

  def reset(self):
    self.currState = self.states[ StateType.MAIN ]

  def updateView(self):
    self.currState.updateView()

  def updateModel(self, cursor):
    self.currState.updateModel( cursor )
