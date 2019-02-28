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
from EatMove import EatMove
from MoveType import MoveType
from EnPassantCommand import EnPassantCommand
from CastleRightCommand import CastleRightCommand
from CastleLeftCommand import CastleLeftCommand

class TestBoard(unittest.TestCase):
  def setUp(self):
    self.color = PieceColor.LIGHT
    self.otherColor = PieceColor.DARK
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

  def test_isCollision(self):
    self.assertFalse( self.board.isCollision( ( 0, 0 ) ) )
    self.board.addPiece( ( 0, 0 ), Pon( self.color ) )
    self.assertTrue( self.board.isCollision( ( 0, 0 ) ) )

  def pairsToMoves(self, startPos, pairsSet ):
    moves = set()

    for p in pairsSet:
      moves.add( SimpleMove( self.board, startPos, p ) )

    return moves

  def pairsToEatMoves(self, startPos, pairsSet ):
    moves = set()

    for p in pairsSet:
      moves.add( EatMove( self.board, startPos, p ) )

    return moves

  def test_getMoves_Pon(self):
    startPos = ( 1, 1 )
    self.board.addPiece( startPos, Pon( self.otherColor ) ) 
    pairsSet = { ( 1, 2 ), ( 1, 3 ) }
    self.assertEqual( self.board.getMoves( startPos ), self.pairsToMoves( startPos, pairsSet ) )

  def test_getMoves_Pon_CanEnPassant(self):
    startPos = ( 1, 1 )
    self.board.addPiece( startPos, Pon( self.otherColor ) ) 
    self.board.getPiece( startPos ).setCanEnPassant( True )
    self.assertFalse( self.board.getMoves( startPos ) == self.pairsToMoves( startPos, { SimpleMove( self.board, ( 1, 1 ), ( 1, 2 ) ), SimpleMove( self.board, ( 1, 1 ), ( 1, 3 ) ) } ) )
    self.assertTrue( self.board.getMoves( startPos ) == self.pairsToMoves( startPos, { ( 1, 2 ), ( 1, 3 ), ( 2, 2 ), ( 0, 2 ) } ) )

  def test_getMoves_Knight(self):
    startPos = ( 2, 2 )
    self.board.addPiece( startPos, Knight( self.color ) ) 
    self.assertTrue( self.board.getMoves( startPos ) == self.pairsToMoves( startPos, { ( 1, 0 ), ( 0, 1 ), ( 4, 3 ), ( 3, 4 ), ( 3, 0 ), ( 1, 4 ), ( 0, 3 ), ( 4, 1 ) } ) )

  def test_getMoves_Bishop(self):
    startPos = ( 2, 2 )
    self.board.addPiece( startPos, Bishop( self.color, 8 ) ) 
    self.assertTrue( self.board.getMoves( startPos ) == self.pairsToMoves( startPos, { ( 0, 0 ), ( 1, 1 ), ( 3, 3 ), ( 4, 4 ), ( 5, 5 ), ( 6, 6 ), ( 7, 7 ), ( 1, 3 ), ( 0, 4 ), ( 3, 1 ), ( 4, 0 ) } ) )

  def test_getMoves_Rook(self):
    startPos = ( 2, 2 )
    self.board.addPiece( startPos, Rook( self.color, 8 ) ) 
    self.assertTrue( self.board.getMoves( startPos ) == self.pairsToMoves( startPos, { ( 2, 1 ), ( 2, 0 ), ( 2, 3 ), ( 2, 4 ), ( 2, 5 ), ( 2, 6 ), ( 2, 7 ), ( 1, 2 ), ( 0, 2 ), ( 3, 2 ), ( 4, 2 ), ( 5, 2 ), ( 6, 2 ), ( 7, 2 ) } ) )

  def test_getMoves_Queen(self):
    startPos = ( 2, 2 )
    self.board.addPiece( startPos, Queen( self.color, 8 ) ) 
    self.assertTrue( self.board.getMoves( startPos ) == self.pairsToMoves( startPos, { ( 0, 0 ), ( 1, 1 ), ( 3, 3 ), ( 4, 4 ), ( 5, 5 ), ( 6, 6 ), ( 7, 7 ), ( 1, 3 ), ( 0, 4 ), ( 3, 1 ), ( 4, 0 ), ( 2, 1 ), ( 2, 0 ), ( 2, 3 ), ( 2, 4 ), ( 2, 5 ), ( 2, 6 ), ( 2, 7 ), ( 1, 2 ), ( 0, 2 ), ( 3, 2 ), ( 4, 2 ), ( 5, 2 ), ( 6, 2 ), ( 7, 2 ) } ) )

  def test_getMoves_King(self):
    startPos = ( 2, 2 )
    self.board.addPiece( startPos, King( self.color ) ) 
    self.assertTrue( self.board.getMoves( startPos ) == self.pairsToMoves( startPos, { ( 1, 1 ), ( 3, 3 ), ( 1, 3 ), ( 3, 1 ), ( 2, 1 ), ( 1, 2 ), ( 3, 2 ), ( 2, 3 ) } ) )

  def test_getMoves_Bishop_Obstacle(self):
    startPos = ( 2, 2 )
    self.board.addPiece( startPos, Bishop( self.color, 8 ) ) 
    self.board.addPiece( ( 4, 4 ), Pon( self.color ) )
    self.assertTrue( self.board.getMoves( startPos ) == self.pairsToMoves( startPos, { ( 0, 0 ), ( 1, 1 ), ( 3, 3 ), ( 1, 3 ), ( 0, 4 ), ( 3, 1 ), ( 4, 0 ) } ) )

  def test_getMoves_Knight_Obstacle(self):
    startPos = ( 2, 2 )
    self.board.addPiece( startPos, Knight( self.color ) ) 
    self.board.addPiece( ( 1, 0 ), Pon( self.color ) )
    self.assertTrue( self.board.getMoves( startPos ) == self.pairsToMoves( startPos, { ( 0, 1 ), ( 4, 3 ), ( 3, 4 ), ( 3, 0 ), ( 1, 4 ), ( 0, 3 ), ( 4, 1 ) } ) )

  def test_move_Pon(self):
    pon = Pon( self.otherColor )
    self.assertFalse( pon.getHasMoved() )
    startPos = ( 1, 1 )
    self.board.addPiece( startPos, pon )
    self.assertTrue( self.board.getMoves( startPos ) == self.pairsToMoves( startPos, { ( 1, 2 ), ( 1, 3 ) } ) )
    self.board.move( SimpleMove( self.board, ( 1, 1 ), ( 1, 2 ) ) )
    startPos = ( 1, 2 )
    self.assertTrue( self.board.getMoves( startPos ) == self.pairsToMoves( startPos, { ( 1, 3 ) } ) )
    self.assertTrue( self.board.getPiece( ( 1, 1 ) ) == None )
    self.assertTrue( self.board.getPiece( ( 1, 2 ) ) == pon )
    self.assertTrue( self.board.getPiece( ( 1, 2 ) ).getHasMoved() )

  def test_getEatMoves_Pon(self):
    pon = Pon( self.otherColor )
    ponPos = ( 1, 1 )
    other = Pon( self.color )
    otherPos = ( 2, 2 )
    self.board.addPiece( ponPos, pon )
    self.assertEqual( self.board.getEatMoves( ponPos ), self.pairsToEatMoves( ponPos,  set() ) )
    self.board.addPiece( ( 1, 2 ), other )
    self.assertEqual( self.board.getEatMoves( ponPos ), self.pairsToEatMoves( ponPos,  set() ) )
    self.board.addPiece( otherPos, other )
    self.assertEqual( self.board.getEatMoves( ponPos ), self.pairsToEatMoves( ponPos,  { ( 2, 2 ) } ) )
    self.board.addPiece( ( 0, 2 ), Pon( self.color ) )
    self.board.addPiece( ( 0, 0 ), Pon( self.color ) )
    self.board.addPiece( ( 2, 0 ), Pon( self.color ) )
    self.assertEqual( self.board.getEatMoves( ponPos ), self.pairsToEatMoves( ponPos,  { ( 0, 2 ), ( 2, 2 ) } ) )

  def test_getEatMoves_Knight(self):
    knight = Knight( self.color )
    kPos = ( 2, 2 )
    self.board.addPiece( kPos, knight )
    self.assertEqual( self.board.getEatMoves( kPos ), self.pairsToEatMoves( kPos, set() ) )
    self.board.addPiece( ( 1, 1 ), Pon( self.otherColor ) )
    self.assertEqual( self.board.getEatMoves( kPos ), self.pairsToEatMoves( kPos, set() ) )
    self.board.addPiece( ( 1, 0 ), Pon( self.otherColor ) )
    self.assertEqual( self.board.getEatMoves( kPos ), self.pairsToEatMoves( kPos, { ( 1, 0 ) } ) )
    self.board.addPiece( ( 1, 4 ), Pon( self.otherColor ) )
    self.board.addPiece( ( 3, 0 ), Pon( self.otherColor ) )
    self.board.addPiece( ( 3, 4 ), Pon( self.otherColor ) )
    self.assertEqual( self.board.getEatMoves( kPos ), self.pairsToEatMoves( kPos, { ( 1, 0 ), ( 1, 4 ), ( 3, 0 ), ( 3, 4 ) } ) )

  def test_getEatMoves_Bishop(self):
    bishop = Bishop( self.color, 8 )
    pos = ( 2, 2 )
    self.board.addPiece( pos, bishop )
    self.assertEqual( self.board.getEatMoves( pos ), self.pairsToEatMoves( pos, set() ) )
    self.board.addPiece( ( 2, 0 ), Pon( self.otherColor ) )
    self.assertEqual( self.board.getEatMoves( pos ), self.pairsToEatMoves( pos, set() ) )
    self.board.addPiece( ( 3, 3 ), Pon( self.otherColor ) )
    self.board.addPiece( ( 1, 1 ), Pon( self.otherColor ) )
    self.board.addPiece( ( 1, 3 ), Pon( self.otherColor ) )
    self.board.addPiece( ( 4, 0 ), Pon( self.otherColor ) )
    self.board.addPiece( ( 5, 0 ), Pon( self.otherColor ) )
    self.assertEqual( self.board.getEatMoves( pos ), self.pairsToEatMoves( pos, { ( 3, 3 ), ( 1, 1 ), ( 1, 3 ), ( 4, 0 ) } ) )

  def test_getEatMoves_Rook(self):
    rook = Rook( self.color, 8 )
    pos = ( 2, 2 )
    self.board.addPiece( pos, rook )
    self.assertEqual( self.board.getEatMoves( pos ), self.pairsToEatMoves( pos, set() ) )
    self.board.addPiece( ( 3, 3 ), Pon( self.otherColor ) )
    self.assertEqual( self.board.getEatMoves( pos ), self.pairsToEatMoves( pos, set() ) )
    self.board.addPiece( ( 1, 1 ), Pon( self.otherColor ) )
    self.board.addPiece( ( 2, 0 ), Pon( self.otherColor ) )
    self.board.addPiece( ( 2, 1 ), Pon( self.otherColor ) )
    self.board.addPiece( ( 2, 7 ), Pon( self.otherColor ) )
    self.board.addPiece( ( 7, 2 ), Pon( self.otherColor ) )
    self.assertEqual( self.board.getEatMoves( pos ), self.pairsToEatMoves( pos, { ( 2, 1 ), ( 2, 7 ), ( 7, 2 ) } ) )

  def test_getEatMoves_Queen(self):
    queen = Queen( self.color, 8 )
    pos = ( 2, 2 )
    self.board.addPiece( pos, queen )
    self.assertEqual( self.board.getEatMoves( pos ), self.pairsToEatMoves( pos, set() ) )
    self.board.addPiece( ( 3, 4 ), Pon( self.otherColor ) )
    self.assertEqual( self.board.getEatMoves( pos ), self.pairsToEatMoves( pos, set() ) )
    self.board.addPiece( ( 2, 3 ), Pon( self.otherColor ) )
    self.board.addPiece( ( 2, 4 ), Pon( self.otherColor ) )
    self.board.addPiece( ( 2, 5 ), Pon( self.otherColor ) )
    self.board.addPiece( ( 2, 6 ), Pon( self.otherColor ) )
    self.board.addPiece( ( 4, 2 ), Pon( self.color ) )
    self.board.addPiece( ( 5, 2 ), Pon( self.otherColor ) )
    self.board.addPiece( ( 3, 3 ), Pon( self.otherColor ) )
    self.board.addPiece( ( 1, 3 ), Pon( self.otherColor ) )
    self.assertEqual( self.board.getEatMoves( pos ), self.pairsToEatMoves( pos, { ( 2, 3 ), ( 3, 3 ), ( 1, 3 ) } ) )

  def test_getEatMoves_King(self):
    king = King( self.color )
    pos = ( 2, 2 )
    self.board.addPiece( pos, king )
    self.assertEqual( self.board.getEatMoves( pos ), self.pairsToEatMoves( pos, set() ) )
    self.board.addPiece( ( 3, 4 ), Pon( self.otherColor ) )
    self.assertEqual( self.board.getEatMoves( pos ), self.pairsToEatMoves( pos, set() ) )
    self.board.addPiece( ( 2, 6 ), Pon( self.otherColor ) )
    self.assertEqual( self.board.getEatMoves( pos ), self.pairsToEatMoves( pos, set() ) )
    self.board.addPiece( ( 3, 3 ), Pon( self.otherColor ) )
    self.board.addPiece( ( 1, 2 ), Pon( self.otherColor ) )
    self.assertEqual( self.board.getEatMoves( pos ), self.pairsToEatMoves( pos, { ( 3, 3 ), ( 1, 2 ) } ) )

  def test_getSpecialMoves_Pon(self):
    pon = Pon( self.color )
    pos = ( 3, 3 )
    target = Pon( self.otherColor )
    targetPos = ( 2, 3 )

    self.board.addPiece( pos, pon )
    self.board.addPiece( targetPos, target )

    self.assertEqual( self.board.getSpecialMoves( pos ), set() )

    pon.setCanEnPassant( True )

    moves = self.board.getSpecialMoves( pos )

    self.assertEqual( len( moves ), 1 )
    for m in moves:
      self.assertEqual( ( pos, ( 2, 2 ) ), m.getPosPair() )

    target2 = Pon( self.otherColor )
    targetPos2 = ( 4, 3 )

    self.board.addPiece( targetPos2, target2 )

    moves = self.board.getSpecialMoves( pos )

    self.assertEqual( len( moves ), 2 )
    for m in moves:
      self.assertTrue( ( pos, ( 2, 2 ) ) == m.getPosPair() or \
                       ( pos, ( 4, 2 ) ) == m.getPosPair() )

  def castleRightCommand(self, color, kingPos, rookPos):
    king = King( color )
    rook = Rook( color )

    self.board.addPiece( kingPos, king )

    self.assertEqual( self.board.getSpecialMoves( kingPos ), set() )

    self.board.addPiece( rookPos, rook )
    
    moves = self.board.getSpecialMoves( kingPos )

    for m in moves:
      self.assertTrue( isinstance( m, CastleRightCommand ) )

    self.board.removePiece( rookPos )

    self.assertEqual( self.board.getSpecialMoves( kingPos ), set() )

  def castleLeftCommand(self, color, kingPos, rookPos):
    king = King( color )
    rook = Rook( color )

    self.board.addPiece( kingPos, king )

    self.assertEqual( self.board.getSpecialMoves( kingPos ), set() )

    self.board.addPiece( rookPos, rook )
    
    moves = self.board.getSpecialMoves( kingPos )

    for m in moves:
      self.assertTrue( isinstance( m, CastleLeftCommand ) )

    self.board.removePiece( rookPos )

    self.assertEqual( self.board.getSpecialMoves( kingPos ), set() )

  def test_getSpecialMoves_LightKing_Right(self):
    self.castleRightCommand( self.color, ( 4, 7 ), ( 7, 7 ) )

  def test_getSpecialMoves_DarkKing_Right(self):
    self.castleRightCommand( self.otherColor, ( 4, 0 ), ( 0, 0 ) )

  def test_getSpecialMoves_LightKing_Left(self):
    self.castleLeftCommand( self.color, ( 4, 7 ), ( 0, 7 ) )

  def test_getSpecialMoves_DarkKing_Left(self):
    self.castleLeftCommand( self.otherColor, ( 4, 0 ), ( 7, 0 ) )

if __name__ == "__main__":
  unittest.main()
