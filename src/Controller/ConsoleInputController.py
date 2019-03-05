from InputController import InputController
from ExceptionHandler import ExceptionHandler
#from ConsoleInputReader import ConsoleInputReader
#from GameResetException import GameResetException

class ConsoleInputController(InputController):
  def __init__(self, inputReader, exceptionHandler):
    self.InputReader = inputReader
    self.ExceptionHandler = exceptionHandler

  def pollUserInput(self):
    return self.ExceptionHandler.executeFunc()
