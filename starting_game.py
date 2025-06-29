from case import chessboard
from piece import *


def position_starting_game(screen): #fonction de blitt de toutes les positions de départ et prise des caracteristiques pour chaque case
    chessboard[0][0].piece = W_rook
    chessboard[0][0].color = chessboard[0][0].piece.color
    chessboard[0][0].surface.blit(chessboard[0][0].piece.get_sprite(), (0, 0))
    screen.blit(chessboard[0][0].surface, chessboard[0][0].get_pos())
    chessboard[0][1].piece = W_pawn
    chessboard[0][1].color = chessboard[0][1].piece.color
    chessboard[0][1].surface.blit(chessboard[0][1].piece.get_sprite(), (0, 0))
    screen.blit(chessboard[0][1].surface, chessboard[0][1].get_pos())
    chessboard[0][6].piece = B_pawn
    chessboard[0][6].color = chessboard[0][6].piece.color
    chessboard[0][6].surface.blit(chessboard[0][6].piece.get_sprite(), (0, 0))
    screen.blit(chessboard[0][6].surface, chessboard[0][6].get_pos())
    chessboard[0][7].piece = B_rook
    chessboard[0][7].color = chessboard[0][7].piece.color
    chessboard[0][7].surface.blit(chessboard[0][7].piece.get_sprite(), (0, 0))
    screen.blit(chessboard[0][7].surface, chessboard[0][7].get_pos())

    chessboard[1][0].piece = W_knight
    chessboard[1][0].color = chessboard[1][0].piece.color
    chessboard[1][0].surface.blit(chessboard[1][0].piece.get_sprite(), (0, 0))
    screen.blit(chessboard[1][0].surface, chessboard[1][0].get_pos())
    chessboard[1][1].piece = W_pawn
    chessboard[1][1].color = chessboard[1][1].piece.color
    chessboard[1][1].surface.blit(chessboard[1][1].piece.get_sprite(), (0, 0))
    screen.blit(chessboard[1][1].surface, chessboard[1][1].get_pos())
    chessboard[1][6].piece = B_pawn
    chessboard[1][6].color = chessboard[1][6].piece.color
    chessboard[1][6].surface.blit(chessboard[1][6].piece.get_sprite(), (0, 0))
    screen.blit(chessboard[1][6].surface, chessboard[1][6].get_pos())
    chessboard[1][7].piece = B_knight
    chessboard[1][7].color = chessboard[1][7].piece.color
    chessboard[1][7].surface.blit(chessboard[1][7].piece.get_sprite(), (0, 0))
    screen.blit(chessboard[1][7].surface, chessboard[1][7].get_pos())

    chessboard[2][0].piece = W_bishop
    chessboard[2][0].color = chessboard[2][0].piece.color
    chessboard[2][0].surface.blit(chessboard[2][0].piece.get_sprite(), (0, 0))
    screen.blit(chessboard[2][0].surface, chessboard[2][0].get_pos())
    chessboard[2][1].piece = W_pawn
    chessboard[2][1].color = chessboard[2][1].piece.color
    chessboard[2][1].surface.blit(chessboard[2][1].piece.get_sprite(), (0, 0))
    screen.blit(chessboard[2][1].surface, chessboard[2][1].get_pos())
    chessboard[2][6].piece = B_pawn
    chessboard[2][6].color = chessboard[2][6].piece.color
    chessboard[2][6].surface.blit(chessboard[2][6].piece.get_sprite(), (0, 0))
    screen.blit(chessboard[2][6].surface, chessboard[2][6].get_pos())
    chessboard[2][7].piece = B_bishop
    chessboard[2][7].color = chessboard[2][7].piece.color
    chessboard[2][7].surface.blit(chessboard[2][7].piece.get_sprite(), (0, 0))
    screen.blit(chessboard[2][7].surface, chessboard[2][7].get_pos())

    chessboard[3][0].piece = W_queen
    chessboard[3][0].color = chessboard[3][0].piece.color
    chessboard[3][0].surface.blit(chessboard[3][0].piece.get_sprite(), (0, 0))
    screen.blit(chessboard[3][0].surface, chessboard[3][0].get_pos())
    chessboard[3][1].piece = W_pawn
    chessboard[3][1].color = chessboard[3][1].piece.color
    chessboard[3][1].surface.blit(chessboard[3][1].piece.get_sprite(), (0, 0))
    screen.blit(chessboard[3][1].surface, chessboard[3][1].get_pos())
    chessboard[3][6].piece = B_pawn
    chessboard[3][6].color = chessboard[3][6].piece.color
    chessboard[3][6].surface.blit(chessboard[3][6].piece.get_sprite(), (0, 0))
    screen.blit(chessboard[3][6].surface, chessboard[3][6].get_pos())
    chessboard[3][7].piece = B_queen
    chessboard[3][7].color = chessboard[3][7].piece.color
    chessboard[3][7].surface.blit(chessboard[3][7].piece.get_sprite(), (0, 0))
    screen.blit(chessboard[3][7].surface, chessboard[3][7].get_pos())

    chessboard[4][0].piece = W_king
    chessboard[4][0].color = chessboard[4][0].piece.color
    chessboard[4][0].surface.blit(chessboard[4][0].piece.get_sprite(), (0, 0))
    screen.blit(chessboard[4][0].surface, chessboard[4][0].get_pos())
    chessboard[4][1].piece = W_pawn
    chessboard[4][1].color = chessboard[4][1].piece.color
    chessboard[4][1].surface.blit(chessboard[4][1].piece.get_sprite(), (0, 0))
    screen.blit(chessboard[4][1].surface, chessboard[4][1].get_pos())
    chessboard[4][6].piece = B_pawn
    chessboard[4][6].color = chessboard[4][6].piece.color
    chessboard[4][6].surface.blit(chessboard[4][6].piece.get_sprite(), (0, 0))
    screen.blit(chessboard[4][6].surface, chessboard[4][6].get_pos())
    chessboard[4][7].piece = B_king
    chessboard[4][7].color = chessboard[4][7].piece.color
    chessboard[4][7].surface.blit(chessboard[4][7].piece.get_sprite(), (0, 0))
    screen.blit(chessboard[4][7].surface, chessboard[4][7].get_pos())

    chessboard[5][0].piece = W_bishop
    chessboard[5][0].color = chessboard[5][0].piece.color
    chessboard[5][0].surface.blit(chessboard[5][0].piece.get_sprite(), (0, 0))
    screen.blit(chessboard[5][0].surface, chessboard[5][0].get_pos())
    chessboard[5][1].piece = W_pawn
    chessboard[5][1].color = chessboard[5][1].piece.color
    chessboard[5][1].surface.blit(chessboard[5][1].piece.get_sprite(), (0, 0))
    screen.blit(chessboard[5][1].surface, chessboard[5][1].get_pos())
    chessboard[5][6].piece = B_pawn
    chessboard[5][6].color = chessboard[5][6].piece.color
    chessboard[5][6].surface.blit(chessboard[5][6].piece.get_sprite(), (0, 0))
    screen.blit(chessboard[5][6].surface, chessboard[5][6].get_pos())
    chessboard[5][7].piece = B_bishop
    chessboard[5][7].color = chessboard[5][7].piece.color
    chessboard[5][7].surface.blit(chessboard[5][7].piece.get_sprite(), (0, 0))
    screen.blit(chessboard[5][7].surface, chessboard[5][7].get_pos())

    chessboard[6][0].piece = W_knight
    chessboard[6][0].color = chessboard[0][0].piece.color
    chessboard[6][0].surface.blit(chessboard[6][0].piece.get_sprite(), (0, 0))
    screen.blit(chessboard[6][0].surface, chessboard[6][0].get_pos())
    chessboard[6][1].piece = W_pawn
    chessboard[6][1].color = chessboard[6][1].piece.color
    chessboard[6][1].surface.blit(chessboard[6][1].piece.get_sprite(), (0, 0))
    screen.blit(chessboard[6][1].surface, chessboard[6][1].get_pos())
    chessboard[6][6].piece = B_pawn
    chessboard[6][6].color = chessboard[6][6].piece.color
    chessboard[6][6].surface.blit(chessboard[6][6].piece.get_sprite(), (0, 0))
    screen.blit(chessboard[6][6].surface, chessboard[6][6].get_pos())
    chessboard[6][7].piece = B_knight
    chessboard[6][7].color = chessboard[6][7].piece.color
    chessboard[6][7].surface.blit(chessboard[6][7].piece.get_sprite(), (0, 0))
    screen.blit(chessboard[6][7].surface, chessboard[6][7].get_pos())

    chessboard[7][0].piece = W_rook
    chessboard[7][0].color = chessboard[7][0].piece.color
    chessboard[7][0].surface.blit(chessboard[7][0].piece.get_sprite(), (0, 0))
    screen.blit(chessboard[7][0].surface, chessboard[7][0].get_pos())
    chessboard[7][1].piece = W_pawn
    chessboard[7][1].color = chessboard[7][1].piece.color
    chessboard[7][1].surface.blit(chessboard[7][1].piece.get_sprite(), (0, 0))
    screen.blit(chessboard[7][1].surface, chessboard[7][1].get_pos())
    chessboard[7][6].piece = B_pawn
    chessboard[7][6].color = chessboard[7][6].piece.color
    chessboard[7][6].surface.blit(chessboard[7][6].piece.get_sprite(), (0, 0))
    screen.blit(chessboard[7][6].surface, chessboard[7][6].get_pos())
    chessboard[7][7].piece = B_rook
    chessboard[7][7].color = chessboard[7][7].piece.color
    chessboard[7][7].surface.blit(chessboard[7][7].piece.get_sprite(), (0, 0))
    screen.blit(chessboard[7][7].surface, chessboard[7][7].get_pos())


