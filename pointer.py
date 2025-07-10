import pygame
from case import chessboard

Pointer = pygame.image.load("sprite/Pointer.png") #Sprite pointer

def add_pointer(screen,enable_case,color_turn,start_index_1, start_index_2): #fonction pour afficher le pointeur
    for row in chessboard:
        for case in row:
                if case.tab64 in enable_case and chessboard[start_index_1][start_index_2].piece.color == color_turn \
                    and chessboard[start_index_1][start_index_2].piece.color != case.color: #si la case est dans la liste des cases possibles et que
                    #c'est a la bonne couleur de jouer
                    x,y = case.get_pos()
                    screen.blit(Pointer, (x, y))

    pygame.display.flip()


def remove_pointer(screen,background,enable_case): #fonction pour enlever le pointeur
    for row in chessboard:
        for case in row:
            if case.tab64 in enable_case:
                x, y = case.get_pos()
                screen.blit(background, (x,y), area=pygame.Rect(x,y, 93.75, 93.75)) #reblitt sur toute les pos ayant un pointeur

                if case.piece is not None: #si une pièce est sur une des cases alors on reblitt juste la surface dessus
                    screen.blit(case.surface, (x, y))

    pygame.display.flip()