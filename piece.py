import pygame


class Pawn:
    def __init__(self, color, sprite):
        self.__color = color
        self.__sprite = sprite

    def get_color(self):
        return self.__color
    def get_sprite(self):
        return self.__sprite
class King:
    def __init__(self, color, sprite):
        self.__color = color
        self.__sprite = sprite

    def get_color(self):
        return self.__color
    def get_sprite(self):
        return self.__sprite
class Queen:
    def __init__(self, color, sprite):
        self.__color = color
        self.__sprite = sprite

    def get_color(self):
        return self.__color
    def get_sprite(self):
        return self.__sprite
class Bishop:
    def __init__(self, color, sprite):
        self.__color = color
        self.__sprite = sprite

    def get_color(self):
        return self.__color
    def get_sprite(self):
        return self.__sprite
class Knight:
    def __init__(self, color, sprite):
        self.__color = color
        self.__sprite = sprite

    def get_color(self):
        return self.__color
    def get_sprite(self):
        return self.__sprite
class Rook:
    def __init__(self, color, sprite):
        self.__color = color
        self.__sprite = sprite

    def get_color(self):
        return self.__color
    def get_sprite(self):
        return self.__sprite
# Définition de classe pour chaque pièces + methode de classe "get_sprite" pour blitt sprite sur case



def transform_pieces(): #definition fonction pour rescaler les pieces en 90 x 90
    for W_piece in W_pieces:
        W_piece = pygame.transform.scale(W_piece, (90, 90))
        W_pieces_scaled.append(W_piece)
    for B_piece in B_pieces:
        B_piece = pygame.transform.scale(B_piece, (90, 90))
        B_pieces_scaled.append(B_piece)


W_pawn = pygame.image.load("sprite/WhitePawn.png")
W_king = pygame.image.load("sprite/WhiteKing.png")
W_queen = pygame.image.load("sprite/WhiteQueen.png")
W_bishop = pygame.image.load("sprite/WhiteBishop.png")
W_knight = pygame.image.load("sprite/WhiteKnight.png")
W_rook = pygame.image.load("sprite/WhiteRook.png") # Chargement piece blanches

B_pawn = pygame.image.load("sprite/BlackPawn.png")
B_king = pygame.image.load("sprite/BlackKing.png")
B_queen = pygame.image.load("sprite/BlackQueen.png")
B_bishop = pygame.image.load("sprite/BlackBishop.png")
B_knight = pygame.image.load("sprite/BlackKnight.png")
B_rook = pygame.image.load("sprite/BlackRook.png") # Chargement piece noires

W_pieces = [W_pawn,W_king,W_queen,W_bishop,W_knight,W_rook]
B_pieces = [B_pawn,B_king,B_queen,B_bishop,B_knight,B_rook]#liste pour utiliser la boucle de la fonction "transform_pieces"

W_pieces_scaled = []
B_pieces_scaled = []#nouvelle liste pour stocker fonction transform_pieces

transform_pieces() #application de la fonction

W_pawn_sprite = W_pieces_scaled[0]
W_king_sprite = W_pieces_scaled[1]
W_queen_sprite = W_pieces_scaled[2]
W_bishop_sprite = W_pieces_scaled[3]
W_knight_sprite = W_pieces_scaled[4]
W_rook_sprite = W_pieces_scaled[5]

B_pawn_sprite = B_pieces_scaled[0]
B_king_sprite = B_pieces_scaled[1]
B_queen_sprite = B_pieces_scaled[2]
B_bishop_sprite = B_pieces_scaled[3]
B_knight_sprite = B_pieces_scaled[4]
B_rook_sprite = B_pieces_scaled[5] # remise des variables pour une facilité d'utilisation dans chaque instance de classe

W_pawn = Pawn("white",W_pawn_sprite) #création d 'instance de classe pour chaque pièce blanche (avec nom et sprite transformé par fonction "transform_pieces")
W_king = King("white",W_king_sprite)
W_queen = Queen("white",W_queen_sprite)
W_bishop = Bishop("white",W_bishop_sprite)
W_knight = Knight("white",W_knight_sprite)
W_rook = Rook("white",W_rook_sprite)

B_pawn = Pawn("black",B_pawn_sprite) #création d 'instance de classe pour chaque pièce noire (avec nom et sprite transformé par fonction "transform_pieces")
B_king = King("black",B_king_sprite)
B_queen = Queen("black",B_queen_sprite)
B_bishop = Bishop("black",B_bishop_sprite)
B_knight = Knight("black",B_knight_sprite)
B_rook = Rook("black",B_rook_sprite)













