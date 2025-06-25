from case import chessboard, tab64_to_tab120#import les  listes "case" et "coord_case" pour fonction "move_and_blitt"
from piece import *
from constants import move_pawn,move_king,move_knight,move_queen,move_rook,move_bishop



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

def possible_movement(start_index_1,start_index_2):
#fonction pour connaitre les cases de chaque pièce en fonction de leur position
    possible_case = []
    if chessboard[start_index_1][start_index_2].piece == "pawn" and chessboard[start_index_1][start_index_2].color == "white":
                if tab64_to_tab120(chessboard[start_index_1][start_index_2].tab64 - move_pawn[0]) == -1:
                    possible_case.append(None)
                else:
                    possible_case.append(chessboard[start_index_1][start_index_2].tab64 - move_pawn[0])
                if tab64_to_tab120(chessboard[start_index_1][start_index_2].tab64 - move_pawn[1]) == -1:
                    possible_case.append(None)
                else:
                    possible_case.append(chessboard[start_index_1][start_index_2].tab64 - move_pawn[1])
                if tab64_to_tab120(chessboard[start_index_1][start_index_2].tab64 - move_pawn[2]) == -1:
                    possible_case.append(None)
                else:
                    possible_case.append(chessboard[start_index_1][start_index_2].tab64 - move_pawn[2])

    if chessboard[start_index_1][start_index_2].piece == "pawn" and chessboard[start_index_1][start_index_2].color == "black":
                if tab64_to_tab120(chessboard[start_index_1][start_index_2].tab64 + move_pawn[0]) == -1:
                    possible_case.append(None)
                else:
                    possible_case.append(chessboard[start_index_1][start_index_2].tab64 + move_pawn[0])
                if tab64_to_tab120(chessboard[start_index_1][start_index_2].tab64 + move_pawn[1]) == -1:
                    possible_case.append(None)
                else:
                    possible_case.append(chessboard[start_index_1][start_index_2].tab64 + move_pawn[1])
                if tab64_to_tab120(chessboard[start_index_1][start_index_2].tab64 + move_pawn[2]) == -1:
                    possible_case.append(None)
                else:
                    possible_case.append(chessboard[start_index_1][start_index_2].tab64 + move_pawn[2])

    if chessboard[start_index_1][start_index_2].piece == "king":
            if tab64_to_tab120(chessboard[start_index_1][start_index_2].tab64 - move_king[0]) == -1:
                possible_case.append(None)
            else:
                possible_case.append(chessboard[start_index_1][start_index_2].tab64 - move_king[0])
            if tab64_to_tab120(chessboard[start_index_1][start_index_2].tab64 + move_king[0]) == -1:
                possible_case.append(None)
            else:
                possible_case.append(chessboard[start_index_1][start_index_2].tab64 + move_king[0])

            if tab64_to_tab120(chessboard[start_index_1][start_index_2].tab64 - move_king[1]) == -1:
                possible_case.append(None)
            else:
                possible_case.append(chessboard[start_index_1][start_index_2].tab64 - move_king[1])
            if tab64_to_tab120(chessboard[start_index_1][start_index_2].tab64 + move_king[1]) == -1:
                possible_case.append(None)
            else:
                possible_case.append(chessboard[start_index_1][start_index_2].tab64 + move_king[1])

            if tab64_to_tab120(chessboard[start_index_1][start_index_2].tab64 - move_king[2]) == -1:
                possible_case.append(None)
            else:
                possible_case.append(chessboard[start_index_1][start_index_2].tab64 - move_king[2])
            if tab64_to_tab120(chessboard[start_index_1][start_index_2].tab64 + move_king[2]) == -1:
                possible_case.append(None)
            else:
                possible_case.append(chessboard[start_index_1][start_index_2].tab64 + move_king[2])

            if tab64_to_tab120(chessboard[start_index_1][start_index_2].tab64 - move_king[3]) == -1:
                possible_case.append(None)
            else:
                possible_case.append(chessboard[start_index_1][start_index_2].tab64 - move_king[3])
            if tab64_to_tab120(chessboard[start_index_1][start_index_2].tab64 + move_king[3]) == -1:
                possible_case.append(None)
            else:
                possible_case.append(chessboard[start_index_1][start_index_2].tab64 + move_king[3])

    if chessboard[start_index_1][start_index_2].piece == "queen":
        for time in range(1, 9):
            if tab64_to_tab120(chessboard[start_index_1][start_index_2].tab64 - move_queen[0] * time) == -1:
                break

            else:
                possible_case.append(chessboard[start_index_1][start_index_2].tab64 - move_queen[0] * time)
        for time in range(1, 9):
            if tab64_to_tab120(chessboard[start_index_1][start_index_2].tab64 + move_queen[0] * time) == -1:
                break

            else:
                possible_case.append(chessboard[start_index_1][start_index_2].tab64 + move_queen[0] * time)
        for time in range(1, 9):
            if tab64_to_tab120(chessboard[start_index_1][start_index_2].tab64 - move_queen[1] * time) == -1:
                break

            else:
                possible_case.append(chessboard[start_index_1][start_index_2].tab64 - move_queen[1] * time)
        for time in range(1, 9):
            if tab64_to_tab120(chessboard[start_index_1][start_index_2].tab64 + move_queen[1] * time) == -1:
                break

            else:
                possible_case.append(chessboard[start_index_1][start_index_2].tab64 + move_queen[1] * time)
        for time in range(1, 9):
            if tab64_to_tab120(chessboard[start_index_1][start_index_2].tab64 - move_queen[2] * time) == -1:
                break

            else:
                possible_case.append(chessboard[start_index_1][start_index_2].tab64 - move_queen[2] * time)
        for time in range(1, 9):
            if tab64_to_tab120(chessboard[start_index_1][start_index_2].tab64 + move_queen[2] * time) == -1:
                break

            else:
                possible_case.append(chessboard[start_index_1][start_index_2].tab64 + move_queen[2] * time)
        for time in range(1, 9):
            if tab64_to_tab120(chessboard[start_index_1][start_index_2].tab64 - move_queen[3] * time) == -1:
                break

            else:
                possible_case.append(chessboard[start_index_1][start_index_2].tab64 - move_queen[3] * time)
        for time in range(1, 9):
            if tab64_to_tab120(chessboard[start_index_1][start_index_2].tab64 + move_queen[3] * time) == -1:
                break

            else:
                possible_case.append(chessboard[start_index_1][start_index_2].tab64 + move_queen[3] * time)

    if chessboard[start_index_1][start_index_2].piece == "bishop":
        for time in range(1, 9):
            if tab64_to_tab120(chessboard[start_index_1][start_index_2].tab64 - move_bishop[0] * time) == -1:
                break

            else:
                possible_case.append(chessboard[start_index_1][start_index_2].tab64 - move_bishop[0] * time)
        for time in range(1, 9):
            if tab64_to_tab120(chessboard[start_index_1][start_index_2].tab64 + move_bishop[0] * time) == -1:
                break

            else:
                possible_case.append(chessboard[start_index_1][start_index_2].tab64 + move_bishop[0] * time)
        for time in range(1, 9):
            if tab64_to_tab120(chessboard[start_index_1][start_index_2].tab64 - move_bishop[1] * time) == -1:
                break

            else:
                possible_case.append(chessboard[start_index_1][start_index_2].tab64 - move_bishop[1] * time)
        for time in range(1, 9):
            if tab64_to_tab120(chessboard[start_index_1][start_index_2].tab64 + move_bishop[1] * time) == -1:
                break

            else:
                possible_case.append(chessboard[start_index_1][start_index_2].tab64 + move_bishop[1] * time)


    if chessboard[start_index_1][start_index_2].piece == "knight":
            if tab64_to_tab120(chessboard[start_index_1][start_index_2].tab64 - move_knight[0]) == -1:
                possible_case.append(None)

            else:
                possible_case.append(chessboard[start_index_1][start_index_2].tab64 - move_knight[0])
            if tab64_to_tab120(chessboard[start_index_1][start_index_2].tab64 + move_knight[0]) == -1:
                possible_case.append(None)

            else:
                possible_case.append(chessboard[start_index_1][start_index_2].tab64 + move_knight[0])
            if tab64_to_tab120(chessboard[start_index_1][start_index_2].tab64 - move_knight[1]) == -1:
                possible_case.append(None)

            else:
                possible_case.append(chessboard[start_index_1][start_index_2].tab64 - move_knight[1])
            if tab64_to_tab120(chessboard[start_index_1][start_index_2].tab64 + move_knight[1]) == -1:
                possible_case.append(None)

            else:
                possible_case.append(chessboard[start_index_1][start_index_2].tab64 + move_knight[1])
            if tab64_to_tab120(chessboard[start_index_1][start_index_2].tab64 - move_knight[2]) == -1:
                possible_case.append(None)

            else:
                possible_case.append(chessboard[start_index_1][start_index_2].tab64 - move_knight[2])
            if tab64_to_tab120(chessboard[start_index_1][start_index_2].tab64 + move_knight[2]) == -1:
                possible_case.append(None)

            else:
                possible_case.append(chessboard[start_index_1][start_index_2].tab64 + move_knight[2])
            if tab64_to_tab120(chessboard[start_index_1][start_index_2].tab64 - move_knight[3]) == -1:
                possible_case.append(None)

            else:
                possible_case.append(chessboard[start_index_1][start_index_2].tab64 - move_knight[3])
            if tab64_to_tab120(chessboard[start_index_1][start_index_2].tab64 + move_knight[3]) == -1:
                possible_case.append(None)

            else:
                possible_case.append(chessboard[start_index_1][start_index_2].tab64 + move_knight[3])


    if chessboard[start_index_1][start_index_2].piece == "rook":
            for time in range(1,9):
                if tab64_to_tab120(chessboard[start_index_1][start_index_2].tab64 - move_rook[0] * time) == -1:
                    break

                else:
                    possible_case.append(chessboard[start_index_1][start_index_2].tab64 - move_rook[0] * time)
            for time in range(1, 9):
                if tab64_to_tab120(chessboard[start_index_1][start_index_2].tab64 + move_rook[0] * time) == -1:
                    break

                else:
                    possible_case.append(chessboard[start_index_1][start_index_2].tab64 + move_rook[0] * time)
            for time in range(1, 9):
                if tab64_to_tab120(chessboard[start_index_1][start_index_2].tab64 - move_rook[1] * time) == -1:
                    break

                else:
                    possible_case.append(chessboard[start_index_1][start_index_2].tab64 - move_rook[1] * time)
            for time in range(1, 9):
                if tab64_to_tab120(chessboard[start_index_1][start_index_2].tab64 + move_rook[1] * time) == -1:
                    break

                else:
                    possible_case.append(chessboard[start_index_1][start_index_2].tab64 + move_rook[1] * time)


    enable_case = list(filter(None,possible_case)) #liste sans None

    return enable_case

