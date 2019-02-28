import logging
from Board import Board

class Model:
  def __init__(self):
    self.board = Board( 8, 8 )

  def getBoard(self):
    return self.board
