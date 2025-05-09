import pygame

pygame.init()

from starting_game import position_starting_game #import fonction position départ
from moving_piece import find_coord #import fonction détection coordonnées pièces
from piece import W_rook #!!!TEST!!!
from case import coord_case # import coordonnées case







running = True #variable initialisation boucle


screen = pygame.display.set_mode((750,750),pygame.SCALED) # définition fenêtre principale
title = pygame.display.set_caption("Chess") #initialisation fenetre principale

background = pygame.image.load("C:/Users/anton/Documents/Python/Chess/sprite/background.png")
screen.blit(background,(0,0)) #chargement du background + affichage

position_starting_game(screen) #appel de la fonction pour la position des pieces en début de partie

pygame.display.flip() #MAJ de l'écran



pos_click = None #variable pour stocker les coordonnées
while running: #Boucle principale

    for event in pygame.event.get():
        if event.type == pygame.QUIT: #permet de quitter la boucle en cliquant sur la croix
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos_click = event.pos
            letter_case,number_x,number_y = find_coord(pos_click) #evenement clique souris + appel de la fonction détection des coordonnées

            letter_case[number_y].blit(W_rook, (0, 0))# !!! TEST !!!
            screen.blit(letter_case[number_y], coord_case[number_x][number_y])# !!! TEST !!!



            pygame.display.flip()#MAJ de l'écran















