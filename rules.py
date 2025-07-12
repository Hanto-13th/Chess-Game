import pygame
from case import chessboard
from piece import W_queen,W_rook,W_bishop,W_knight,B_queen,B_rook,B_bishop,B_knight

def checkmate(possible_movement,check,color_king_in_check):
    #regarder si echec
    if check:
        king_tab64 = None
        attackers = []
        case_protected = []
        case_attacked = []
        move_king = []

    #si oui regarder les deplacement du roi
        for row in chessboard:
            for case in row:
                if case.piece is not None and case.piece.name == "king" and case.piece.color == color_king_in_check: #recherche du roi et de ses mouvements
                    king_tab64 = case.tab64
                    i,j = find_attack(case.get_pos())
                    king_pos = (i,j)
                    move_king,_,_ = possible_movement(i,j)
                elif case.piece is not None and case.piece.color == color_king_in_check:
                    i, j = find_attack(case.get_pos())
                    moves, _, _ = possible_movement(i, j)
                    case_protected.extend(moves)
                elif case.piece is not None and case.piece.color != color_king_in_check:#recherche des attaquants
                    i,j = find_attack(case.get_pos())
                    moves, _, _ = possible_movement(i, j)
                    case_attacked.extend(moves)
                    if king_tab64 in moves:
                        attackers.append((i, j))

        if not move_king:
            print("Error: king not find")
            return False  # on considère pas mat pour éviter crash
        if len(attackers) >= 2:
            return True
        # si pas dans liste alors pas mat
        safe_squares = any(move not in case_attacked for move in move_king)

        if safe_squares:
            return False

    # sinon regarder si piece qui met en echec est capturable
        for attacker in attackers:
            x,y = attacker
            attacker_tab64 = chessboard[x][y].tab64
            if attacker_tab64 in case_protected:
                return False

        king_x,king_y = king_pos
        for attacker in attackers:
            attacker_x,attacker_y = attacker
            attacker_piece = chessboard[attacker_x][attacker_y].piece

            # Si cavalier, pas de case intermédiaire : soit on le capture, soit c’est mat
            if attacker_piece.name == "knight":
                continue

            case_between_king_and_attacker = []

            dist_x = attacker_x - king_x
            dist_y = attacker_y - king_y
            step_x = (dist_x // abs(dist_x)) if dist_x != 0 else 0
            step_y = (dist_y // abs(dist_y)) if dist_y != 0 else 0
            i, j = king_x + step_x, king_y + step_y
            while (i,j) != (attacker_x,attacker_y):
                case_between_king_and_attacker.append(chessboard[i][j].tab64)
                i += step_x
                j += step_y

            if any(tab64 in case_protected for tab64 in case_between_king_and_attacker):
                return False

        return True


def stalemate(possible_movement, color_turn, check,case_attacked_by_white,case_attacked_by_black):
    if not check:
        legal_move = []

        for row in chessboard:
            for case in row:
                if case.piece is not None and case.piece.color == color_turn:
                    i, j = find_attack((case.get_pos()))
                    moves, _, _ = possible_movement(i, j)
                    legal_move.extend(moves)

        legal_move = list(set(legal_move))

        if case_attacked_by_white is not None and color_turn == "black" and all(move in case_attacked_by_white for move in legal_move):
            return True # Pas pat, il y a un coup non attaqué

        if case_attacked_by_black is not None and color_turn == "white" and all(move in case_attacked_by_black for move in legal_move):
            return True  # Pas pat, il y a un coup non attaqué

        return False



def is_check(possible_movement):
    attack_case_by_white = []
    attack_case_by_black = []
    king_pos_white = None
    king_pos_black = None
    for row in chessboard:
        for case in row:
            if case.piece is not None and case.piece.name == "king":#recuperation pos des rois
                if case.piece.color == "white":
                    king_pos_white = case.tab64
                elif case.piece.color == "black":
                    king_pos_black = case.tab64
            if case.piece is not None and case.piece.color == "white": #Regarde toute les cases attaqué par piece blanches
                i,j = find_attack(case.get_pos()) #on cherche toute les cases attaqué
                attack,_,_ = possible_movement(i,j)
                attack_case_by_white.extend(attack)
            elif case.piece is not None and case.piece.color == "black": #Regarde toute les cases attaqué par piece noires
                i,j = find_attack(case.get_pos()) #on cherche toute les cases attaqué
                attack,_,_ = possible_movement(i,j)
                attack_case_by_black.extend(attack)
    attack_list_by_white = list(set([x for x in attack_case_by_white if x is not None and 21 <= x <= 98]))
    attack_list_by_black = list(set([x for x in attack_case_by_black if x is not None and 21 <= x <= 98]))
    if king_pos_white in attack_list_by_black:
        return True,"white",None,None
    elif king_pos_black in attack_list_by_white:
        return True,"black",None,None

    return False,None,attack_list_by_white,attack_list_by_black
#si roi adverse est dans cette liste alors echec

def checking(possible_movement, start_index_1, start_index_2, arrived_index_1, arrived_index_2,color_turn):
    # Sauvegarde des pièces pour rollback
    piece_depart = chessboard[start_index_1][start_index_2].piece
    piece_arrivee = chessboard[arrived_index_1][arrived_index_2].piece

    # Simule le déplacement
    chessboard[arrived_index_1][arrived_index_2].piece = piece_depart
    chessboard[start_index_1][start_index_2].piece = None

    attack_case_by_white = []
    attack_case_by_black = []
    king_pos_white = None
    king_pos_black = None
    for row in chessboard:
        for case in row:
            if case.piece is not None and case.piece.name == "king":  # recuperation pos des rois
                if case.piece.color == "white":
                    king_pos_white = case.tab64
                elif case.piece.color == "black":
                    king_pos_black = case.tab64

            if case.piece is not None and case.piece.color == "white":  # Regarde toute les cases attaqué par piece blanches
                i, j = find_attack(case.get_pos())  # on cherche toute les cases attaqué
                attack, _, _ = possible_movement(i, j)
                attack_case_by_white.extend(attack)
            elif case.piece is not None and case.piece.color == "black":  # Regarde toute les cases attaqué par piece noires
                i, j = find_attack(case.get_pos())  # on cherche toute les cases attaqué
                attack, _, _ = possible_movement(i, j)
                attack_case_by_black.extend(attack)


    attack_list_by_white = list(set([x for x in attack_case_by_white if x is not None and 21 <= x <= 98]))
    attack_list_by_black = list(set([x for x in attack_case_by_black if x is not None and 21 <= x <= 98]))
    chessboard[start_index_1][start_index_2].piece = piece_depart
    chessboard[arrived_index_1][arrived_index_2].piece = piece_arrivee
    if king_pos_black in attack_list_by_white and color_turn == "black":
        return True
    elif king_pos_white in attack_list_by_black and color_turn == "white":
        return True

    return False


# si roi adverse est dans cette liste alors echec

def find_attack(tuple_pos):
    x, y = tuple_pos
    coord_index_x = None
    coord_index_y = None

    # X
    if 0 <= x < 93.75:
        coord_index_x = 0
    elif 93.75 <= x < 187.5:
        coord_index_x = 1
    elif 187.5 <= x < 281.25:
        coord_index_x = 2
    elif 281.25 <= x < 375:
        coord_index_x = 3
    elif 375 <= x < 468.75:
        coord_index_x = 4
    elif 468.75 <= x < 562.5:
        coord_index_x = 5
    elif 562.5 <= x < 656.25:
        coord_index_x = 6
    elif 656.25 <= x <= 750:
        coord_index_x = 7

    # Y
    if 0 <= y < 93.75:
        coord_index_y = 7
    elif 93.75 <= y < 187.5:
        coord_index_y = 6
    elif 187.5 <= y < 281.25:
        coord_index_y = 5
    elif 281.25 <= y < 375:
        coord_index_y = 4
    elif 375 <= y < 468.75:
        coord_index_y = 3
    elif 468.75 <= y < 562.5:
        coord_index_y = 2
    elif 562.5 <= y < 656.25:
        coord_index_y = 1
    elif 656.25 <= y <= 750:
        coord_index_y = 0

    return coord_index_x, coord_index_y


def is_castling(color,start_tab64):
    castling_long = None
    castling_little = None
    if color == "white":
        if chessboard[0][0].play_once == 0: #si tour grand roque a pas bougé
            castling_long = start_tab64 - 2 #alors ajout vecteur directionnel dans variable
        if chessboard[7][0].play_once == 0:
            castling_little = start_tab64 + 2
        return castling_little,castling_long
    elif color == "black":
        if chessboard[0][7].play_once == 0: #si tour grand roque a pas bougé
            castling_long = start_tab64 - 2 #alors ajout vecteur directionnel dans variable
        if chessboard[7][7].play_once == 0:
            castling_little = start_tab64 + 2
        return castling_little,castling_long


def king_side_castle(move_and_capture,start_index_1, start_index_2,arrived_index_1, arrived_index_2,screen,background,enable_case):

    move_and_capture(screen, background, start_index_1, start_index_2, arrived_index_1, arrived_index_2, enable_case,castling_little=None, castling_long=None)

    rook_start_x, rook_start_y = chessboard[arrived_index_1 + 1][arrived_index_2].get_pos()
    rook_arrived_x, rook_arrived_y = chessboard[arrived_index_1 - 1][arrived_index_2].get_pos()

    screen.blit(background, (rook_arrived_x, rook_arrived_y), area=pygame.Rect(rook_arrived_x, rook_arrived_y, 93.75,93.75))  # blit morceau background sur case arrivée pour enlever pièce

    chessboard[arrived_index_1 - 1][arrived_index_2].surface = chessboard[arrived_index_1 + 1][arrived_index_2].surface
    chessboard[arrived_index_1 - 1][arrived_index_2].piece = chessboard[arrived_index_1 + 1][arrived_index_2].piece  # pièce sur case arrivée devient celle de case de départ
    chessboard[arrived_index_1 - 1][arrived_index_2].color = chessboard[arrived_index_1 + 1][arrived_index_2].piece.color

    chessboard[arrived_index_1 + 1][arrived_index_2].play_once += 1

    chessboard[arrived_index_1 + 1][arrived_index_2].color = None
    chessboard[arrived_index_1 + 1][arrived_index_2].piece = None  # efface pièce de la case de départ
    screen.blit(chessboard[arrived_index_1 - 1][arrived_index_2].surface,(rook_arrived_x, rook_arrived_y))  # blit sur ecran de la position de la nouvelle pièce sur case arrivée

    screen.blit(background, (rook_start_x, rook_start_y), area=pygame.Rect(rook_start_x, rook_start_y, 93.75,93.75))  # efface l’ancienne case de départ avec le fond


def queen_side_castle(move_and_capture,start_index_1, start_index_2,arrived_index_1, arrived_index_2,screen,background,enable_case):

    move_and_capture(screen, background, start_index_1, start_index_2, arrived_index_1, arrived_index_2, enable_case,castling_little=None, castling_long=None)

    rook_start_x, rook_start_y = chessboard[arrived_index_1 - 2][arrived_index_2].get_pos()
    rook_arrived_x, rook_arrived_y = chessboard[arrived_index_1 + 1][arrived_index_2].get_pos()

    screen.blit(background, (rook_arrived_x, rook_arrived_y), area=pygame.Rect(rook_arrived_x, rook_arrived_y, 93.75,93.75))  # blit morceau background sur case arrivée pour enlever pièce

    chessboard[arrived_index_1 + 1][arrived_index_2].surface = chessboard[arrived_index_1 - 2][arrived_index_2].surface
    chessboard[arrived_index_1 + 1][arrived_index_2].piece = chessboard[arrived_index_1 - 2][arrived_index_2].piece  # pièce sur case arrivée devient celle de case de départ
    chessboard[arrived_index_1 + 1][arrived_index_2].color = chessboard[arrived_index_1 - 2][arrived_index_2].piece.color

    chessboard[arrived_index_1 - 2][arrived_index_2].play_once += 1

    chessboard[arrived_index_1 - 2][arrived_index_2].color = None
    chessboard[arrived_index_1 - 2][arrived_index_2].piece = None  # efface pièce de la case de départ
    screen.blit(chessboard[arrived_index_1 + 1][arrived_index_2].surface,(rook_arrived_x, rook_arrived_y))  # blit sur ecran de la position de la nouvelle pièce sur case arrivée

    screen.blit(background, (rook_start_x, rook_start_y), area=pygame.Rect(rook_start_x, rook_start_y, 93.75,93.75))  # efface l’ancienne case de départ avec le fond


def promotion(arrived_index_1,arrived_index_2,screen,background,color_turn):
    x,y = chessboard[arrived_index_1][arrived_index_2].get_pos()
    list_promo = ["q","k","b","r"]
    promotion_piece = input("Choose a piece and press Enter (q for queen,k for knight,b for bishop or r for rook): ")
    while promotion_piece not in list_promo:
        print("ERROR CHOOSE A VALID ISSUE !")
        promotion_piece = input("Choose a piece and press Enter (q for queen,k for knight,b for bishop or r for rook): ")

    match promotion_piece:
        case "q":
            if color_turn == "white":
                chessboard[arrived_index_1][arrived_index_2].piece = W_queen
                chessboard[arrived_index_1][arrived_index_2].surface = chessboard[arrived_index_1][arrived_index_2].piece.get_sprite()
            elif color_turn == "black":
                chessboard[arrived_index_1][arrived_index_2].piece = B_queen
                chessboard[arrived_index_1][arrived_index_2].surface = chessboard[arrived_index_1][arrived_index_2].piece.get_sprite()

            screen.blit(background, (x, y), area=pygame.Rect(x, y, 93.75, 93.75))
            screen.blit(chessboard[arrived_index_1][arrived_index_2].surface,(x, y))  # blit sur ecran de la position de la nouvelle pièce sur case arrivée
            pygame.display.flip()



        case "k":
            if color_turn == "white":
                chessboard[arrived_index_1][arrived_index_2].piece = W_knight
                chessboard[arrived_index_1][arrived_index_2].surface = chessboard[arrived_index_1][arrived_index_2].piece.get_sprite()
            elif color_turn == "black":
                chessboard[arrived_index_1][arrived_index_2].piece = B_knight
                chessboard[arrived_index_1][arrived_index_2].surface = chessboard[arrived_index_1][arrived_index_2].piece.get_sprite()

            screen.blit(background, (x, y), area=pygame.Rect(x, y, 93.75, 93.75))
            screen.blit(chessboard[arrived_index_1][arrived_index_2].surface,(x, y))  # blit sur ecran de la position de la nouvelle pièce sur case arrivée
            pygame.display.flip()



        case "b":
            if color_turn == "white":
                chessboard[arrived_index_1][arrived_index_2].piece = W_bishop
                chessboard[arrived_index_1][arrived_index_2].surface = chessboard[arrived_index_1][arrived_index_2].piece.get_sprite()
            elif color_turn == "black":
                chessboard[arrived_index_1][arrived_index_2].piece = B_bishop
                chessboard[arrived_index_1][arrived_index_2].surface = chessboard[arrived_index_1][arrived_index_2].piece.get_sprite()

            screen.blit(background, (x, y), area=pygame.Rect(x, y, 93.75, 93.75))
            screen.blit(chessboard[arrived_index_1][arrived_index_2].surface,(x, y))  # blit sur ecran de la position de la nouvelle pièce sur case arrivée
            pygame.display.flip()


        case "r":
            if color_turn == "white":
                chessboard[arrived_index_1][arrived_index_2].piece = W_rook
                chessboard[arrived_index_1][arrived_index_2].surface = chessboard[arrived_index_1][arrived_index_2].piece.get_sprite()
            elif color_turn == "black":
                chessboard[arrived_index_1][arrived_index_2].piece = B_rook
                chessboard[arrived_index_1][arrived_index_2].surface = chessboard[arrived_index_1][arrived_index_2].piece.get_sprite()

            screen.blit(background, (x, y), area=pygame.Rect(x, y, 93.75, 93.75))
            screen.blit(chessboard[arrived_index_1][arrived_index_2].surface,(x, y))  # blit sur ecran de la position de la nouvelle pièce sur case arrivée
            pygame.display.flip()


