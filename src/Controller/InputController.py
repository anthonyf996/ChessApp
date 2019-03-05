from ExceptionHandler import ExceptionHandler

class InputController:
  def __init__(self, inputReader, exceptionHandler):
    self.InputReader = inputReader
    self.ExceptionHandler = exceptionHandler

  def pollUserInput(self):
    return self.ExceptionHandler.executeFunc()
