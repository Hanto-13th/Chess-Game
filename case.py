import pygame
from constants import COORD_CASE, TAB120

#-----------------------
# Creation of Case Class
#-----------------------
# With all his attributes to her manipulations

class Case:
    def __init__(self,surface,pos,piece,tab64,color,play_once):
        self.surface = surface
        self.pos = pos
        self.piece = piece
        self.tab64 = tab64
        self.color = color
        self.play_once = play_once

    def get_pos(self):
        return self.pos

def tab64_to_tab120(tab64_number):
    """Function to mailbox method (cf. Robert Hyatt)
    to translate tab64_number into tab 120 equivalent"""
    return TAB120[tab64_number]


#list for instance classes case creation on the chessboard
#(White position) from the left to the right: nearest to distant

chessboard = [[0,1,2,3,4,5,6,7] # case a
            ,[8,9,10,11,12,13,14,15] # case b
            ,[16,17,18,19,20,21,22,23] # case c
            ,[24,25,26,27,28,29,30,31] # case d
            ,[32,33,34,35,36,37,38,39] # case e
            ,[40,41,42,43,44,45,46,47] # case f
            ,[48,49,50,51,52,53,54,55] # case g
            ,[56,57,58,59,60,61,62,63]] # case h


# loop for creation and stocking all instances of cases in chessboard with attributes
index = 0
tab64 = 91
for number in range(1,9):

    chessboard[0][index] = Case(pygame.Surface((93.75, 93.75), pygame.SRCALPHA, 32),COORD_CASE[0][index],None,tab64,None,0)

    chessboard[1][index] = Case(pygame.Surface((93.75, 93.75), pygame.SRCALPHA, 32),COORD_CASE[1][index],None,tab64 + 1,None,0)

    chessboard[2][index] = Case(pygame.Surface((93.75, 93.75), pygame.SRCALPHA, 32),COORD_CASE[2][index],None,tab64 + 2,None,0)

    chessboard[3][index] = Case(pygame.Surface((93.75, 93.75), pygame.SRCALPHA, 32),COORD_CASE[3][index],None,tab64 + 3,None,0)

    chessboard[4][index] = Case(pygame.Surface((93.75, 93.75), pygame.SRCALPHA, 32),COORD_CASE[4][index],None,tab64 + 4,None,0)

    chessboard[5][index] = Case(pygame.Surface((93.75, 93.75), pygame.SRCALPHA, 32),COORD_CASE[5][index],None,tab64 + 5,None,0)

    chessboard[6][index] = Case(pygame.Surface((93.75, 93.75), pygame.SRCALPHA, 32),COORD_CASE[6][index],None,tab64 + 6,None,0)

    chessboard[7][index] = Case(pygame.Surface((93.75, 93.75), pygame.SRCALPHA, 32),COORD_CASE[7][index],None,tab64 + 7,None,0)

    tab64 -= 10
    index += 1






