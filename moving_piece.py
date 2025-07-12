from case import chessboard, tab64_to_tab120#import les  listes "case" et "coord_case" pour fonction "move_and_blitt"
from piece import *
from constants import move_pawn_white,move_pawn_black,move_king,move_knight,move_queen,move_rook,move_bishop,last_case_white,last_case_black
from rules import is_castling,king_side_castle,queen_side_castle,promotion



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

def possible_movement(start_index_1,start_index_2,en_passant,pos_en_passant):
#fonction pour connaitre les cases de chaque pièce en fonction de leur position
    case_with_piece = []
    possible_case = []
    castling_little, castling_long = None,None

    for row in chessboard:
        for case in row:
            if case.piece is not None:
                case_with_piece.append(case.tab64)

    if chessboard[start_index_1][start_index_2].piece is None:
        return None,None,None

    if chessboard[start_index_1][start_index_2].piece.name == "pawn" and chessboard[start_index_1][start_index_2].piece.color == "white":
        start_tab64 = chessboard[start_index_1][start_index_2].tab64
        directions = move_pawn_white

        for direction in directions:
            if direction == -10: # si on avance
                next_tab64 = start_tab64 + direction #on ajoute direction a pos départ
                if tab64_to_tab120(next_tab64) != -1 and next_tab64 not in case_with_piece:#si la case ne sort pas du tableau ou ne rencontre pas de piece
                    possible_case.append(next_tab64) #on l ajoute
            if chessboard[start_index_1][start_index_2].play_once == 0:
                next_tab64 = start_tab64 - 20  # on ajoute direction a pos départ
                if tab64_to_tab120(next_tab64) != -1 and next_tab64 not in case_with_piece:  # si la case ne sort pas du tableau ou ne rencontre pas de piece
                    possible_case.append(next_tab64)  # on l ajoute
            if direction == -11 and start_tab64 + direction in case_with_piece:
                next_tab64 = start_tab64 + direction  # on ajoute direction a pos départ
                if tab64_to_tab120(next_tab64) != -1:  # si la case ne sort pas du tableau ou ne rencontre pas de piece
                    possible_case.append(next_tab64)  # on l ajoute
            if direction == -9 and start_tab64 + direction in case_with_piece:
                next_tab64 = start_tab64 + direction  # on ajoute direction a pos départ
                if tab64_to_tab120(next_tab64) != -1:  # si la case ne sort pas du tableau ou ne rencontre pas de piece
                    possible_case.append(next_tab64)  # on l ajoute
            if en_passant == 1 and pos_en_passant == chessboard[start_index_1][start_index_2].tab64 + 1:
                next_tab64_enpassant = start_tab64 - 9
                if tab64_to_tab120(next_tab64_enpassant) != -1:
                    possible_case.append(next_tab64_enpassant)
            if en_passant == 1 and pos_en_passant == chessboard[start_index_1][start_index_2].tab64 - 1:
                next_tab64_enpassant = start_tab64 - 11
                if tab64_to_tab120(next_tab64_enpassant) != -1:
                    possible_case.append(next_tab64_enpassant)



    if chessboard[start_index_1][start_index_2].piece.name == "pawn" and chessboard[start_index_1][start_index_2].piece.color == "black":
        start_tab64 = chessboard[start_index_1][start_index_2].tab64
        directions = move_pawn_black
        for direction in directions:
            if direction == 10:  # si on avance
                next_tab64 = start_tab64 + direction  # on ajoute direction a pos départ
                if tab64_to_tab120(next_tab64) != -1 and next_tab64 not in case_with_piece:  # si la case ne sort pas du tableau ou ne rencontre pas de piece
                    possible_case.append(next_tab64)  # on l ajoute
            if chessboard[start_index_1][start_index_2].play_once == 0:
                next_tab64 = start_tab64 + 20  # on ajoute direction a pos départ
                if tab64_to_tab120(next_tab64) != -1 and next_tab64 not in case_with_piece:  # si la case ne sort pas du tableau ou ne rencontre pas de piece
                    possible_case.append(next_tab64)  # on l ajoute
            if direction == 11 and start_tab64 + direction in case_with_piece:
                next_tab64 = start_tab64 + direction  # on ajoute direction a pos départ
                if tab64_to_tab120(next_tab64) != -1:  # si la case ne sort pas du tableau ou ne rencontre pas de piece
                    possible_case.append(next_tab64)  # on l ajoute
            if direction == 9 and start_tab64 + direction in case_with_piece:
                next_tab64 = start_tab64 + direction
                if tab64_to_tab120(next_tab64) != -1:  # si la case ne sort pas du tableau ou ne rencontre pas de piece
                    possible_case.append(next_tab64)  # on l ajoute
            if en_passant == 1 and pos_en_passant == chessboard[start_index_1][start_index_2].tab64 - 1:
                next_tab64_enpassant = start_tab64 + 9
                if tab64_to_tab120(next_tab64_enpassant) != -1:
                    possible_case.append(next_tab64_enpassant)
            if en_passant == 1 and pos_en_passant == chessboard[start_index_1][start_index_2].tab64 + 1:
                next_tab64_enpassant = start_tab64 + 11
                if tab64_to_tab120(next_tab64_enpassant) != -1:
                    possible_case.append(next_tab64_enpassant)

    if chessboard[start_index_1][start_index_2].piece.name == "king":
        start_tab64 = chessboard[start_index_1][start_index_2].tab64
        directions = move_king

        if chessboard[start_index_1][start_index_2].play_once == 0:
            castling_little, castling_long = is_castling(chessboard[start_index_1][start_index_2].piece.color,start_tab64)
            if castling_little not in case_with_piece:
                possible_case.append(castling_little)  # en dehors du plateau
            if castling_long not in case_with_piece:
                possible_case.append(castling_long)
        for direction in directions:
            next_tab64 = start_tab64 + direction
            if tab64_to_tab120(next_tab64) != -1:
                for row in chessboard:
                    for case in row:
                        if case.tab64 == next_tab64:
                            if case.piece is None or case.piece.color != chessboard[start_index_1][start_index_2].piece.color:
                                possible_case.append(next_tab64)



    if chessboard[start_index_1][start_index_2].piece.name == "queen":
        start_tab64 = chessboard[start_index_1][start_index_2].tab64
        directions = move_queen

        for direction in directions:
            time = 1
            while True:
                next_tab64 = start_tab64 + direction * time
                if tab64_to_tab120(next_tab64) == -1:
                    break  # en dehors du plateau

                possible_case.append(next_tab64)

                if next_tab64 in case_with_piece:
                    break

                time += 1

    if chessboard[start_index_1][start_index_2].piece.name == "bishop":
        start_tab64 = chessboard[start_index_1][start_index_2].tab64
        directions = move_bishop

        for direction in directions:
            time = 1
            while True:
                next_tab64 = start_tab64 + direction * time
                if tab64_to_tab120(next_tab64) == -1:
                    break  # en dehors du plateau

                possible_case.append(next_tab64)

                if next_tab64 in case_with_piece:
                    break

                time += 1


    if chessboard[start_index_1][start_index_2].piece.name == "knight":
        start_tab64 = chessboard[start_index_1][start_index_2].tab64
        directions = move_knight

        for direction in directions:
                next_tab64 = start_tab64 + direction

                if tab64_to_tab120(next_tab64) != -1:
                    for row in chessboard:
                        for case in row:
                            if case.tab64 == next_tab64:
                                if case.piece is None or case.piece.color != chessboard[start_index_1][start_index_2].piece.color:
                                    possible_case.append(next_tab64)


    if chessboard[start_index_1][start_index_2].piece.name == "rook":
        start_tab64 = chessboard[start_index_1][start_index_2].tab64
        directions = move_rook

        for direction in directions:
            time = 1
            while True:
                next_tab64 = start_tab64 + direction * time
                if tab64_to_tab120(next_tab64) == -1:
                    break  # en dehors du plateau

                possible_case.append(next_tab64)

                if next_tab64 in case_with_piece:
                    break

                time += 1


    possible_case = list(filter(lambda x: tab64_to_tab120(x) != -1,list(filter(None,possible_case))))
    return possible_case,castling_little,castling_long

