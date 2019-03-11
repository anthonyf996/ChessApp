from ControllerStateManager import ControllerStateManager
from StateType import StateType
from GUIMainState import GUIMainState
from GUIAIState import GUIAIState
from GUIPieceUpgradeState import GUIPieceUpgradeState 

class GUIControllerStateManager(ControllerStateManager):
  def __init__(self, View, Model, MoveController, InputController):
    super().__init__( View, Model, MoveController, InputController)
    self.states[ StateType.MAIN ] = GUIMainState( self, self.View, self.Model,\
                                               self.MoveController, self.InputController )
    self.states[ StateType.AI ] = GUIAIState( self, self.View, self.Model,\
                                               self.MoveController, self.InputController )
    self.states[ StateType.PIECE_UPGRADE ] = GUIPieceUpgradeState( self, self.View,\
                                               self.MoveController, self.InputController,\
                                               self.Model.getBoard(),\
                                               self.Model.getGame() )
    self.reset()

  def reset(self):
    self.currState = self.states[ StateType.MAIN ]
