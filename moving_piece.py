from case import chessboard, tab64_to_tab120
from piece import *
from constants import move_pawn_white,move_pawn_black,move_king,move_knight,move_queen,move_rook,move_bishop,last_case_white,last_case_black
from rules import is_castling,king_side_castle,queen_side_castle,promotion,capture_en_passant


def find_coord(pos_click):
    """This function is to translate the coordinates of player click on the screen into
    coordinates for each chessboard cases (coord: x,y --> case C4),

    it takes one argument: the output of player click
    """
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
    """The function to know all possible movement of a piece, for each piece we take their possible vector of directions
     in the CONSTANTS FILE, and we test if the piece no encounter another piece or get out the board, if not
     we add the case in the case available to move. the arguments are:

     - start_index_1,start_index_2 : the start coordinates of piece
     - en_passant,pos_en_passant : ONLY FOR THE PAWN , to know if possible to capture en passant"""
    case_with_piece = []
    possible_case = []
    castling_little, castling_long = None,None

    #add all the case with piece to detect collision
    for row in chessboard:
        for case in row:
            if case.piece is not None:
                case_with_piece.append(case.tab64)

    if chessboard[start_index_1][start_index_2].piece is None:
        return None,None,None

    #---------------------------------
    # Movement of white and black Pawn
    #---------------------------------

    if chessboard[start_index_1][start_index_2].piece.name == "pawn" and chessboard[start_index_1][start_index_2].piece.color == "white":
        start_tab64 = chessboard[start_index_1][start_index_2].tab64
        directions = move_pawn_white

        for direction in directions:
            if direction == -10:
                next_tab64 = start_tab64 + direction
                if tab64_to_tab120(next_tab64) != -1 and next_tab64 not in case_with_piece:
                    possible_case.append(next_tab64)
            #for double push
            if chessboard[start_index_1][start_index_2].play_once == 0:
                next_tab64 = start_tab64 - 20
                obstacle_to_push = start_tab64 - 10
                if tab64_to_tab120(next_tab64) != -1 and next_tab64 not in case_with_piece and obstacle_to_push not in case_with_piece:
                    possible_case.append(next_tab64)
            if direction == -11 and start_tab64 + direction in case_with_piece:
                next_tab64 = start_tab64 + direction
                if tab64_to_tab120(next_tab64) != -1:
                    possible_case.append(next_tab64)
            if direction == -9 and start_tab64 + direction in case_with_piece:
                next_tab64 = start_tab64 + direction
                if tab64_to_tab120(next_tab64) != -1:
                    possible_case.append(next_tab64)
            #for en passant
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
            if direction == 10:
                next_tab64 = start_tab64 + direction
                if tab64_to_tab120(next_tab64) != -1 and next_tab64 not in case_with_piece:
                    possible_case.append(next_tab64)
            #for double push
            if chessboard[start_index_1][start_index_2].play_once == 0:
                next_tab64 = start_tab64 + 20
                obstacle_to_push = start_tab64 + 10
                if tab64_to_tab120(next_tab64) != -1 and next_tab64 not in case_with_piece and obstacle_to_push not in case_with_piece:
                    possible_case.append(next_tab64)
            if direction == 11 and start_tab64 + direction in case_with_piece:
                next_tab64 = start_tab64 + direction
                if tab64_to_tab120(next_tab64) != -1:
                    possible_case.append(next_tab64)
            if direction == 9 and start_tab64 + direction in case_with_piece:
                next_tab64 = start_tab64 + direction
                if tab64_to_tab120(next_tab64) != -1:
                    possible_case.append(next_tab64)
            #for en passant
            if en_passant == 1 and pos_en_passant == chessboard[start_index_1][start_index_2].tab64 - 1:
                next_tab64_enpassant = start_tab64 + 9
                if tab64_to_tab120(next_tab64_enpassant) != -1:
                    possible_case.append(next_tab64_enpassant)
            if en_passant == 1 and pos_en_passant == chessboard[start_index_1][start_index_2].tab64 + 1:
                next_tab64_enpassant = start_tab64 + 11
                if tab64_to_tab120(next_tab64_enpassant) != -1:
                    possible_case.append(next_tab64_enpassant)

    #------------------------------------------------
    # Movement of King and his castling possibilities
    #------------------------------------------------

    if chessboard[start_index_1][start_index_2].piece.name == "king":
        start_tab64 = chessboard[start_index_1][start_index_2].tab64
        directions = move_king

        #to check the possibilities of castling
        if chessboard[start_index_1][start_index_2].play_once == 0:
            castling_little, castling_long = is_castling(chessboard[start_index_1][start_index_2].piece.color,start_tab64)
            if castling_little not in case_with_piece:
                possible_case.append(castling_little)
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


    #----------------------
    # Movement of the Queen
    #----------------------

    if chessboard[start_index_1][start_index_2].piece.name == "queen":
        start_tab64 = chessboard[start_index_1][start_index_2].tab64
        directions = move_queen

        for direction in directions:
            time = 1
            while True:
                next_tab64 = start_tab64 + direction * time
                if tab64_to_tab120(next_tab64) == -1:
                    break

                possible_case.append(next_tab64)

                if next_tab64 in case_with_piece:
                    break

                time += 1

    #-----------------------
    # Movement of the Bishop
    #-----------------------

    if chessboard[start_index_1][start_index_2].piece.name == "bishop":
        start_tab64 = chessboard[start_index_1][start_index_2].tab64
        directions = move_bishop

        for direction in directions:
            time = 1
            while True:
                next_tab64 = start_tab64 + direction * time
                if tab64_to_tab120(next_tab64) == -1:
                    break

                possible_case.append(next_tab64)

                if next_tab64 in case_with_piece:
                    break

                time += 1

    #-----------------------
    # Movement of the Knight
    #-----------------------
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

    #---------------------
    # Movement of the Rook
    #---------------------

    if chessboard[start_index_1][start_index_2].piece.name == "rook":
        start_tab64 = chessboard[start_index_1][start_index_2].tab64
        directions = move_rook

        for direction in directions:
            time = 1
            while True:
                next_tab64 = start_tab64 + direction * time
                if tab64_to_tab120(next_tab64) == -1:
                    break

                possible_case.append(next_tab64)

                if next_tab64 in case_with_piece:
                    break

                time += 1


    possible_case = list(filter(lambda x: tab64_to_tab120(x) != -1,list(filter(None,possible_case))))
    return possible_case,castling_little,castling_long

