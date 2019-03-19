from ControllerStateManager import ControllerStateManager
from StateType import StateType
from GUIMainState import GUIMainState
from GUIAIState import GUIAIState
from GUIPieceUpgradeState import GUIPieceUpgradeState 
from GUIPauseState import GUIPauseState 

class GUIControllerStateManager(ControllerStateManager):
  def __init__(self, View, Model, MoveController, InputController, AI, HintManager):
    super().__init__( View, Model, MoveController, InputController, AI, HintManager)
    self.states[ StateType.MAIN ] = GUIMainState( self, self.View, self.Model,\
                                      self.MoveController, self.InputController,\
                                      self.HintManager )
    self.states[ StateType.PAUSE ] = GUIPauseState( self, self.View, self.Model,\
                                      self.MoveController, self.InputController )
    self.states[ StateType.AI ] = GUIAIState( self, self.View, self.Model,\
                                    self.MoveController, self.InputController,\
                                    self.AI )
    self.states[ StateType.PIECE_UPGRADE ] = GUIPieceUpgradeState( self,\
                                               self.View,\
                                               self.MoveController,\
                                               self.InputController,\
                                               self.Model.getBoard(),\
                                               self.Model.getGame() )
    self.reset()

  def reset(self):
    self.currState = self.states[ StateType.MAIN ]
    self.HintManager.clearHint()
