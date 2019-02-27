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
from SimpleMove import SimpleMove

class TestBoard(unittest.TestCase):
  def setUp(self):
    self.color = PieceColor.LIGHT
    self.otherColor = PieceColor.DARK
    self.board = Board( 8, 8 )

  def test_SimpleMove_Pon(self):
    pon = Pon( self.color )
    self.board.addPiece( ( 2, 2 ), pon )
    self.board.move( SimpleMove( self.board, ( 2, 2 ), ( 3, 3 ) ) )
    self.assertEqual( self.board.getPiece( ( 3, 3 ) ), pon )
    self.assertEqual( self.board.getPiece( ( 2, 2 ) ), None )

  def test_SimpleMove_Pon_undo(self):
    pon = Pon( self.color )
    self.board.addPiece( ( 2, 2 ), pon )
    self.assertFalse( pon.getHasMoved() )
    move = SimpleMove( self.board, ( 2, 2 ), ( 3, 3 ) )
    self.board.move( move )
    self.assertTrue( pon.getHasMoved() )
    self.assertEqual( self.board.getPiece( ( 3, 3 ) ), pon )
    self.assertEqual( self.board.getPiece( ( 2, 2 ) ), None )
    self.board.undo( move )
    self.assertEqual( self.board.getPiece( ( 2, 2 ) ), pon )
    self.assertEqual( self.board.getPiece( ( 3, 3 ) ), None )
    self.assertFalse( pon.getHasMoved() )

if __name__ == "__main__":
  unittest.main()
