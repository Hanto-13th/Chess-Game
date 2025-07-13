import pygame
from case import chessboard
from piece import W_queen,W_rook,W_bishop,W_knight,B_queen,B_rook,B_bishop,B_knight

def checkmate(possible_movement,check,color_king_in_check,en_passant,pos_en_passant):
    """Function to look about a checkmate, it will verify if many conditions are respected if all False it's checkmate.

    the arguments are: -possible_movement,check to view there is a check and compute all the cases which attack and defend the king
     -color_king_in_check to know the king color attack
     -en_passant,pos_en_passant just in arg for possible_movement function"""
    if check:
        king_tab64 = None
        attackers = []
        case_protected = []
        case_attacked = []
        move_king = []

    #get all king movement, cases attacked, defended and identified the attackers
        for row in chessboard:
            for case in row:
                if case.piece is not None and case.piece.name == "king" and case.piece.color == color_king_in_check: #recherche du roi et de ses mouvements
                    king_tab64 = case.tab64
                    i,j = find_attack(case.get_pos())
                    king_pos = (i,j)
                    move_king,_,_ = possible_movement(i,j,en_passant,pos_en_passant)
                elif case.piece is not None and case.piece.color == color_king_in_check:
                    i, j = find_attack(case.get_pos())
                    moves, _, _ = possible_movement(i, j,en_passant,pos_en_passant)
                    case_protected.extend(moves)
                elif case.piece is not None and case.piece.color != color_king_in_check:#recherche des attaquants
                    i,j = find_attack(case.get_pos())
                    moves, _, _ = possible_movement(i, j,en_passant,pos_en_passant)
                    case_attacked.extend(moves)
                    if king_tab64 in moves:
                        attackers.append((i, j))
        #if king not found
        if not move_king:
            print("Error: king not find")
            return False
        #if more 2 attackers, automatically checkmate
        if len(attackers) >= 2:
            return True
        #if any move of king is free, no checkmate
        safe_squares = any(move not in case_attacked for move in move_king)
        if safe_squares:
            return False

        #if piece which attack could be capture, no checkmate
        for attacker in attackers:
            x,y = attacker
            attacker_tab64 = chessboard[x][y].tab64
            if attacker_tab64 in case_protected:
                return False

        #detect all pieces attackers
        king_x,king_y = king_pos
        for attacker in attackers:
            attacker_x,attacker_y = attacker
            attacker_piece = chessboard[attacker_x][attacker_y].piece

            #if attacker is knight, no intermediate case, it's capture or mat
            if attacker_piece.name == "knight":
                continue
            #compute the distance between the king and attacker and show if a piece can intercept the capture, if not all conditions
            #are done and it's a checkmate
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


def stalemate(possible_movement, color_turn, check,case_attacked_by_white,case_attacked_by_black,en_passant,pos_en_passant):
    """Function to detect stalemate if king not check, the arguments are :

    -possible_movement,en_passant,pos_en_passant to have the legal move
    -color_turn, check to get the state of game
    -case_attacked_by_white,case_attacked_by_black to check if there is a free case in all attacked case"""
    if not check:
        legal_move = []
        #look about all possibles and legal moves
        for row in chessboard:
            for case in row:
                if case.piece is not None and case.piece.color == color_turn:
                    i, j = find_attack((case.get_pos()))
                    moves, _, _ = possible_movement(i, j,en_passant,pos_en_passant)
                    legal_move.extend(moves)

        legal_move = list(set(legal_move))
        #if all legal move of king in case attacked so it's stalemate
        if case_attacked_by_white is not None and color_turn == "black" and all(move in case_attacked_by_white for move in legal_move):
            return True

        if case_attacked_by_black is not None and color_turn == "white" and all(move in case_attacked_by_black for move in legal_move):
            return True

        return False



