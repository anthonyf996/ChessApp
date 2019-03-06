import logging
from Board import Board
from Game import Game
from GameRules import GameRules

class Model:
  def __init__(self, boardconfigFileName = ""):
    self.board = Board( 8, 8, boardconfigFileName )
    self.Game = Game()
    self.GameRules = GameRules()

  def getBoard(self):
    return self.board

  def getGameRules(self):
    return self.GameRules

  def getGame(self):
    return self.Game

  def update(self):
    self.Game.update( self.board, self.Game, self.GameRules )
