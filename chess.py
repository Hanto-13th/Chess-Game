import pygame

pygame.init()

from constants import SCREEN_H,SCREEN_W
from case import chessboard
from starting_game import position_starting_game #import fonction position départ
from moving_piece import find_coord,possible_movement,move_and_capture,display_state,who_is_the_turn  # import des fonctions de déplacement de pièce
from pointer import add_pointer,remove_pointer #import du sprite ainsi que les fonctions d'affichage et désaffichage du pointeur
from rules import is_check,checking,checkmate,stalemate

screen = pygame.display.set_mode((SCREEN_H,SCREEN_W),pygame.SCALED) # définition fenêtre principale
title = pygame.display.set_caption("Chess") #initialisation fenetre principale
background = pygame.image.load("sprite/background.png")
screen.blit(background,(0,0)) #chargement du background + affichage

running = True #variable initialisation boucle
selected_piece = 0 #variable pour savoir si une piece est séléctionnée
color_turn = "white"
turn = 0 #variable pour gestion tour
global_turn = 1
start_index_1,start_index_2 = None,None
arrived_index_1, arrived_index_2 = None,None #variable de coordonnées d'arrivée et de sortie
castling_little,castling_long = None,None
enable_case = [] #liste pour case de déplacement valide
list_attack_white,list_attack_black = None,None
check = False


position_starting_game(screen) #appel de la fonction pour la position des pieces en début de partie
display_state(color_turn = "white",global_turn = 1,check = None)
pygame.display.flip() #MAJ de l'écran


while running: #Boucle principale

    for event in pygame.event.get():
        if event.type == pygame.QUIT: #permet de quitter la boucle en cliquant sur la croix
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:

            if selected_piece == 0:#si aucune piece n'est séléctionné
                pat = stalemate(possible_movement, color_turn, check, list_attack_white, list_attack_black)
                if pat:
                    print("STALEMATE")
                else:
                    click_pos_start = event.pos
                    start_index_1,start_index_2 = find_coord(click_pos_start)#evenement clique souris + appel et stockage de la fonction détection des coordonnées
                    enable_case,castling_little,castling_long = possible_movement(start_index_1, start_index_2) #stockage des cases de déplacement possible
                    try:
                        add_pointer(screen,enable_case,color_turn,start_index_1, start_index_2) #affichage pointeur
                    except Exception as ex:
                        selected_piece = 0
                        print("Any pieces are selected")
                    selected_piece = 1
                    if chessboard[start_index_1][start_index_2].color != color_turn or enable_case is None:
                        selected_piece = 0


            elif selected_piece == 1:#si une piece est séléctionné
                click_pos_arrived = event.pos
                arrived_index_1, arrived_index_2 = find_coord(click_pos_arrived)  # evenement clique souris + appel et stockage de la fonction détection des coordonnées


                if check:
                    # vérifier si le coup rend/maintient le roi en échec
                    if checking(possible_movement, start_index_1, start_index_2, arrived_index_1, arrived_index_2,color_turn):
                        print("THE KING IS CHECK !")
                        remove_pointer(screen, background, enable_case)
                        selected_piece = 0
                    if not checking(possible_movement, start_index_1, start_index_2, arrived_index_1, arrived_index_2,color_turn):
                        check = False

                if (arrived_index_1 == start_index_1 and arrived_index_2 == start_index_2) \
                    or (color_turn == chessboard[arrived_index_1][arrived_index_2].color):
                    # si la même case est séléctionné ou si la case d'arrivée est une case de la même couleur que la case de départ alors reset
                    remove_pointer(screen, background, enable_case)
                    selected_piece = 0

                if not check and not checking(possible_movement,start_index_1,start_index_2,arrived_index_1,arrived_index_2,color_turn) and selected_piece == 1:
                    remove_pointer(screen,background,enable_case) #désaffichage pointeur
                    play = move_and_capture(screen,background,start_index_1,start_index_2,arrived_index_1,arrived_index_2,enable_case,castling_little,castling_long,color_turn)#appel fonction déplacement des pièces
                    selected_piece = 0

                    check,color_king_in_check,list_attack_white,list_attack_black = is_check(possible_movement)
                    mat = checkmate(possible_movement, check, color_king_in_check)
                    if mat:
                        print("CHECKMATE")
                    else:
                        color_turn,play,turn,global_turn = who_is_the_turn(color_turn,play,turn,global_turn)
                        display_state(color_turn,global_turn,check)


                    pygame.display.flip()#MAJ de l'écran