def is_check(possible_movement,en_passant,pos_en_passant):
    """Function to detect if a king is checking. the arguments are :

    -possible_movement,en_passant,pos_en_passant to detect if a king is on attacking case"""
    attack_case_by_white = []
    attack_case_by_black = []
    king_pos_white = None
    king_pos_black = None
    for row in chessboard:
        for case in row:
            #find the kings
            if case.piece is not None and case.piece.name == "king":
                if case.piece.color == "white":
                    king_pos_white = case.tab64
                elif case.piece.color == "black":
                    king_pos_black = case.tab64
            #find cases attacked by white
            if case.piece is not None and case.piece.color == "white":
                i,j = find_attack(case.get_pos())
                attack,_,_ = possible_movement(i,j,en_passant,pos_en_passant)
                attack_case_by_white.extend(attack)
            #find cases attacked by black
            elif case.piece is not None and case.piece.color == "black":
                i,j = find_attack(case.get_pos())
                attack,_,_ = possible_movement(i,j,en_passant,pos_en_passant)
                attack_case_by_black.extend(attack)
    #if a king in attack list so it's check
    attack_list_by_white = list(set([x for x in attack_case_by_white if x is not None and 21 <= x <= 98]))
    attack_list_by_black = list(set([x for x in attack_case_by_black if x is not None and 21 <= x <= 98]))
    if king_pos_white in attack_list_by_black:
        return True,"white",None,None
    elif king_pos_black in attack_list_by_white:
        return True,"black",None,None

    return False,None,attack_list_by_white,attack_list_by_black


def checking(possible_movement, start_index_1, start_index_2, arrived_index_1, arrived_index_2,color_turn,en_passant,pos_en_passant):
    """Function to get if a king with the next move leaves his check state. The arguments are :

     -possible_movement,en_passant,pos_en_passant to detect if a king is on attacking case
     -start_index_1, start_index_2, arrived_index_1, arrived_index_2,color_turn to manipulate the pieces"""

    #simule the next movement
    piece_depart = chessboard[start_index_1][start_index_2].piece
    piece_arrivee = chessboard[arrived_index_1][arrived_index_2].piece
    chessboard[arrived_index_1][arrived_index_2].piece = piece_depart
    chessboard[start_index_1][start_index_2].piece = None

    #look if after the movement the king is still check
    attack_case_by_white = []
    attack_case_by_black = []
    king_pos_white = None
    king_pos_black = None
    for row in chessboard:
        for case in row:
            if case.piece is not None and case.piece.name == "king":
                if case.piece.color == "white":
                    king_pos_white = case.tab64
                elif case.piece.color == "black":
                    king_pos_black = case.tab64

            if case.piece is not None and case.piece.color == "white":
                i, j = find_attack(case.get_pos())
                attack, _, _ = possible_movement(i, j,en_passant,pos_en_passant)
                attack_case_by_white.extend(attack)
            elif case.piece is not None and case.piece.color == "black":
                i, j = find_attack(case.get_pos())
                attack, _, _ = possible_movement(i, j,en_passant,pos_en_passant)
                attack_case_by_black.extend(attack)

    attack_list_by_white = list(set([x for x in attack_case_by_white if x is not None and 21 <= x <= 98]))
    attack_list_by_black = list(set([x for x in attack_case_by_black if x is not None and 21 <= x <= 98]))

    #reset the changes of movement simulation
    chessboard[start_index_1][start_index_2].piece = piece_depart
    chessboard[arrived_index_1][arrived_index_2].piece = piece_arrivee
    #if the king still in the case attacked even the movement simulate, is still check, and you can't move the piece
    if king_pos_black in attack_list_by_white and color_turn == "black":
        return True
    elif king_pos_white in attack_list_by_black and color_turn == "white":
        return True

    return False




def find_attack(tuple_pos):
    """This function translate the tuple position of a piece into his case equivalent (cf. coord_case in CONSTANTS FILE),
    (Exemple: x,y --> case C4).Using for all the check,checkmate and stalemate function.

    The argument is : -tuple_pos of piece you want to translate"""
    x, y = tuple_pos
    coord_index_x = None
    coord_index_y = None


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
    """This function detect the capacities of castling, arguments are :

    -color,start_tab64 to manipulate the pieces"""
    castling_long = None
    castling_little = None
    #if rooks are not moved during the game, compute the direction vector and return him
    if color == "white":
        if chessboard[0][0].play_once == 0:
            castling_long = start_tab64 - 2
        if chessboard[7][0].play_once == 0:
            castling_little = start_tab64 + 2
        return castling_little,castling_long
    elif color == "black":
        if chessboard[0][7].play_once == 0:
            castling_long = start_tab64 - 2
        if chessboard[7][7].play_once == 0:
            castling_little = start_tab64 + 2
        return castling_little,castling_long


