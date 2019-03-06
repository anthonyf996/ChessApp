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

class ConsoleControllerFactory(ControllerFactory):
  def createModel(self):
    return Model( boardconfigFileName = "Model/StandardConfig.json" )

  def createView(self):
    return ConsoleView()

  def createClock(self):
    return ConsoleClock( fpsSpec = { "FPS" : 60 } )

  def createInputReader(self, View, Game, MoveController):
    return ConsoleInputReader( {
                               #"getPosPairFromCursor" : View.getPosPairFromCursor,
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

  def createStateManager(self, View, Model, MoveController, InputController):
    return ConsoleControllerStateManager( View, Model, MoveController, InputController )
