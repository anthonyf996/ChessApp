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
from EnPassantCommand import EnPassantCommand
from BoardOrientation import BoardOrientation
from PieceColor import PieceColor
from SetEnPassantCommand import SetEnPassantCommand

class TestSetEnPassant(unittest.TestCase):
  def setUp(self):
    self.color = PieceColor.LIGHT
    self.otherColor = PieceColor.DARK
    self.board = Board( 8, 8 )

  def test_SetEnPassant(self):
    pon = Pon( self.color )
    pon2 = Pon( self.otherColor )
    pon3 = Pon( self.otherColor )
    self.board.addPiece( ( 1, 1 ), pon )
    self.board.addPiece( ( 0, 1 ), pon2 )
    self.board.addPiece( ( 2, 1 ), pon3 )
    self.assertFalse( pon2.getCanEnPassant() )
    self.assertFalse( pon3.getCanEnPassant() )
    setEnPassant = SetEnPassantCommand( self.board, pon.getPos() )
    setEnPassant.execute()
    self.assertTrue( pon2.getCanEnPassant() )
    self.assertTrue( pon3.getCanEnPassant() )
    setEnPassant.undo()
    self.assertFalse( pon2.getCanEnPassant() )
    self.assertFalse( pon3.getCanEnPassant() )

if __name__ == "__main__":
  unittest.main()
