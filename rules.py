import pygame
from case import chessboard

def is_castling(color,start_tab64):
    castling_long = None
    castling_little = None
    if color == "white":
        if chessboard[0][0].play_once == 0: #si tour grand roque a pas bougé
            castling_long = start_tab64 - 2 #alors ajout vecteur directionnel dans variable
        if chessboard[7][0].play_once == 0:
            castling_little = start_tab64 + 2
        return castling_little,castling_long
    elif color == "black":
        if chessboard[0][7].play_once == 0: #si tour grand roque a pas bougé
            castling_long = start_tab64 - 2 #alors ajout vecteur directionnel dans variable
        if chessboard[7][7].play_once == 0:
            castling_little = start_tab64 + 2
        return castling_little,castling_long


def king_side_castle(arrived_index_1, arrived_index_2, screen, background):
    rook_start_x, rook_start_y = chessboard[arrived_index_1 + 1][arrived_index_2].get_pos()
    rook_arrived_x, rook_arrived_y = chessboard[arrived_index_1 - 1][arrived_index_2].get_pos()

    screen.blit(background, (rook_arrived_x, rook_arrived_y), area=pygame.Rect(rook_arrived_x, rook_arrived_y, 93.75,
                                                                               93.75))  # blit morceau background sur case arrivée pour enlever pièce

    chessboard[arrived_index_1 - 1][arrived_index_2].surface = chessboard[arrived_index_1 + 1][arrived_index_2].surface
    chessboard[arrived_index_1 - 1][arrived_index_2].piece = chessboard[arrived_index_1 + 1][arrived_index_2].piece  # pièce sur case arrivée devient celle de case de départ
    chessboard[arrived_index_1 - 1][arrived_index_2].color = chessboard[arrived_index_1 + 1][arrived_index_2].piece.color

    chessboard[arrived_index_1 + 1][arrived_index_2].play_once += 1

    chessboard[arrived_index_1 + 1][arrived_index_2].color = None
    chessboard[arrived_index_1 + 1][arrived_index_2].piece = None  # efface pièce de la case de départ
    screen.blit(chessboard[arrived_index_1 - 1][arrived_index_2].surface,(rook_arrived_x, rook_arrived_y))  # blit sur ecran de la position de la nouvelle pièce sur case arrivée

    screen.blit(background, (rook_start_x, rook_start_y), area=pygame.Rect(rook_start_x, rook_start_y, 93.75,93.75))  # efface l’ancienne case de départ avec le fond


def queen_side_castle(arrived_index_1, arrived_index_2, screen, background):
    rook_start_x, rook_start_y = chessboard[arrived_index_1 - 2][arrived_index_2].get_pos()
    rook_arrived_x, rook_arrived_y = chessboard[arrived_index_1 + 1][arrived_index_2].get_pos()

    screen.blit(background, (rook_arrived_x, rook_arrived_y), area=pygame.Rect(rook_arrived_x, rook_arrived_y, 93.75,
                                                                               93.75))  # blit morceau background sur case arrivée pour enlever pièce

    chessboard[arrived_index_1 + 1][arrived_index_2].surface = chessboard[arrived_index_1 - 2][arrived_index_2].surface
    chessboard[arrived_index_1 + 1][arrived_index_2].piece = chessboard[arrived_index_1 - 2][arrived_index_2].piece  # pièce sur case arrivée devient celle de case de départ
    chessboard[arrived_index_1 + 1][arrived_index_2].color = chessboard[arrived_index_1 - 2][arrived_index_2].piece.color

    chessboard[arrived_index_1 - 2][arrived_index_2].play_once += 1

    chessboard[arrived_index_1 - 2][arrived_index_2].color = None
    chessboard[arrived_index_1 - 2][arrived_index_2].piece = None  # efface pièce de la case de départ
    screen.blit(chessboard[arrived_index_1 + 1][arrived_index_2].surface,(rook_arrived_x, rook_arrived_y))  # blit sur ecran de la position de la nouvelle pièce sur case arrivée

    screen.blit(background, (rook_start_x, rook_start_y), area=pygame.Rect(rook_start_x, rook_start_y, 93.75,93.75))  # efface l’ancienne case de départ avec le fond

