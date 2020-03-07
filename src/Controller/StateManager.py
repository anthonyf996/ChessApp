class StateManager:
  def __init__(self):
    self.states = {}
    self.currState = None
    self.prevState = None

  def getState(self, key):
    return self.states[ key ]

  def setState(self, key):
    self.prevState = self.currState
    self.currState = self.states[ key ]

  def setPriorState(self):
    if self.prevState is not None:
      self.currState = self.prevState

  def reset(self):
    raise NotImplementedError
