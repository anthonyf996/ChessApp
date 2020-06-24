from ControllerFactory import ControllerFactory 
from ConsoleView import ConsoleView
from Model import Model
from ConsoleClock import ConsoleClock
from ConsoleInputReader import ConsoleInputReader 
from InputController import InputController 
from MoveController import MoveController
from ConsoleControllerStateManager import ConsoleControllerStateManager 
from ExceptionHandler import ExceptionHandler 
from GameResetException import GameResetException 
from ConsoleKeyHandler import ConsoleKeyHandler
from AI import AI
from HintManager import HintManager
from MoveHistory import MoveHistory

class ConsoleControllerFactory(ControllerFactory):
  def createModel(self):
    return Model( boardconfigFileName = "Model/StandardConfig.json" )

  def createView(self):
    return ConsoleView()

  def createClock(self):
    return ConsoleClock( fpsSpec = { "FPS" : 60, "AI_FPS" : 2, "TESTING_FPS" : 500 } )

  def createInputReader(self, View, Game, MoveController, KeyHandler):
    return ConsoleInputReader( {
                               #"getPosPairFromCursor" : View.getPosPairFromCursor,
                               "handleKeyPress" : KeyHandler.handleKeyPress,
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

  def createMoveHistory(self, Model):
    return MoveHistory( Model.getBoard() )

  def createKeyHandler(self, Model, MoveController, HintManager):
    return ConsoleKeyHandler( Model.getBoard(), Model.getGame(), MoveController, HintManager )

  def createHintManager(self, Game, AI):
    return HintManager( Game, AI )

  def createAI(self, Model):
    return AI( Model, Model.getBoard(), Model.getGame() )

  def createStateManager(self, View, Model, Controller, MoveController, InputController,\
                         AI, HintManager):
    return ConsoleControllerStateManager( View, Model, MoveController,\
                                            InputController, AI, HintManager )
