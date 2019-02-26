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

class TestBoard(unittest.TestCase):
  def setUp(self):
    self.color = PieceColor.LIGHT
    self.board = Board( 8, 8 )

  def test_Board(self):
    self.assertTrue( len( self.board.board ) == 8 )
    for i in range(0,8):
      self.assertTrue( len( self.board.board[i] ) == 8 )

  def test_addPiece(self):
    pon = Pon( self.color )
    self.board.addPiece( ( 1, 1 ), pon ) 
    self.assertTrue( self.board.getPiece( ( 1, 1 ) ) == pon )

  def test_getPiece(self):
    pon = Pon( self.color )
    self.board.addPiece( ( 1, 1 ), pon ) 
    self.assertTrue( self.board.getPiece( ( 1, 1 ) ) == pon )

  def test_removePiece(self):
    pon = Pon( self.color )
    self.board.addPiece( ( 1, 1 ), pon ) 
    self.board.removePiece( ( 1, 1 ) ) 
    self.assertTrue( self.board.getPiece( ( 1, 1 ) ) == None )

  def test_isValidMove(self):
    self.assertTrue( self.board.isValidMove( ( 0, 0 ) ) )
    self.assertTrue( self.board.isValidMove( ( 2, 3 ) ) )
    self.assertTrue( self.board.isValidMove( ( 7, 7 ) ) )
    self.assertFalse( self.board.isValidMove( ( 7, 8 ) ) )
    self.assertFalse( self.board.isValidMove( ( 8, 7 ) ) )
    self.assertFalse( self.board.isValidMove( ( -1, 7 ) ) )
    self.assertFalse( self.board.isValidMove( ( 1, -1 ) ) )
    self.board.addPiece( ( 0, 0 ), Pon( self.color ) )
    self.assertFalse( self.board.isValidMove( ( 0, 0 ) ) )

  def test_getMoves_Pon(self):
    self.board.addPiece( ( 1, 1 ), Pon( self.color ) ) 
    self.assertTrue( self.board.getMoves( ( 1, 1 ) ) == { ( 1, 2 ), ( 1, 3 ) } )

  def test_getMoves_Pon_CanEnPassant(self):
    self.board.addPiece( ( 1, 1 ), Pon( self.color ) ) 
    self.board.getPiece( ( 1, 1 ) ).setCanEnPassant( True )
    self.assertFalse( self.board.getMoves( ( 1, 1 ) ) == { ( 1, 2 ), ( 1, 3 ) } )
    self.assertTrue( self.board.getMoves( ( 1, 1 ) ) == { ( 1, 2 ), ( 1, 3 ), ( 2, 2 ), ( 0, 2 ) } )

  def test_getMoves_Knight(self):
    self.board.addPiece( ( 2, 2 ), Knight( self.color ) ) 
    self.assertTrue( self.board.getMoves( ( 2, 2 ) ) == { ( 1, 0 ), ( 0, 1 ), ( 4, 3 ), ( 3, 4 ), ( 3, 0 ), ( 1, 4 ), ( 0, 3 ), ( 4, 1 ) } )

  def test_getMoves_Bishop(self):
    self.board.addPiece( ( 2, 2 ), Bishop( self.color, 8 ) ) 
    self.assertTrue( self.board.getMoves( ( 2, 2 ) ) == { ( 0, 0 ), ( 1, 1 ), ( 3, 3 ), ( 4, 4 ), ( 5, 5 ), ( 6, 6 ), ( 7, 7 ), ( 1, 3 ), ( 0, 4 ), ( 3, 1 ), ( 4, 0 ) } )

  def test_getMoves_Rook(self):
    self.board.addPiece( ( 2, 2 ), Rook( self.color, 8 ) ) 
    self.assertTrue( self.board.getMoves( ( 2, 2 ) ) == { ( 2, 1 ), ( 2, 0 ), ( 2, 3 ), ( 2, 4 ), ( 2, 5 ), ( 2, 6 ), ( 2, 7 ), ( 1, 2 ), ( 0, 2 ), ( 3, 2 ), ( 4, 2 ), ( 5, 2 ), ( 6, 2 ), ( 7, 2 ) } )

  def test_getMoves_Queen(self):
    self.board.addPiece( ( 2, 2 ), Queen( self.color, 8 ) ) 
    self.assertTrue( self.board.getMoves( ( 2, 2 ) ) == { ( 0, 0 ), ( 1, 1 ), ( 3, 3 ), ( 4, 4 ), ( 5, 5 ), ( 6, 6 ), ( 7, 7 ), ( 1, 3 ), ( 0, 4 ), ( 3, 1 ), ( 4, 0 ), ( 2, 1 ), ( 2, 0 ), ( 2, 3 ), ( 2, 4 ), ( 2, 5 ), ( 2, 6 ), ( 2, 7 ), ( 1, 2 ), ( 0, 2 ), ( 3, 2 ), ( 4, 2 ), ( 5, 2 ), ( 6, 2 ), ( 7, 2 ) } )

  def test_getMoves_King(self):
    self.board.addPiece( ( 2, 2 ), King( self.color ) ) 
    self.assertTrue( self.board.getMoves( ( 2, 2 ) ) == { ( 1, 1 ), ( 3, 3 ), ( 1, 3 ), ( 3, 1 ), ( 2, 1 ), ( 1, 2 ), ( 3, 2 ), ( 2, 3 ) } )

  def test_getMoves_Bishop_Obstacle(self):
    self.board.addPiece( ( 2, 2 ), Bishop( self.color, 8 ) ) 
    self.board.addPiece( ( 4, 4 ), Pon( self.color ) )
    self.assertTrue( self.board.getMoves( ( 2, 2 ) ) == { ( 0, 0 ), ( 1, 1 ), ( 3, 3 ), ( 1, 3 ), ( 0, 4 ), ( 3, 1 ), ( 4, 0 ) } )

  def test_getMoves_Knight_Obstacle(self):
    self.board.addPiece( ( 2, 2 ), Knight( self.color ) ) 
    self.board.addPiece( ( 1, 0 ), Pon( self.color ) )
    self.assertTrue( self.board.getMoves( ( 2, 2 ) ) == { ( 0, 1 ), ( 4, 3 ), ( 3, 4 ), ( 3, 0 ), ( 1, 4 ), ( 0, 3 ), ( 4, 1 ) } )

  def test_move_Pon(self):
    pon = Pon( self.color )
    self.assertFalse( pon.getHasMoved() )
    self.board.addPiece( ( 1, 1 ), pon )
    self.assertTrue( self.board.getMoves( ( 1, 1 ) ) == { ( 1, 2 ), ( 1, 3 ) } )
    self.board.move( ( 1, 1 ), ( 1, 2 ) )
    self.assertTrue( self.board.getMoves( ( 1, 2 ) ) == { ( 1, 3 ) } )
    self.assertTrue( self.board.getPiece( ( 1, 1 ) ) == None )
    self.assertTrue( self.board.getPiece( ( 1, 2 ) ) == pon )
    self.assertTrue( self.board.getPiece( ( 1, 2 ) ).getHasMoved() )

if __name__ == "__main__":
  unittest.main()
