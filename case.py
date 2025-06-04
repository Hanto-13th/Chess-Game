import pygame

coord_case = [[(0,656.25),(0,562.5),(0,468.75),(0,375),(0,281.25),(0,187.5),(0,93.75),(0,0)] # case a
           ,[(93.75,656.25),(93.75,562.5),(93.75,468.75),(93.75,375),(93.75,281.25),(93.75,187.5),(93.75,93.75),(93.75,0)] # case b
           ,[(187.5,656.25),(187.5,562.5),(187.5,468.75),(187.5,375),(187.5,281.25),(187.5,187.5),(187.5,93.75),(187.5,0)] # case c
           ,[(281.25,656.25),(281.25,562.5),(281.25,468.75),(281.25,375),(281.25,281.25),(281.25,187.5),(281.25,93.75),(281.25,0)] # case d
           ,[(375,656.25),(375,562.5),(375,468.75),(375,375),(375,281.25),(375,187.5),(375,93.75),(375,0)] # case e
           ,[(468.75,656.25),(468.75,562.5),(468.75,468.75),(468.75,375),(468.75,281.25),(468.75,187.5),(468.75,93.75),(468.75,0)] # case f
           ,[(562.5,656.25),(562.5,562.5),(562.5,468.75),(562.5,375),(562.5,281.25),(562.5,187.5),(562.5,93.75),(562.5,0)] # case g
           ,[(656.25,656.25),(656.25,562.5),(656.25,468.75),(656.25,375),(656.25,281.25),(656.25,187.5),(656.25,93.75),(656.25,0)]] # case h
#Coordonnées de chaque case (W_pos)
#de gauche a droite: de la plus proche à la plus éloignée

chessboard = [[1,2,3,4,5,6,7,8] # case a
            ,[1,2,3,4,5,6,7,8] # case b
            ,[1,2,3,4,5,6,7,8] # case c
            ,[1,2,3,4,5,6,7,8] # case d
            ,[1,2,3,4,5,6,7,8] # case e
            ,[1,2,3,4,5,6,7,8] # case f
            ,[1,2,3,4,5,6,7,8] # case g
            ,[1,2,3,4,5,6,7,8]] # case h
#liste pour création des surfaces de chaque cases (W_pos)
#de gauche a droite: de la plus proche à la plus éloignée

index = 0

for number in range(1,9):
    chessboard[0][index] = pygame.Surface((93.75,93.75),pygame.SRCALPHA, 32)


    chessboard[1][index] = pygame.Surface((93.75, 93.75), pygame.SRCALPHA, 32)


    chessboard[2][index] = pygame.Surface((93.75, 93.75), pygame.SRCALPHA, 32)


    chessboard[3][index] = pygame.Surface((93.75, 93.75), pygame.SRCALPHA, 32)


    chessboard[4][index] = pygame.Surface((93.75, 93.75), pygame.SRCALPHA, 32)


    chessboard[5][index] = pygame.Surface((93.75, 93.75), pygame.SRCALPHA, 32)


    chessboard[6][index] = pygame.Surface((93.75, 93.75), pygame.SRCALPHA, 32)


    chessboard[7][index] = pygame.Surface((93.75, 93.75), pygame.SRCALPHA, 32)


    index += 1

#boucle pour création des surfaces de chaque cases




