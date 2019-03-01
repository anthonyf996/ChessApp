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
from Game import Game
from GameRules import GameRules
from SimpleMove import SimpleMove

class TestCastle(unittest.TestCase):
  def setUp(self):
    self.color = PieceColor.LIGHT
    self.otherColor = PieceColor.DARK
    self.board = Board( 8, 8 )
    self.game = Game()
    self.rules = GameRules()

  def test_isInCheck(self):
    kingPos = ( 0, 4 )
    king = King( self.color )
    enemyPos = ( 2, 3 )
    enemy = Rook( self.otherColor )

    self.board.addPiece( kingPos, king )
    self.board.addPiece( enemyPos, enemy )

    self.assertFalse( self.rules.isInCheck( self.board, kingPos ) )
    self.board.move( SimpleMove( self.board, enemyPos, ( 2, 4 ) ) )
    self.assertTrue( self.rules.isInCheck( self.board, kingPos ) )
    self.board.move( SimpleMove( self.board, ( 2, 4 ), ( 2, 0 ) ) )
    self.assertFalse( self.rules.isInCheck( self.board, kingPos ) )

  def test_isInCheckMate(self):
    kingPos = ( 0, 4 )
    king = King( self.color )
    enemyPos = ( 2, 3 )
    enemy = Rook( self.otherColor )

    self.board.addPiece( kingPos, king )
    self.board.addPiece( enemyPos, enemy )

    self.assertFalse( self.rules.isInCheckMate( self.board, kingPos ) )
    self.board.move( SimpleMove( self.board, enemyPos, ( 2, 4 ) ) )
    self.assertFalse( self.rules.isInCheckMate( self.board, kingPos ) )
    self.board.move( SimpleMove( self.board, ( 2, 4 ), ( 2, 0 ) ) )
    self.assertFalse( self.rules.isInCheckMate( self.board, kingPos ) )
    self.board.move( SimpleMove( self.board, ( 2, 0 ), ( 0, 0 ) ) )
    self.board.move( SimpleMove( self.board, ( 0, 0 ), ( 0, 3 ) ) )
    self.assertFalse( self.rules.isInCheckMate( self.board, kingPos ) )

    self.board.addPiece( ( 1, 3 ), Queen( self.otherColor ) )

    self.assertTrue( self.rules.isInCheck( self.board, kingPos ) )
    self.assertTrue( self.rules.isInCheckMate( self.board, kingPos ) )

    self.board.move( SimpleMove( self.board, ( 1, 3 ), ( 1, 1 ) ) )

    self.assertTrue( self.rules.isInCheck( self.board, kingPos ) )
    self.assertFalse( self.rules.isInCheckMate( self.board, kingPos ) )

  def test_isDraw(self):
    kingPos = ( 0, 4 )
    king = King( self.color )
    enemyPos = ( 2, 3 )
    enemy = Rook( self.otherColor )

    self.board.addPiece( kingPos, king )
    self.board.addPiece( enemyPos, enemy )
    kingPos2 = ( 7, 0 )
    self.board.addPiece( kingPos2, King( self.otherColor ) )

    self.assertFalse( self.rules.isDraw( self.board, self.game, kingPos, kingPos2 ) )

    self.board.addPiece( ( 1, 6 ), Queen( self.otherColor ) )

    self.assertTrue( self.rules.isDraw( self.board, self.game, kingPos, kingPos2 ) )
    self.assertFalse( self.rules.isInCheck( self.board, kingPos ) )
    self.assertFalse( self.rules.isInCheckMate( self.board, kingPos ) )

    self.board.addPiece( ( 7, 7 ), Rook( self.color ) )

    self.assertFalse( self.rules.isDraw( self.board, self.game, kingPos, kingPos2 ) )
    self.assertFalse( self.rules.isInCheck( self.board, kingPos ) )
    self.assertFalse( self.rules.isInCheckMate( self.board, kingPos ) )

    self.game.turnCount = 100

    self.assertTrue( self.rules.isDraw( self.board, self.game, kingPos, kingPos2 ) )
    self.assertFalse( self.rules.isInCheck( self.board, kingPos ) )
    self.assertFalse( self.rules.isInCheckMate( self.board, kingPos ) )

if __name__ == "__main__":
  unittest.main()
