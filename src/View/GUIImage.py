import pygame
from Image import Image

class GUIImage(Image):
  def __init__(self, name):
    super().__init__(name)
    self.img = self.register()

  def register(self):
    return pygame.image.load( self.name )

  def getImg(self):
    return self.img
