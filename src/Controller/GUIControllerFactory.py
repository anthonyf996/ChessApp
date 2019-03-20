from ControllerFactory import ControllerFactory 
from GUIView import GUIView
from Model import Model
from GUIClock import GUIClock
from GUIInputReader import GUIInputReader 
from InputController import InputController 
from MoveController import MoveController
from GUIControllerStateManager import GUIControllerStateManager
from ExceptionHandler import ExceptionHandler 
from GameResetException import GameResetException 
from GUIKeyHandler import GUIKeyHandler
from AI import AI
from HintManager import HintManager
from MoveHistory import MoveHistory

class GUIControllerFactory(ControllerFactory):
  def createModel(self):
    return Model( boardconfigFileName = "Model/StandardConfig.json" )

  def createView(self):
    return GUIView()

  def createClock(self):
    return GUIClock( fpsSpec = { "FPS" : 20, "AI_FPS" : 2, "TESTING_FPS" : 500 } )

  def createInputReader(self, View, Game, MoveController, KeyHandler):
    return GUIInputReader( {
                               "handleKeyPress" : KeyHandler.handleKeyPress,
                               "getPosPairFromCursor" : View.getPosPairFromCursor,
                               "getCurrPos" : MoveController.getCurrPos, 
                               "isGameOver" : Game.isGameOver, 
                               "getTurnColor" : Game.getTurnColor 
                             } )

  def createInputController(self, Controller, InputReader):
    return InputController( 
                             InputReader,
                             ExceptionHandler( 
                               InputReader.read, 
                               [ GameResetException() ],
                               Controller.reset
                             ) )

  def createMoveController(self, MoveHistory):
    return MoveController( MoveHistory )

  def createMoveHistory(self):
    return MoveHistory()

  def createKeyHandler(self, Model, MoveController, HintManager):
    return GUIKeyHandler( Model.getGame(), MoveController, HintManager )

  def createHintManager(self, Game, AI):
    return HintManager( Game, AI )

  def createAI(self, Model):
    return AI( Model, Model.getBoard(), Model.getGame(),\
                  Model.getGame().getAIColor() )

  def createStateManager(self, View, Model, MoveController, InputController,\
                         AI, HintManager):
    return GUIControllerStateManager( View, Model, MoveController,\
                                      InputController, AI, HintManager )
