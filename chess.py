import pygame

pygame.init()

from starting_game import position_starting_game #import fonction position départ
from moving_piece import find_coord,move_and_blitt #import fonction détection coordonnées pièces et deplacement pieces

from piece import *





running = True #variable initialisation boucle


screen = pygame.display.set_mode((750,750),pygame.SCALED) # définition fenêtre principale
title = pygame.display.set_caption("Chess") #initialisation fenetre principale

background = pygame.image.load("sprite/background.png")
screen.blit(background,(0,0)) #chargement du background + affichage

position_starting_game(screen) #appel de la fonction pour la position des pieces en début de partie

pygame.display.flip() #MAJ de l'écran


selected_piece = 0 #variable pour savoir si une piece est séléctionnée

start_index_1,start_index_2 = None,None
arrived_index_1, arrived_index_2 = None,None #variable de coordonnées d'arrivée et de sortie

click_pos_start = None
click_pos_arrived = None #variable pour stocker les coordonnées
while running: #Boucle principale

    for event in pygame.event.get():
        if event.type == pygame.QUIT: #permet de quitter la boucle en cliquant sur la croix
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if selected_piece == 0:#si aucune piece n'est séléctionné
                click_pos_start = event.pos
                start_index_1,start_index_2 = find_coord(click_pos_start)#evenement clique souris + appel et stockage de la fonction détection des coordonnées
                selected_piece = 1
            else:
                click_pos_arrived = event.pos #si une piece est séléctionné
                arrived_index_1, arrived_index_2 = find_coord(click_pos_arrived)#evenement clique souris + appel et stockage de la fonction détection des coordonnées
                if arrived_index_1 == start_index_1 and arrived_index_2 == start_index_2: #si la même case est séléctionné alors reset
                    selected_piece = 0
                else:
                    move_and_blitt(screen,background,start_index_1,start_index_2,arrived_index_1,arrived_index_2)#appel fonction déplacement des pièces
                    selected_piece = 0



                    pygame.display.flip()#MAJ de l'écran















