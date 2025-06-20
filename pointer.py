import pygame
from case import chessboard

Pointer = pygame.image.load("sprite/Pointer.jpg") #Sprite pointer

def add_pointer(screen,enable_case,color_turn,start_index_1, start_index_2):
    for row in chessboard:
        for case in row:
                if case.tab64 in enable_case and chessboard[start_index_1][start_index_2].color == color_turn:
                    x,y = case.get_pos()
                    screen.blit(Pointer, (x, y))
    pygame.display.flip()


def remove_pointer(screen,background,enable_case):
    for row in chessboard:
        for case in row:
            if case.tab64 in enable_case:
                x, y = case.get_pos()
                screen.blit(background, (x,y), area=pygame.Rect(x,y, 93.75, 93.75))

                if case.piece is not None:
                    screen.blit(case.surface, (x, y))

    pygame.display.flip()