from case import chessboard

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