def move_and_capture(screen,background,start_index_1,start_index_2,arrived_index_1,arrived_index_2,enable_case,castling_little,castling_long,en_passant,color_turn):
    """Function to handle the move and the capture of the pieces, and castling, en passant or promotion.
    the function arguments are:

    - screen and background to blit on the screen or replace the piece capture or moved by part of background
    - start_index_1,start_index_2,arrived_index_1,arrived_index_2,color_turn to know the start and arrive position of piece and his color
    - enable_case to know the movement possibilities of piece which move
    - castling_little,castling_long to know the possibilities of castling and the coordinates to do
    - en_passant to know the possibilities of capture en passant"""
    pos_en_passant = None
    #if all the condition are ready, we can castle in the two sides
    if chessboard[arrived_index_1][arrived_index_2].tab64 in enable_case:
        if chessboard[arrived_index_1][arrived_index_2].tab64 == castling_little:
            king_side_castle(move_and_capture,start_index_1, start_index_2,arrived_index_1, arrived_index_2,screen,background,enable_case)
            return True,en_passant,pos_en_passant

        elif chessboard[arrived_index_1][arrived_index_2].tab64 == castling_long:
            queen_side_castle(move_and_capture,start_index_1, start_index_2,arrived_index_1, arrived_index_2,screen,background,enable_case)
            return True,en_passant,pos_en_passant

        #get the pos of start and arrive position
        start_x, start_y = chessboard[start_index_1][start_index_2].get_pos()
        arrived_x, arrived_y = chessboard[arrived_index_1][arrived_index_2].get_pos()

        #clear the arrived case
        screen.blit(background, (arrived_x, arrived_y), area=pygame.Rect(arrived_x, arrived_y, 93.75, 93.75))

        #switch information between start and arrive position and clear the start position info
        chessboard[arrived_index_1][arrived_index_2].surface = chessboard[start_index_1][start_index_2].surface
        chessboard[arrived_index_1][arrived_index_2].piece = chessboard[start_index_1][start_index_2].piece
        chessboard[arrived_index_1][arrived_index_2].color = chessboard[start_index_1][start_index_2].piece.color
        chessboard[start_index_1][start_index_2].play_once += 1
        chessboard[arrived_index_1][arrived_index_2].play_once += 1
        chessboard[start_index_1][start_index_2].color = None
        chessboard[start_index_1][start_index_2].piece = None

        #blit on the screen the new position of the piece and blit a part of background on his old pos
        screen.blit(chessboard[arrived_index_1][arrived_index_2].surface, (arrived_x, arrived_y))
        screen.blit(background, (start_x, start_y), area=pygame.Rect(start_x, start_y, 93.75, 93.75))
        pygame.display.flip()

        #if a pawn reach the last line promote him
        if chessboard[arrived_index_1][arrived_index_2].piece.name == "pawn" and color_turn == "white" and chessboard[arrived_index_1][arrived_index_2].tab64 in last_case_black:
            promotion(arrived_index_1,arrived_index_2,screen,background,color_turn)

        elif chessboard[arrived_index_1][arrived_index_2].piece.name == "pawn" and color_turn == "black" and chessboard[arrived_index_1][arrived_index_2].tab64 in last_case_white:
            promotion(arrived_index_1,arrived_index_2,screen,background,color_turn)

        #if condition are ready, we can capture en passant
        if en_passant == 1 and chessboard[arrived_index_1][arrived_index_2].piece.name == "pawn" and (chessboard[arrived_index_1][arrived_index_2].tab64 == chessboard[start_index_1][start_index_2].tab64 - 11 or chessboard[arrived_index_1][arrived_index_2].tab64 == chessboard[start_index_1][start_index_2].tab64 - 9):
            en_passant = 0
            color_piece = chessboard[arrived_index_1][arrived_index_2].piece.color
            capture_en_passant(color_piece,arrived_index_1,arrived_index_2,screen,background)

        elif en_passant == 1 and chessboard[arrived_index_1][arrived_index_2].piece.name == "pawn" and (chessboard[arrived_index_1][arrived_index_2].tab64 == chessboard[start_index_1][start_index_2].tab64 + 11 or chessboard[arrived_index_1][arrived_index_2].tab64 == chessboard[start_index_1][start_index_2].tab64 + 9):
            en_passant = 0
            color_piece = chessboard[arrived_index_1][arrived_index_2].piece.color
            capture_en_passant(color_piece, arrived_index_1, arrived_index_2, screen, background)
        else:
            en_passant = 0

        #if condition are ready, active the capture en passant feature for the other player
        if chessboard[arrived_index_1][arrived_index_2].piece.name == "pawn" and color_turn == "white" and arrived_index_2 == start_index_2 + 2:
            en_passant = 1
            pos_en_passant = chessboard[arrived_index_1][arrived_index_2].tab64
        elif chessboard[arrived_index_1][arrived_index_2].piece.name == "pawn" and color_turn == "black" and arrived_index_2 == start_index_2 - 2:
            en_passant = 1
            pos_en_passant = chessboard[arrived_index_1][arrived_index_2].tab64


        return True,en_passant,pos_en_passant

    else:
        return False,en_passant,pos_en_passant

def who_is_the_turn(color_turn,play,half_turn,global_turn):
    """Function to know who is the color turn and the number of turn, arguments are:

    - color_turn to know the color of progressing player
    - play to know if a player plays without problems
    - half_turn,global_turn to handle the number of turn plays"""
    if color_turn == "white" and play:
        color_turn = "black"
        half_turn += 0.5
    elif color_turn == "black" and play:
        color_turn = "white"
        half_turn += 0.5
    if half_turn == 1:
        global_turn += 1
        half_turn = 0
    play = False
    return color_turn,play,half_turn,global_turn

def display_state(color_turn,global_turn,check):
    """Function to display the state of part."""
    print(f"NUMBER TURN: {global_turn}")
    print(f"COLOR TURN: {color_turn}\n")
    if check:
        print(f"CHECK")





























































