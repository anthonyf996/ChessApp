import unittest
import sys
sys.path.insert(0, "../../src/Model/")
from PieceColor import PieceColor
from Pon import Pon
from Knight import Knight
from Bishop import Bishop
from Rook import Rook
from Queen import Queen
from King import King
from Board import Board
from CastleLeftCommand import CastleLeftCommand
from CastleRightCommand import CastleRightCommand
from BoardOrientation import BoardOrientation
from BoardFromFile import BoardFromFile

class TestBoardFromFile(unittest.TestCase):
  def setUp(self):
    self.color = PieceColor.LIGHT
    self.otherColor = PieceColor.DARK
    self.board = Board( 8, 8 )

  def test_genBoard(self):
    BoardFromFile( self.board, "testFile.txt" ).setupBoard()
    for r in self.board.getBoard():
      for c in r:
        print( c, end="" )
        print( " ", end="" )
      print()

if __name__ == "__main__":
  unittest.main()