def king_side_castle(move_and_capture,start_index_1, start_index_2,arrived_index_1, arrived_index_2,screen,background,enable_case):
    """Function to move and display the little castling on the screen. It takes in arguments :

    -move_and_capture,start_index_1, start_index_2,arrived_index_1, arrived_index_2,screen,background to display and execute the movement
    -enable_case to show the way"""
    #same thing with the move_and_capture function but with add rook movement
    move_and_capture(screen, background, start_index_1, start_index_2, arrived_index_1, arrived_index_2, enable_case,castling_little=None, castling_long=None,en_passant=None,color_turn=None)

    rook_start_x, rook_start_y = chessboard[arrived_index_1 + 1][arrived_index_2].get_pos()
    rook_arrived_x, rook_arrived_y = chessboard[arrived_index_1 - 1][arrived_index_2].get_pos()

    screen.blit(background, (rook_arrived_x, rook_arrived_y), area=pygame.Rect(rook_arrived_x, rook_arrived_y, 93.75,93.75))

    chessboard[arrived_index_1 - 1][arrived_index_2].surface = chessboard[arrived_index_1 + 1][arrived_index_2].surface
    chessboard[arrived_index_1 - 1][arrived_index_2].piece = chessboard[arrived_index_1 + 1][arrived_index_2].piece
    chessboard[arrived_index_1 - 1][arrived_index_2].color = chessboard[arrived_index_1 + 1][arrived_index_2].piece.color

    chessboard[arrived_index_1 + 1][arrived_index_2].play_once += 1
    chessboard[arrived_index_1 + 1][arrived_index_2].color = None
    chessboard[arrived_index_1 + 1][arrived_index_2].piece = None
    screen.blit(chessboard[arrived_index_1 - 1][arrived_index_2].surface,(rook_arrived_x, rook_arrived_y))

    screen.blit(background, (rook_start_x, rook_start_y), area=pygame.Rect(rook_start_x, rook_start_y, 93.75,93.75))


def queen_side_castle(move_and_capture,start_index_1, start_index_2,arrived_index_1, arrived_index_2,screen,background,enable_case):
    """Function to move and display the long castling on the screen. It takes in arguments :

        -move_and_capture,start_index_1, start_index_2,arrived_index_1, arrived_index_2,screen,background to display and execute the movement
        -enable_case to show the way"""

    # same thing with the move_and_capture function but with add rook movement
    move_and_capture(screen, background, start_index_1, start_index_2, arrived_index_1, arrived_index_2, enable_case,castling_little=None, castling_long=None,en_passant = None,color_turn = None)

    rook_start_x, rook_start_y = chessboard[arrived_index_1 - 2][arrived_index_2].get_pos()
    rook_arrived_x, rook_arrived_y = chessboard[arrived_index_1 + 1][arrived_index_2].get_pos()

    screen.blit(background, (rook_arrived_x, rook_arrived_y), area=pygame.Rect(rook_arrived_x, rook_arrived_y, 93.75,93.75))

    chessboard[arrived_index_1 + 1][arrived_index_2].surface = chessboard[arrived_index_1 - 2][arrived_index_2].surface
    chessboard[arrived_index_1 + 1][arrived_index_2].piece = chessboard[arrived_index_1 - 2][arrived_index_2].piece
    chessboard[arrived_index_1 + 1][arrived_index_2].color = chessboard[arrived_index_1 - 2][arrived_index_2].piece.color

    chessboard[arrived_index_1 - 2][arrived_index_2].play_once += 1
    chessboard[arrived_index_1 - 2][arrived_index_2].color = None
    chessboard[arrived_index_1 - 2][arrived_index_2].piece = None
    screen.blit(chessboard[arrived_index_1 + 1][arrived_index_2].surface,(rook_arrived_x, rook_arrived_y))

    screen.blit(background, (rook_start_x, rook_start_y), area=pygame.Rect(rook_start_x, rook_start_y, 93.75,93.75))


