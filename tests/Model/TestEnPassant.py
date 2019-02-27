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

class TestBoard(unittest.TestCase):
  def setUp(self):
    self.color = PieceColor.LIGHT
    self.otherColor = PieceColor.DARK

  def enPassantCommand(self, color, otherColor, ponStartPos, ponEndPos, targetStartPos):
    board = Board( 8, 8 )
    pon = Pon( color )
    target = Pon( otherColor )

    board.addPiece( ponStartPos, pon )
    board.addPiece( targetStartPos, target )

    self.assertEqual( board.getPiece( ponStartPos ), pon )
    self.assertEqual( board.getPiece( ponEndPos ), None )
    self.assertEqual( board.getPiece( targetStartPos ), target )

    move = EnPassantCommand( board, ponStartPos, targetStartPos )
    board.move( move )

    self.assertEqual( board.getPiece( ponStartPos ), None )
    self.assertEqual( board.getPiece( ponEndPos ), pon )
    self.assertEqual( board.getPiece( targetStartPos ), None )

  def enPassantCommandUndo(self, color, otherColor, ponStartPos, ponEndPos, targetStartPos):
    board = Board( 8, 8 )
    pon = Pon( color )
    target = Pon( otherColor )

    board.addPiece( ponStartPos, pon )
    board.addPiece( targetStartPos, target )

    self.assertEqual( board.getPiece( ponStartPos ), pon )
    self.assertEqual( board.getPiece( ponEndPos ), None )
    self.assertEqual( board.getPiece( targetStartPos ), target )

    move = EnPassantCommand( board, ponStartPos, targetStartPos )
    board.move( move )

    self.assertEqual( board.getPiece( ponStartPos ), None )
    self.assertEqual( board.getPiece( ponEndPos ), pon )
    self.assertEqual( board.getPiece( targetStartPos ), None )

    board.undo( move )

    self.assertEqual( board.getPiece( ponStartPos ), pon )
    self.assertEqual( board.getPiece( ponEndPos ), None )
    self.assertEqual( board.getPiece( targetStartPos ), target )

  def test_EnPassantCommand_LightPiece_Left(self):
    color = PieceColor.LIGHT
    otherColor = PieceColor.DARK
    ponStartPos = ( 3, 3 )
    ponEndPos = ( 2, 2 )
    targetStartPos = ( 2, 3 )
    self.enPassantCommand( color, otherColor, ponStartPos, ponEndPos, targetStartPos )
    self.enPassantCommandUndo( color, otherColor, ponStartPos, ponEndPos, targetStartPos )

  def test_EnPassantCommand_LightPiece_Right(self):
    color = PieceColor.LIGHT
    otherColor = PieceColor.DARK
    ponStartPos = ( 3, 3 )
    ponEndPos = ( 4, 2 )
    targetStartPos = ( 4, 3 )
    self.enPassantCommand( color, otherColor, ponStartPos, ponEndPos, targetStartPos )
    self.enPassantCommandUndo( color, otherColor, ponStartPos, ponEndPos, targetStartPos )

  def test_EnPassantCommand_DarkPiece_Left(self):
    color = PieceColor.DARK
    otherColor = PieceColor.LIGHT
    ponStartPos = ( 3, 4 )
    ponEndPos = ( 2, 5 )
    targetStartPos = ( 2, 4 )
    self.enPassantCommand( color, otherColor, ponStartPos, ponEndPos, targetStartPos )
    self.enPassantCommandUndo( color, otherColor, ponStartPos, ponEndPos, targetStartPos )

  def test_EnPassantCommand_DarkPiece_Right(self):
    color = PieceColor.DARK
    otherColor = PieceColor.LIGHT
    ponStartPos = ( 3, 4 )
    ponEndPos = ( 4, 5 )
    targetStartPos = ( 4, 4 )
    self.enPassantCommand( color, otherColor, ponStartPos, ponEndPos, targetStartPos )
    self.enPassantCommandUndo( color, otherColor, ponStartPos, ponEndPos, targetStartPos )

if __name__ == "__main__":
  unittest.main()
