from MoveController import MoveController
from InputController import InputController
#from ConsoleInputReader import ConsoleInputReader
from GUIInputReader import GUIInputReader
from GameExitException import GameExitException
#from ConsoleClock import ConsoleClock
from ExceptionHandler import ExceptionHandler
from GameResetException import GameResetException
from ControllerStateManager import ControllerStateManager

class Controller:
  def __init__(self, View, Model, Clock, InputReader):
    self.View = View
    self.Model = Model
    #self.Clock = ConsoleClock( fpsSpec = { "FPS" : 60 } )
    self.Clock = Clock
    self.MoveController = MoveController()
    self.InputReader = InputReader
    self.InputReader.addCallback( "getPosPairFromCursor", self.View.getPosPairFromCursor )
    self.InputReader.addCallback( "getCurrPos", self.MoveController.getCurrPos )
    self.InputReader.addCallback( "isGameOver", self.Model.isGameOver )
    self.InputReader.addCallback( "getTurnColor", self.Model.getTurnColor )

    """
    self.InputReader = ConsoleInputReader( { 
                               "getCurrPos" : self.MoveController.getCurrPos, 
                               "isGameOver" : self.Model.isGameOver, 
                               "getTurnColor" : self.Model.getTurnColor 
                             } )
    self.InputReader = GUIInputReader( {
                               "getPosPairFromCursor" : self.View.getPosPairFromCursor,
                               "getCurrPos" : self.MoveController.getCurrPos, 
                               "isGameOver" : self.Model.isGameOver, 
                               "getTurnColor" : self.Model.getTurnColor 
                             } )
    """
    self.InputController = InputController( 
                             self.InputReader,
                             ExceptionHandler( 
                               self.InputReader.read, 
                               [ GameResetException() ],
                               self.reset
                             ) )

    self.StateManager = ControllerStateManager( self.View, self.Model, self.MoveController )

  def run(self):
    try:
      while True:
        self.StateManager.updateView()

        cursor = self.InputController.pollUserInput()

        self.StateManager.updateModel( cursor )

        self.Clock.tick()
    except GameExitException as e:
      print( e )
    finally:
      self.finish()

  def finish(self):
    self.View.finish()

  def reset(self):
    self.Model.getBoard().reset()
    self.Model.getGame().reset()
    self.MoveController.reset()
    self.StateManager.reset()
