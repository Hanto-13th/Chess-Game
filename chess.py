import pygame

pygame.init()

from starting_game import position_starting_game #import fonction position départ
from moving_piece import *  # import fonction détection coordonnées pièces et deplacement pieces
from pointer import *





running = True #variable initialisation boucle


screen = pygame.display.set_mode((750,750),pygame.SCALED) # définition fenêtre principale
title = pygame.display.set_caption("Chess") #initialisation fenetre principale

background = pygame.image.load("sprite/background.png")
screen.blit(background,(0,0)) #chargement du background + affichage

position_starting_game(screen) #appel de la fonction pour la position des pieces en début de partie

pygame.display.flip() #MAJ de l'écran


selected_piece = 0 #variable pour savoir si une piece est séléctionnée
color_turn = "white"
turn = 1

start_index_1,start_index_2 = None,None
arrived_index_1, arrived_index_2 = None,None #variable de coordonnées d'arrivée et de sortie

click_pos_start = None
click_pos_arrived = None #variable pour stocker les coordonnées

play = 0
enable_case = []
print(f"NUMBER TURN: {turn}")
print(f"COLOR TURN: {color_turn}\n")
while running: #Boucle principale

    for event in pygame.event.get():
        if event.type == pygame.QUIT: #permet de quitter la boucle en cliquant sur la croix
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if selected_piece == 0:#si aucune piece n'est séléctionné
                click_pos_start = event.pos
                start_index_1,start_index_2 = find_coord(click_pos_start)#evenement clique souris + appel et stockage de la fonction détection des coordonnées
                enable_case = possible_movement(start_index_1, start_index_2)
                add_pointer(screen,enable_case,color_turn,start_index_1, start_index_2)
                selected_piece = 1

            else:#si une piece est séléctionné
                click_pos_arrived = event.pos
                arrived_index_1, arrived_index_2 = find_coord(click_pos_arrived)#evenement clique souris + appel et stockage de la fonction détection des coordonnées
                if (arrived_index_1 == start_index_1 and arrived_index_2 == start_index_2) or (color_turn == chessboard[arrived_index_1][arrived_index_2].color) or (color_turn != chessboard[start_index_1][start_index_2].color):
                    #si la même case est séléctionné ou si la case d'arrivée est une case de la même couleur que la case de départ alors reset
                    selected_piece = 0
                else:
                    remove_pointer(screen,background,enable_case)
                    play = move_and_capture(screen,background,start_index_1,start_index_2,arrived_index_1,arrived_index_2,enable_case,play)#appel fonction déplacement des pièces
                    selected_piece = 0
                    color_turn,play = who_is_the_turn(color_turn,play)
                    turn += 1
                    print(f"NUMBER TURN: {turn}")
                    print(f"COLOR TURN: {color_turn}\n")


                    pygame.display.flip()#MAJ de l'écran















