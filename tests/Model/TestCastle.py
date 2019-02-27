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

class TestBoard(unittest.TestCase):
  def setUp(self):
    self.color = PieceColor.LIGHT
    self.otherColor = PieceColor.DARK

  def castle(self, board, move, kingStartPos, kingEndPos, rookStartPos, rookEndPos):
    king = King( self.color )
    rook = Rook( self.color, 8 )

    board.addPiece( kingStartPos, king )
    board.addPiece( rookStartPos, rook )

    self.assertFalse( king.getHasMoved() )
    self.assertFalse( rook.getHasMoved() )

    self.assertEqual( board.getPiece( kingStartPos ), king )
    self.assertEqual( board.getPiece( rookStartPos ), rook )
    self.assertEqual( board.getPiece( kingEndPos ), None )
    self.assertEqual( board.getPiece( rookEndPos ), None )

    board.move( move )

    self.assertTrue( king.getHasMoved() )
    self.assertTrue( rook.getHasMoved() )

    self.assertEqual( board.getPiece( kingStartPos ), None )
    self.assertEqual( board.getPiece( rookStartPos ), None )
    self.assertEqual( board.getPiece( kingEndPos ), king )
    self.assertEqual( board.getPiece( rookEndPos ), rook )

  def castleUndo(self, board, move, kingStartPos, kingEndPos, rookStartPos, rookEndPos):
    king = King( self.color )
    rook = Rook( self.color, 8 )

    board.addPiece( kingStartPos, king )
    board.addPiece( rookStartPos, rook )

    self.assertFalse( king.getHasMoved() )
    self.assertFalse( rook.getHasMoved() )

    self.assertEqual( board.getPiece( kingStartPos ), king )
    self.assertEqual( board.getPiece( rookStartPos ), rook )
    self.assertEqual( board.getPiece( kingEndPos ), None )
    self.assertEqual( board.getPiece( rookEndPos ), None )

    board.move( move )

    self.assertTrue( king.getHasMoved() )
    self.assertTrue( rook.getHasMoved() )

    self.assertEqual( board.getPiece( kingStartPos ), None )
    self.assertEqual( board.getPiece( rookStartPos ), None )
    self.assertEqual( board.getPiece( kingEndPos ), king )
    self.assertEqual( board.getPiece( rookEndPos ), rook )

    board.undo( move )

    self.assertFalse( king.getHasMoved() )
    self.assertFalse( rook.getHasMoved() )

    self.assertEqual( board.getPiece( kingStartPos ), king )
    self.assertEqual( board.getPiece( rookStartPos ), rook )
    self.assertEqual( board.getPiece( kingEndPos ), None )
    self.assertEqual( board.getPiece( rookEndPos ), None )

  def test_CastleLeft_LightTileRight(self):
    board = Board( 8, 8, orientation = BoardOrientation.LIGHT_TILE_RIGHT )
    kingStartPos, kingEndPos = ( 4, 7 ), ( 2, 7 )
    rookStartPos, rookEndPos = ( 0, 7 ), ( 3, 7 )

    self.castle( board, CastleLeftCommand( board, kingStartPos ), kingStartPos, kingEndPos, rookStartPos, rookEndPos )

  def test_CastleLeft_LightTileRight_undo(self):
    board = Board( 8, 8, orientation = BoardOrientation.LIGHT_TILE_RIGHT )
    kingStartPos, kingEndPos = ( 4, 7 ), ( 2, 7 )
    rookStartPos, rookEndPos = ( 0, 7 ), ( 3, 7 )

    self.castleUndo( board, CastleLeftCommand( board, kingStartPos ), kingStartPos, kingEndPos, rookStartPos, rookEndPos )

  def test_CastleLeft_DarkTileRight(self):
    board = Board( 8, 8, orientation = BoardOrientation.DARK_TILE_RIGHT )
    kingStartPos, kingEndPos = ( 4, 0 ), ( 6, 0 )
    rookStartPos, rookEndPos = ( 7, 0 ), ( 5, 0 )

    self.castle( board, CastleLeftCommand( board, kingStartPos ), kingStartPos, kingEndPos, rookStartPos, rookEndPos )

  def test_CastleLeft_DarkTileRight_undo(self):
    board = Board( 8, 8, orientation = BoardOrientation.DARK_TILE_RIGHT )
    kingStartPos, kingEndPos = ( 4, 0 ), ( 6, 0 )
    rookStartPos, rookEndPos = ( 7, 0 ), ( 5, 0 )

    self.castleUndo( board, CastleLeftCommand( board, kingStartPos ), kingStartPos, kingEndPos, rookStartPos, rookEndPos )

  def test_CastleRight_LightTileRight(self):
    board = Board( 8, 8, orientation = BoardOrientation.LIGHT_TILE_RIGHT )
    kingStartPos, kingEndPos = ( 4, 7 ), ( 6, 7 )
    rookStartPos, rookEndPos = ( 7, 7 ), ( 5, 7 )

    self.castle( board, CastleRightCommand( board, kingStartPos ), kingStartPos, kingEndPos, rookStartPos, rookEndPos )

  def test_CastleRight_LightTileRight_undo(self):
    board = Board( 8, 8, orientation = BoardOrientation.LIGHT_TILE_RIGHT )
    kingStartPos, kingEndPos = ( 4, 7 ), ( 6, 7 )
    rookStartPos, rookEndPos = ( 7, 7 ), ( 5, 7 )

    self.castleUndo( board, CastleRightCommand( board, kingStartPos ), kingStartPos, kingEndPos, rookStartPos, rookEndPos )

  def test_CastleRight_DarkTileRight(self):
    board = Board( 8, 8, orientation = BoardOrientation.DARK_TILE_RIGHT )
    kingStartPos, kingEndPos = ( 4, 0 ), ( 2, 0 )
    rookStartPos, rookEndPos = ( 0, 0 ), ( 3, 0 )

    self.castle( board, CastleRightCommand( board, kingStartPos ), kingStartPos, kingEndPos, rookStartPos, rookEndPos )

  def test_CastleRight_DarkTileRight_undo(self):
    board = Board( 8, 8, orientation = BoardOrientation.DARK_TILE_RIGHT )
    kingStartPos, kingEndPos = ( 4, 0 ), ( 2, 0 )
    rookStartPos, rookEndPos = ( 0, 0 ), ( 3, 0 )

    self.castleUndo( board, CastleRightCommand( board, kingStartPos ), kingStartPos, kingEndPos, rookStartPos, rookEndPos )

if __name__ == "__main__":
  unittest.main()
