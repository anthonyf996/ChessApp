from InputController import InputController
from ExceptionHandler import ExceptionHandler
from ConsoleInputReader import ConsoleInputReader

class ConsoleInputController(InputController):
  def __init__(self, inputReader):
    self.InputReader = inputReader
    self.ExceptionHandler = ExceptionHandler( self.InputReader.read )

  def pollUserInput(self):
    return self.ExceptionHandler.executeFunc()
