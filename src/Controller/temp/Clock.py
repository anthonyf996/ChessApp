class Clock:
  def __init__(self, fpsSpec):
    self.fpsSpec = fpsSpec

  def tick(self):
    raise NotImplementedError
