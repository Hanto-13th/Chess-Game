import pygame
pygame.init()

#import all my function and variable from my other files
from constants import *
from case import chessboard
from starting_game import position_starting_game
from moving_piece import find_coord,possible_movement,move_and_capture,display_state,who_is_the_turn
from pointer import add_pointer,remove_pointer
from rules import is_check,checking,checkmate,stalemate

#---------------------------------------------------------------------
# Set the screen and display the game start position and state of play
#---------------------------------------------------------------------

screen = pygame.display.set_mode((SCREEN_H,SCREEN_W),pygame.SCALED)
title = pygame.display.set_caption("Chess")
background = pygame.image.load("sprite/background.png")
screen.blit(background,(0,0))

position_starting_game(screen)
display_state(color_turn = "white",global_turn = 1,check = None)
pygame.display.flip() #Screen Update

#--------------
# The Main Loop
#--------------

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            #if no pieces selected yet
            if selected_piece == 0:
                #look about if there is a stalemate
                pat = stalemate(possible_movement, color_turn, check, list_attack_white, list_attack_black,en_passant,pos_en_passant)
                if pat:
                    print("STALEMATE")
                else:
                    #take information about the piece (position,possible movement and add the pointer to view his movement)
                    click_pos_start = event.pos
                    start_index_1,start_index_2 = find_coord(click_pos_start)
                    enable_case,castling_little,castling_long = possible_movement(start_index_1, start_index_2,en_passant,pos_en_passant)
                    try:
                        add_pointer(screen,enable_case,color_turn,start_index_1, start_index_2)
                    except Exception as ex:
                        selected_piece = 0
                        print("Any pieces are selected")
                    #if no any problem the piece is select
                    selected_piece = 1
                    if chessboard[start_index_1][start_index_2].color != color_turn or enable_case is None:
                        selected_piece = 0

            #if a piece is select
            elif selected_piece == 1:
                #take information about his destination
                click_pos_arrived = event.pos
                arrived_index_1, arrived_index_2 = find_coord(click_pos_arrived)

                #if there is a check, until the check is still active, look if the next movement maintain check active
                #if not, the game continue
                if check:
                    if checking(possible_movement, start_index_1, start_index_2, arrived_index_1, arrived_index_2,color_turn,en_passant,pos_en_passant):
                        print("THE KING IS CHECK !")
                        remove_pointer(screen, background, enable_case)
                        selected_piece = 0
                    if not checking(possible_movement, start_index_1, start_index_2, arrived_index_1, arrived_index_2,color_turn,en_passant,pos_en_passant):
                        check = False

                if (arrived_index_1 == start_index_1 and arrived_index_2 == start_index_2) or (color_turn == chessboard[arrived_index_1][arrived_index_2].color):
                    remove_pointer(screen, background, enable_case)
                    selected_piece = 0
                #if they are no problem, the destination is applicable and the piece is moved
                if not check and not checking(possible_movement,start_index_1,start_index_2,arrived_index_1,arrived_index_2,color_turn,en_passant,pos_en_passant) and selected_piece == 1:
                    remove_pointer(screen,background,enable_case)
                    play,en_passant,pos_en_passant = move_and_capture(screen,background,start_index_1,start_index_2,arrived_index_1,arrived_index_2,enable_case,castling_little,castling_long,en_passant,color_turn)
                    selected_piece = 0
                    #look after the move if there is a check
                    check,color_king_in_check,list_attack_white,list_attack_black = is_check(possible_movement,en_passant,pos_en_passant)
                    #and after if the check is a checkmate or not
                    mat = checkmate(possible_movement, check, color_king_in_check,en_passant,pos_en_passant)
                    if mat:
                        print("CHECKMATE")
                    #if not, the game pass one turn, and it's the other player to play
                    else:
                        color_turn,play,half_turn,global_turn = who_is_the_turn(color_turn,play,half_turn,global_turn)
                        display_state(color_turn,global_turn,check)


                    pygame.display.flip()#MAJ de l'écran















