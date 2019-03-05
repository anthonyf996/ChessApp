from Clock import Clock
import pygame

class GUIClock(Clock):
  def __init__(self, fpsSpec):
    super().__init__(fpsSpec)
    self.Clock = pygame.time.Clock()

  def tick(self, fpsKey = "FPS" ):
    self.Clock.tick( self.fpsSpec[ fpsKey ] )