def move_and_capture(screen,background,start_index_1,start_index_2,arrived_index_1,arrived_index_2,enable_case,castling_little,castling_long,en_passant,color_turn): #fonction de déplacement des pièces
    pos_en_passant = None
    if chessboard[arrived_index_1][arrived_index_2].tab64 in enable_case:
        if chessboard[arrived_index_1][arrived_index_2].tab64 == castling_little:
            king_side_castle(move_and_capture,start_index_1, start_index_2,arrived_index_1, arrived_index_2,screen,background,enable_case)
            return True,en_passant,pos_en_passant  # une pièce a été joué

        elif chessboard[arrived_index_1][arrived_index_2].tab64 == castling_long:
            queen_side_castle(move_and_capture,start_index_1, start_index_2,arrived_index_1, arrived_index_2,screen,background,enable_case)
            return True,en_passant,pos_en_passant # une pièce a été joué

        start_x, start_y = chessboard[start_index_1][start_index_2].get_pos()
        arrived_x, arrived_y = chessboard[arrived_index_1][arrived_index_2].get_pos()

        screen.blit(background, (arrived_x, arrived_y), area=pygame.Rect(arrived_x, arrived_y, 93.75, 93.75)) #blit morceau background sur case arrivée pour enlever pièce

        chessboard[arrived_index_1][arrived_index_2].surface = chessboard[start_index_1][start_index_2].surface #affichage sur case arrivée devient celle de case de départ
        chessboard[arrived_index_1][arrived_index_2].piece = chessboard[start_index_1][start_index_2].piece  # pièce sur case arrivée devient celle de case de départ
        chessboard[arrived_index_1][arrived_index_2].color = chessboard[start_index_1][start_index_2].piece.color
        chessboard[start_index_1][start_index_2].play_once += 1
        chessboard[arrived_index_1][arrived_index_2].play_once += 1
        chessboard[start_index_1][start_index_2].color = None
        chessboard[start_index_1][start_index_2].piece = None #efface pièce de la case de départ
        screen.blit(chessboard[arrived_index_1][arrived_index_2].surface, (arrived_x, arrived_y)) #blit sur ecran de la position de la nouvelle pièce sur case arrivée

        screen.blit(background, (start_x, start_y), area=pygame.Rect(start_x, start_y, 93.75, 93.75)) #efface l’ancienne case de départ avec le fond
        pygame.display.flip()  # MAJ de l'écran

        if chessboard[arrived_index_1][arrived_index_2].piece.name == "pawn" and color_turn == "white" and chessboard[arrived_index_1][arrived_index_2].tab64 in last_case_black:
            promotion(arrived_index_1,arrived_index_2,screen,background,color_turn)

        elif chessboard[arrived_index_1][arrived_index_2].piece.name == "pawn" and color_turn == "black" and chessboard[arrived_index_1][arrived_index_2].tab64 in last_case_white:
            promotion(arrived_index_1,arrived_index_2,screen,background,color_turn)

        if chessboard[arrived_index_1][arrived_index_2].piece.name == "pawn" and color_turn == "white" and arrived_index_2 == start_index_2 + 2:
            en_passant = 1
            pos_en_passant = chessboard[arrived_index_1][arrived_index_2].tab64
        elif chessboard[arrived_index_1][arrived_index_2].piece.name == "pawn" and color_turn == "black" and arrived_index_2 == start_index_2 - 2:
            en_passant = 1
            pos_en_passant = chessboard[arrived_index_1][arrived_index_2].tab64

        if en_passant == 1 and chessboard[arrived_index_1][arrived_index_2].tab64 == chessboard[start_index_1][start_index_2].tab64 - 9:
            en_passant = 0
            x,y = chessboard[arrived_index_1][arrived_index_2 - 1].get_pos()
            chessboard[arrived_index_1][arrived_index_2 - 1].color = None
            chessboard[arrived_index_1][arrived_index_2 - 1].piece = None  # efface pièce de la case de départ
            screen.blit(background, (x,y), area=pygame.Rect(x,y, 93.75,93.75))  # efface l’ancienne case de départ avec le fond
            pygame.display.flip()  # MAJ de l'écran

        elif en_passant == 1 and chessboard[arrived_index_1][arrived_index_2].tab64 == chessboard[start_index_1][start_index_2].tab64 - 11:
            en_passant = 0

            x,y = chessboard[arrived_index_1][arrived_index_2 - 1].get_pos()
            chessboard[arrived_index_1][arrived_index_2 - 1].color = None
            chessboard[arrived_index_1][arrived_index_2 - 1].piece = None  # efface pièce de la case de départ
            screen.blit(background, (x, y),area=pygame.Rect(x, y, 93.75, 93.75))  # efface l’ancienne case de départ avec le fond
            pygame.display.flip()  # MAJ de l'écran

        elif en_passant == 1 and chessboard[arrived_index_1][arrived_index_2].tab64 == chessboard[start_index_1][start_index_2].tab64 + 9:
            en_passant = 0

            x,y = chessboard[arrived_index_1][arrived_index_2 + 1].get_pos()
            chessboard[arrived_index_1][arrived_index_2 + 1].color = None
            chessboard[arrived_index_1][arrived_index_2 + 1].piece = None  # efface pièce de la case de départ
            screen.blit(background, (x, y),area=pygame.Rect(x, y, 93.75, 93.75))  # efface l’ancienne case de départ avec le fond
            pygame.display.flip()  # MAJ de l'écran

        elif en_passant == 1 and chessboard[arrived_index_1][arrived_index_2].tab64 == chessboard[start_index_1][start_index_2].tab64 + 11:
            en_passant = 0
            x,y = chessboard[arrived_index_1][arrived_index_2 + 1].get_pos()
            chessboard[arrived_index_1][arrived_index_2 + 1].color = None
            chessboard[arrived_index_1][arrived_index_2 + 1].piece = None  # efface pièce de la case de départ
            screen.blit(background, (x, y),area=pygame.Rect(x, y, 93.75, 93.75))  # efface l’ancienne case de départ avec le fond
            pygame.display.flip()  # MAJ de l'écran


        return True,en_passant,pos_en_passant #une pièce a été joué

    else:
        return False,en_passant,pos_en_passant #une pièce n'est pas joué

def who_is_the_turn(color_turn,play,turn,global_turn):#fonction pour savoir qui joue le tour
    if color_turn == "white" and play:
        color_turn = "black"
        turn += 0.5
    elif color_turn == "black" and play:
        color_turn = "white"
        turn += 0.5
    if turn == 1:
        global_turn += 1
        turn = 0
    play = False
    return color_turn,play,turn,global_turn

def display_state(color_turn,global_turn,check):
    print(f"NUMBER TURN: {global_turn}")
    print(f"COLOR TURN: {color_turn}\n")
    if check:
        print(f"CHECK")




























































