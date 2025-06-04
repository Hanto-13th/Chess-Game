import pygame
pygame.init()

from case import *#import les  listes "case" et "coord_case" pour fonction "move_and_blitt"
from piece import *



#fonction de détéction de coordonnées avec return index pour affichage piece a chaque clique
def find_coord(pos_click):
    x,y = pos_click
    coord_index_x = None
    coord_index_y = None

    if 0 < x < 93.75:
        coord_index_x = 0
    elif 93.75 < x < 187.5:
        coord_index_x = 1
    elif 187.5 < x < 281.25:
        coord_index_x = 2
    elif 281.25 < x < 375:
        coord_index_x = 3
    elif 375 < x < 468.75:
        coord_index_x = 4
    elif 468.75 < x < 562.5:
        coord_index_x = 5
    elif 562.5 < x < 656.25:
        coord_index_x = 6
    elif 656.25 < x < 750:
        coord_index_x = 7

    if 0 < y < 93.75:
        coord_index_y = 7
    elif 93.75 < y < 187.5:
        coord_index_y = 6
    elif 187.5 < y < 281.25:
        coord_index_y = 5
    elif 281.25 < y < 375:
        coord_index_y = 4
    elif 375 < y < 468.75:
        coord_index_y = 3
    elif 468.75 < y < 562.5:
        coord_index_y = 2
    elif 562.5 < y < 656.25:
        coord_index_y = 1
    elif 656.25 < y < 750:
        coord_index_y = 0


    return coord_index_x,coord_index_y

def move_and_capture(screen,background,start_index_1,start_index_2,arrived_index_1,arrived_index_2):
#fonction de déplacement des pièces




    #prise coordonnées des cases de départ et d'arrivée dans des variables
    x, y = coord_case[start_index_1][start_index_2]
    z, w = coord_case[arrived_index_1][arrived_index_2]

    screen.blit(background, (z,w), area=pygame.Rect(z,w, 93.75, 93.75)) #blit morceau background sur case arrivée pour enlever pièce

    chessboard[arrived_index_1][arrived_index_2] = chessboard[start_index_1][start_index_2] #pièce sur case arrivée devient celle de case de départ
    screen.blit(chessboard[arrived_index_1][arrived_index_2], (z, w)) #blit sur ecran de la position de la nouvelle pièce sur case arrivée

    screen.blit(background, (x, y), area=pygame.Rect(x, y, 93.75, 93.75)) #efface l’ancienne case de départ avec le fond

def who_is_the_turn(color_turn):
    if color_turn == "white":
        color_turn = "black"
    elif color_turn == "black":
        color_turn = "white"


    return color_turn


















































