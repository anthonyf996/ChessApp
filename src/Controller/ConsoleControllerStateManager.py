from ControllerStateManager import ControllerStateManager
from StateType import StateType
from ConsoleMainState import ConsoleMainState
from ConsolePieceUpgradeState import ConsolePieceUpgradeState 
from ConsoleAIState import ConsoleAIState

class ConsoleControllerStateManager(ControllerStateManager):
  def __init__(self, View, Model, MoveController, InputController, AI):
    super().__init__( View, Model, MoveController, InputController, AI )
    self.states[ StateType.MAIN ] = ConsoleMainState( self, self.View, self.Model,\
                                               self.MoveController, self.InputController )
    self.states[ StateType.AI ] = ConsoleAIState( self, self.View, self.Model,\
                                    self.MoveController, self.InputController,\
                                    self.AI )
    self.states[ StateType.PIECE_UPGRADE ] = ConsolePieceUpgradeState( self, self.View,\
                                               self.MoveController, self.InputController,\
                                               self.Model.getBoard(),\
                                               self.Model.getGame() )
    self.reset()

  def reset(self):
    self.currState = self.states[ StateType.MAIN ]
