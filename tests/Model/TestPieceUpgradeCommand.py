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
from PieceColor import PieceColor
from PieceType import PieceType
from PieceUpgradeCommand import PieceUpgradeCommand

class TestPieceUpgradeCommand(unittest.TestCase):
  def setUp(self):
    self.color = PieceColor.LIGHT
    self.otherColor = PieceColor.DARK
    self.board = Board( 8, 8 )

  def upgrade(self, upgradeType, upgradePiece):
    pon = Pon( self.color )
    currPiecePos = ( 6, 0 )

    self.assertEqual( self.board.getPiece( currPiecePos ), None )

    self.board.addPiece( currPiecePos, pon )

    self.assertEqual( self.board.getPiece( currPiecePos ), pon )

    move = PieceUpgradeCommand( self.board, currPiecePos, upgradeType )

    self.board.move( move )

    self.assertEqual( type( self.board.getPiece( currPiecePos ) ), type( upgradePiece ) )

  def upgradeUndo(self, upgradeType, upgradePiece):
    pon = Pon( self.color )
    currPiecePos = ( 6, 0 )

    self.assertEqual( self.board.getPiece( currPiecePos ), None )

    self.board.addPiece( currPiecePos, pon )

    self.assertEqual( self.board.getPiece( currPiecePos ), pon )

    move = PieceUpgradeCommand( self.board, currPiecePos, upgradeType )

    self.board.move( move )

    self.assertEqual( type( self.board.getPiece( currPiecePos ) ), type( upgradePiece ) )

    self.board.undo( move )

    self.assertEqual( self.board.getPiece( currPiecePos ), pon )

  def test_PieceUpgradeCommand_Knight(self):
    upgradeType = PieceType.KNIGHT
    upgradePiece = Knight( self.color )
    self.upgrade( upgradeType, upgradePiece )

  def test_PieceUpgradeCommand_Knight_undo(self):
    upgradeType = PieceType.KNIGHT
    upgradePiece = Knight( self.color )
    self.upgradeUndo( upgradeType, upgradePiece )

  def test_PieceUpgradeCommand_Bishop(self):
    upgradeType = PieceType.BISHOP
    upgradePiece = Bishop( self.color )
    self.upgrade( upgradeType, upgradePiece )

  def test_PieceUpgradeCommand_Bishop_undo(self):
    upgradeType = PieceType.BISHOP
    upgradePiece = Bishop( self.color )
    self.upgradeUndo( upgradeType, upgradePiece )

  def test_PieceUpgradeCommand_Rook(self):
    upgradeType = PieceType.ROOK
    upgradePiece = Rook( self.color )
    self.upgrade( upgradeType, upgradePiece )

  def test_PieceUpgradeCommand_Rook_undo(self):
    upgradeType = PieceType.ROOK
    upgradePiece = Rook( self.color )
    self.upgradeUndo( upgradeType, upgradePiece )

  def test_PieceUpgradeCommand_Queen(self):
    upgradeType = PieceType.QUEEN
    upgradePiece = Queen( self.color )
    self.upgrade( upgradeType, upgradePiece )

  def test_PieceUpgradeCommand_Queen_undo(self):
    upgradeType = PieceType.QUEEN
    upgradePiece = Queen( self.color )
    self.upgradeUndo( upgradeType, upgradePiece )

if __name__ == "__main__":
  unittest.main()
