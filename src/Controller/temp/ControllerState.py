from MoveController import MoveController
from InputController import InputController
#from ConsoleInputReader import ConsoleInputReader
from GUIInputReader import GUIInputReader
from GameExitException import GameExitException
#from ConsoleClock import ConsoleClock
from ExceptionHandler import ExceptionHandler
from GameResetException import GameResetException

class ControllerState:
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
                               "promptUpgradeType" : self.promptUpgradeType,
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

        pos = self.View.getPosPairFromCursor( self.InputController.pollUserInput() )

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

  def promptUpgradeType(self, color):
    upgradeType = None
 
    while upgradeType is None:
      cursor = self.InputController.pollUserInput()
      upgradeType = self.View.promptUpgradeType( cursor )
      self.View.showUpgradeMenu( color )
      self.View.update()
      self.Clock.tick()
    self.View.removeUpgradeMenu()

    return upgradeType

  def updateView(self):
    self.View.display( self.Model.getBoard(), self.Model.getGame(), self.MoveController.getMoves( self.Model.getBoard() ), self.MoveController.getCurrPos() )
    self.View.update()

  def updateModel(self):
    self.MoveController.handleInput( self.Model.getBoard(), self.Model.getGame(), pos )
    self.Model.update()
