class HintManager:
  def __init__(self, Game, AI):
    self.Game = Game
    self.AI = AI
    self.currHint = None

  def toggleHint(self):
    if self.currHint is None:
      self.currHint = self.AI.getMove( self.Game.getTurnColor() )
    else:
      self.clearHint()

  def getHint(self):
    return self.currHint

  def clearHint(self):
    self.currHint = None
