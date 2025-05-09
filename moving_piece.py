import pygame
pygame.init()

from case import * #import pour stockage surface correspondante dans variable "lettre"

#fonction de détéction de coordonnées avec return de lettre et chiffre pour affichage piece a chaque clique
def find_coord(pos_click):
    x,y = pos_click
    letter = None
    number_x = None
    number_y = None

    if 0 < x < 93.75:
        letter = a
        number_x = 0
    elif 93.75 < x < 187.5:
        letter = b
        number_x = 1
    elif 187.5 < x < 281.25:
        letter = c
        number_x = 2
    elif 281.25 < x < 375:
        letter = d
        number_x = 3
    elif 375 < x < 468.75:
        letter = e
        number_x = 4
    elif 468.75 < x < 562.5:
        letter = f
        number_x = 5
    elif 562.5 < x < 656.25:
        letter = g
        number_x = 6
    elif 656.25 < x < 750:
        letter = h
        number_x = 7

    if 0 < y < 93.75:
        number_y = 7
    elif 93.75 < y < 187.5:
        number_y = 6
    elif 187.5 < y < 281.25:
        number_y = 5
    elif 281.25 < y < 375:
        number_y = 4
    elif 375 < y < 468.75:
        number_y = 3
    elif 468.75 < y < 562.5:
        number_y = 2
    elif 562.5 < y < 656.25:
        number_y = 1
    elif 656.25 < y < 750:
        number_y = 0


    return letter,number_x,number_y


























