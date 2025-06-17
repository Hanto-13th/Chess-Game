import pygame

class Case:
    def __init__(self,surface,color,pos,piece,tab64):
        self.surface = surface
        self.color = color
        self.__pos = pos
        self.piece = piece
        self.tab64 = tab64

    def get_color(self):
        return self.color
    def get_pos(self):
        return self.__pos
# Définition de classe pour les cases avec création de leur surface et leur couleur
#+ methode de classe "get_color" pour stocker les couleurs des pions dans les cases correspondantes

def tab64_to_tab120(tab64):
    return tab120[tab64]



coord_case = [[(0,656.25),(0,562.5),(0,468.75),(0,375),(0,281.25),(0,187.5),(0,93.75),(0,0)] # case a                                           ########
           ,[(93.75,656.25),(93.75,562.5),(93.75,468.75),(93.75,375),(93.75,281.25),(93.75,187.5),(93.75,93.75),(93.75,0)] # case b             ########
           ,[(187.5,656.25),(187.5,562.5),(187.5,468.75),(187.5,375),(187.5,281.25),(187.5,187.5),(187.5,93.75),(187.5,0)] # case c             ########
           ,[(281.25,656.25),(281.25,562.5),(281.25,468.75),(281.25,375),(281.25,281.25),(281.25,187.5),(281.25,93.75),(281.25,0)] # case d     ########
           ,[(375,656.25),(375,562.5),(375,468.75),(375,375),(375,281.25),(375,187.5),(375,93.75),(375,0)] # case e                             ########
           ,[(468.75,656.25),(468.75,562.5),(468.75,468.75),(468.75,375),(468.75,281.25),(468.75,187.5),(468.75,93.75),(468.75,0)] # case f     ########
           ,[(562.5,656.25),(562.5,562.5),(562.5,468.75),(562.5,375),(562.5,281.25),(562.5,187.5),(562.5,93.75),(562.5,0)] # case g             ########
           ,[(656.25,656.25),(656.25,562.5),(656.25,468.75),(656.25,375),(656.25,281.25),(656.25,187.5),(656.25,93.75),(656.25,0)]] # case h    ########
#Coordonnées de chaque case (W_pos)
#de gauche a droite: de la plus proche à la plus éloignée

tab120 = (
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1
,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1
,-1, 0, 1, 2, 3, 4, 5, 6, 7, -1
,-1, 8,9, 10, 11, 12, 13, 14, 15, -1
,-1, 16, 17, 18, 19, 20, 21, 22, 23, -1
,-1, 24, 25, 26, 27, 28, 29, 30, 31, -1
,-1, 32, 33, 34, 35, 36, 37, 38, 39, -1
,-1, 40, 41, 42, 43, 44, 45, 46, 47, -1
,-1, 48, 49, 50, 51, 52, 53, 54, 55, -1
,-1, 56, 57, 58, 59, 60, 61, 62, 63, -1
,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1
,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1
)
#tableau 120 pour méthode "mailbox" de Robert Hyatt

chessboard = [[0,1,2,3,4,5,6,7] # case a
            ,[8,9,10,11,12,13,14,15] # case b
            ,[16,17,18,19,20,21,22,23] # case c
            ,[24,25,26,27,28,29,30,31] # case d
            ,[32,33,34,35,36,37,38,39] # case e
            ,[40,41,42,43,44,45,46,47] # case f
            ,[48,49,50,51,52,53,54,55] # case g
            ,[56,57,58,59,60,61,62,63]] # case h
#liste pour création des instances de classe de chaque cases sur le plateau "chessboard"
# (W_pos) de gauche a droite: de la plus proche à la plus éloignée

index = 0
tab64_a = 91
tab64_b = 92
tab64_c = 93
tab64_d = 94
tab64_e = 95
tab64_f = 96
tab64_g = 97
tab64_h = 98

for number in range(1,9): #boucle pour création des instances de classe de chaque cases sur le plateau "chessboard"
    chessboard[0][index] = Case(pygame.Surface((93.75, 93.75), pygame.SRCALPHA, 32),None,coord_case[0][index],None,tab64_a)

    chessboard[1][index] = Case(pygame.Surface((93.75, 93.75), pygame.SRCALPHA, 32),None,coord_case[1][index],None,tab64_b)

    chessboard[2][index] = Case(pygame.Surface((93.75, 93.75), pygame.SRCALPHA, 32),None,coord_case[2][index],None,tab64_c)

    chessboard[3][index] = Case(pygame.Surface((93.75, 93.75), pygame.SRCALPHA, 32),None,coord_case[3][index],None,tab64_d)

    chessboard[4][index] = Case(pygame.Surface((93.75, 93.75), pygame.SRCALPHA, 32),None,coord_case[4][index],None,tab64_e)

    chessboard[5][index] = Case(pygame.Surface((93.75, 93.75), pygame.SRCALPHA, 32),None,coord_case[5][index],None,tab64_f)

    chessboard[6][index] = Case(pygame.Surface((93.75, 93.75), pygame.SRCALPHA, 32),None,coord_case[6][index],None,tab64_g)

    chessboard[7][index] = Case(pygame.Surface((93.75, 93.75), pygame.SRCALPHA, 32),None,coord_case[7][index],None,tab64_h)

    tab64_a -= 10
    tab64_b -= 10
    tab64_c -= 10
    tab64_d -= 10
    tab64_e -= 10
    tab64_f -= 10
    tab64_g -= 10
    tab64_h -= 10
    index += 1






