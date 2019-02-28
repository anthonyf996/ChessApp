from Clock import Clock
from time import sleep

class ConsoleClock(Clock):
  def tick(self, fpsKey = "FPS" ):
    sleep( self.getSeconds( self.fpsSpec[ fpsKey ] ) )

  def getSeconds(self, fps):
    return 1 / fps