def move_and_capture(screen,background,start_index_1,start_index_2,arrived_index_1,arrived_index_2,enable_case): #fonction de déplacement des pièces

    if chessboard[arrived_index_1][arrived_index_2].tab64 in enable_case:
        start_x, start_y = chessboard[start_index_1][start_index_2].get_pos()
        arrived_x, arrived_y = chessboard[arrived_index_1][arrived_index_2].get_pos()

        screen.blit(background, (arrived_x, arrived_y), area=pygame.Rect(arrived_x, arrived_y, 93.75, 93.75)) #blit morceau background sur case arrivée pour enlever pièce

        chessboard[arrived_index_1][arrived_index_2].surface = chessboard[start_index_1][start_index_2].surface #affichage sur case arrivée devient celle de case de départ
        chessboard[arrived_index_1][arrived_index_2].color = chessboard[start_index_1][start_index_2].get_color() #couleur sur case arrivée devient celle de case de départ
        chessboard[arrived_index_1][arrived_index_2].piece = chessboard[start_index_1][start_index_2].piece#pièce sur case arrivée devient celle de case de départ
        chessboard[start_index_1][start_index_2].color = None #efface couleur de la case de départ
        chessboard[start_index_1][start_index_2].piece = None #efface pièce de la case de départ
        screen.blit(chessboard[arrived_index_1][arrived_index_2].surface, (arrived_x, arrived_y)) #blit sur ecran de la position de la nouvelle pièce sur case arrivée

        screen.blit(background, (start_x, start_y), area=pygame.Rect(start_x, start_y, 93.75, 93.75)) #efface l’ancienne case de départ avec le fond
        return True #une pièce a été joué

    else:
        return False #une pièce n'est pas joué

def who_is_the_turn(color_turn,play,turn):#fonction pour savoir qui joue le tour
    if color_turn == "white" and play:
        color_turn = "black"
    elif color_turn == "black" and play:
        color_turn = "white"

    play = False
    turn += 1
    return color_turn,play,turn

def display_turn_and_color(color_turn,turn):
    print(f"NUMBER TURN: {turn}")
    print(f"COLOR TURN: {color_turn}\n")




























































