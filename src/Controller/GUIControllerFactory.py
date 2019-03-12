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
from AI import AI

class GUIControllerFactory(ControllerFactory):
  def createModel(self):
    return Model( boardconfigFileName = "Model/StandardConfig.json" )

  def createView(self):
    return GUIView()

  def createClock(self):
    return GUIClock( fpsSpec = { "FPS" : 20 } )

  def createInputReader(self, View, Game, MoveController):
    return GUIInputReader( {
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

  def createMoveController(self):
    return MoveController()

  def createAI(self, Model):
    return AI( Model, Model.getBoard(), Model.getGame(),\
                  Model.getGame().getAIColor() )

  def createStateManager(self, View, Model, MoveController, InputController,\
                         AI):
    return GUIControllerStateManager( View, Model, MoveController,\
                                      InputController, AI )