def promotion(arrived_index_1,arrived_index_2,screen,background,color_turn):
    """Function to promote the pawn using the python shell. Arguments are :

    -arrived_index_1,arrived_index_2,screen,background,color_turn to modify the pawn into another pieces choose by player"""

    #the player choose a piece with the command shell and if result not available, reset the process
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
            screen.blit(chessboard[arrived_index_1][arrived_index_2].surface,(x, y))

        case "k":
            if color_turn == "white":
                chessboard[arrived_index_1][arrived_index_2].piece = W_knight
                chessboard[arrived_index_1][arrived_index_2].surface = chessboard[arrived_index_1][arrived_index_2].piece.get_sprite()
            elif color_turn == "black":
                chessboard[arrived_index_1][arrived_index_2].piece = B_knight
                chessboard[arrived_index_1][arrived_index_2].surface = chessboard[arrived_index_1][arrived_index_2].piece.get_sprite()

            screen.blit(background, (x, y), area=pygame.Rect(x, y, 93.75, 93.75))
            screen.blit(chessboard[arrived_index_1][arrived_index_2].surface,(x, y))

        case "b":
            if color_turn == "white":
                chessboard[arrived_index_1][arrived_index_2].piece = W_bishop
                chessboard[arrived_index_1][arrived_index_2].surface = chessboard[arrived_index_1][arrived_index_2].piece.get_sprite()
            elif color_turn == "black":
                chessboard[arrived_index_1][arrived_index_2].piece = B_bishop
                chessboard[arrived_index_1][arrived_index_2].surface = chessboard[arrived_index_1][arrived_index_2].piece.get_sprite()

            screen.blit(background, (x, y), area=pygame.Rect(x, y, 93.75, 93.75))
            screen.blit(chessboard[arrived_index_1][arrived_index_2].surface,(x, y))


        case "r":
            if color_turn == "white":
                chessboard[arrived_index_1][arrived_index_2].piece = W_rook
                chessboard[arrived_index_1][arrived_index_2].surface = chessboard[arrived_index_1][arrived_index_2].piece.get_sprite()
            elif color_turn == "black":
                chessboard[arrived_index_1][arrived_index_2].piece = B_rook
                chessboard[arrived_index_1][arrived_index_2].surface = chessboard[arrived_index_1][arrived_index_2].piece.get_sprite()

            screen.blit(background, (x, y), area=pygame.Rect(x, y, 93.75, 93.75))
            screen.blit(chessboard[arrived_index_1][arrived_index_2].surface,(x, y))

    pygame.display.flip()  #Screen Update


def capture_en_passant(color_piece, arrived_index_1, arrived_index_2, screen, background):
    """Function to display capture en passant on the screen. Arguments are :

    -color_piece, arrived_index_1, arrived_index_2, screen, background to know the piece to remove"""

    #remove the piece en passant in function of color and coordinates of piece
    if color_piece == "white":
        x, y = chessboard[arrived_index_1][arrived_index_2 - 1].get_pos()
        chessboard[arrived_index_1][arrived_index_2 - 1].color = None
        chessboard[arrived_index_1][arrived_index_2 - 1].piece = None
        screen.blit(background, (x, y),area=pygame.Rect(x, y, 93.75, 93.75))
        pygame.display.flip()

    elif color_piece == "black":
        x, y = chessboard[arrived_index_1][arrived_index_2 + 1].get_pos()
        chessboard[arrived_index_1][arrived_index_2 + 1].color = None
        chessboard[arrived_index_1][arrived_index_2 + 1].piece = None
        screen.blit(background, (x, y),area=pygame.Rect(x, y, 93.75, 93.75))
        pygame.display.flip()


