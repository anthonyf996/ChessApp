class Image:
  def __init__(self, name):
    self.name = name

  def register(self):
    raise NotImplementedError

  def getImg(self):
    raise NotImplementedError
