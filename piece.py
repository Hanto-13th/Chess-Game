import pygame


def transform_pieces(): #definition fonction pour rescaler les pieces en 90 x 90
    for piece in pieces:
        piece = pygame.transform.scale(piece, (90, 90))
        pieces_scaled.append(piece)

W_pawn = pygame.image.load("C:/Users/anton/Documents/Python/Chess/sprite/WhitePawn.png")
W_king = pygame.image.load("C:/Users/anton/Documents/Python/Chess/sprite/WhiteKing.png")
W_queen = pygame.image.load("C:/Users/anton/Documents/Python/Chess/sprite/WhiteQueen.png")
W_bishop = pygame.image.load("C:/Users/anton/Documents/Python/Chess/sprite/WhiteBishop.png")
W_knight = pygame.image.load("C:/Users/anton/Documents/Python/Chess/sprite/WhiteKnight.png")
W_rook = pygame.image.load("C:/Users/anton/Documents/Python/Chess/sprite/WhiteRook.png") # Chargement piece blanches

B_pawn = pygame.image.load("C:/Users/anton/Documents/Python/Chess/sprite/BlackPawn.png")
B_king = pygame.image.load("C:/Users/anton/Documents/Python/Chess/sprite/BlackKing.png")
B_queen = pygame.image.load("C:/Users/anton/Documents/Python/Chess/sprite/BlackQueen.png")
B_bishop = pygame.image.load("C:/Users/anton/Documents/Python/Chess/sprite/BlackBishop.png")
B_knight = pygame.image.load("C:/Users/anton/Documents/Python/Chess/sprite/BlackKnight.png")
B_rook = pygame.image.load("C:/Users/anton/Documents/Python/Chess/sprite/BlackRook.png") # Chargement piece noires

W_tiles = pygame.image.load("C:/Users/anton/Documents/Python/Chess/sprite/W_Tiles.png")
B_tiles = pygame.image.load("C:/Users/anton/Documents/Python/Chess/sprite/B_Tiles.png")


pieces = [W_pawn,W_king,W_queen,W_bishop,W_knight,W_rook,B_pawn,B_king,B_queen,B_bishop,B_knight,B_rook] #liste pour utiliser la fonction transform_pieces
pieces_scaled = [] #nouvelle liste pour fonction transform_pieces
transform_pieces() #application de la fonction

W_pawn = pieces_scaled[0]
W_king = pieces_scaled[1]
W_queen = pieces_scaled[2]
W_bishop = pieces_scaled[3]
W_knight = pieces_scaled[4]
W_rook = pieces_scaled[5]

B_pawn = pieces_scaled[6]
B_king = pieces_scaled[7]
B_queen = pieces_scaled[8]
B_bishop = pieces_scaled[9]
B_knight = pieces_scaled[10]
B_rook = pieces_scaled[11] # remise des variables pour une facilité d'utilisation





