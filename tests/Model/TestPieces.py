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

class TestPieces(unittest.TestCase):
  def setUp(self):
    self.color = PieceColor.LIGHT

  def test_Pon(self):
    pon = Pon( self.color )

  def test_Knight(self):
    pon = Knight( self.color )

  def test_Bishop(self):
    pon = Bishop( self.color, 8 )

  def test_Rook(self):
    pon = Rook( self.color, 8 )

  def test_Queen(self):
    pon = Queen( self.color, 8 )

  def test_King(self):
    pon = King( self.color )

if __name__ == "__main__":
  unittest.main()
