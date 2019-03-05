from MoveController import MoveController
from InputController import InputController
#from ConsoleInputReader import ConsoleInputReader
from GUIInputReader import GUIInputReader
from GameExitException import GameExitException
#from ConsoleClock import ConsoleClock
from ExceptionHandler import ExceptionHandler
from GameResetException import GameResetException

class Controller:
  def __init__(self, View, Model, Clock):
    self.View = View
    self.Model = Model
    #self.Clock = ConsoleClock( fpsSpec = { "FPS" : 60 } )
    self.Clock = Clock
    self.MoveController = MoveController()
    """
    self.InputReader = ConsoleInputReader( { 
                               "getCurrPos" : self.MoveController.getCurrPos, 
                               "isGameOver" : self.Model.isGameOver, 
                               "getTurnColor" : self.Model.getTurnColor 
                             } )
    """
    self.InputReader = GUIInputReader( {
                               "getPosPairFromCursor" : self.View.getPosPairFromCursor,
                               "getCurrPos" : self.MoveController.getCurrPos, 
                               "isGameOver" : self.Model.isGameOver, 
                               "getTurnColor" : self.Model.getTurnColor 
                             } )
    #self.InputController = ConsoleInputController( 
    self.InputController = InputController( 
                             self.InputReader,
                             ExceptionHandler( 
                               self.InputReader.read, 
                               [ GameResetException() ],
                               self.reset
                             ) )
    self.Model.registerRequestUpgradeTypeCallback( self.InputReader.promptUpgradeType )

  def run(self):
    try:
      while True:
        self.updateView()

        pos = self.InputController.pollUserInput()

        self.MoveController.handleInput( self.Model.getBoard(), self.Model.getGame(), pos )

        self.updateModel()

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

  def updateView(self):
    self.View.display( self.Model.getBoard(), self.Model.getGame(), self.MoveController.getMoves( self.Model.getBoard() ) )

  def updateModel(self):
    self.Model.update()
