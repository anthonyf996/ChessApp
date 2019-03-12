class ControllerFactory:
  def __init__(self):
    pass

  def createView(self):
    raise NotImplementedError

  def createModel(self):
    raise NotImplementedError

  def createClock(self):
    raise NotImplementedError

  def createInputReader(self):
    raise NotImplementedError

  def createMoveController(self):
    raise NotImplementedError

  def createAI(self):
    raise NotImplementedError

  def createControllerStateManager(self):
    raise NotImplementedError
