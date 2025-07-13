import pygame
from case import chessboard

#load the sprite pointer (Draw by me)
Pointer = pygame.image.load("sprite/Pointer.png")

def add_pointer(screen,enable_case,color_turn,start_index_1, start_index_2):
    """Function to blit the pointer on the screen, in the enable case which
        can move or capture (start_index_1, start_index_2)"""

    #blit the pointer for all cases in enable_case
    for row in chessboard:
        for case in row:
                if case.tab64 in enable_case and chessboard[start_index_1][start_index_2].piece.color == color_turn \
                    and chessboard[start_index_1][start_index_2].piece.color != case.color:
                    x,y = case.get_pos()
                    screen.blit(Pointer, (x, y))

    pygame.display.flip()


def remove_pointer(screen,background,enable_case):
    """Function to remove the pointer on the screen, in the enable case which
            can move or capture (start_index_1, start_index_2)"""

    # blit part of background for all cases in enable_case
    for row in chessboard:
        for case in row:
            if case.tab64 in enable_case:
                x, y = case.get_pos()
                screen.blit(background, (x,y), area=pygame.Rect(x,y, 93.75, 93.75))
                #if piece is on, blit the piece surface on the case
                if case.piece is not None:
                    screen.blit(case.surface, (x, y))

    pygame.display.flip()