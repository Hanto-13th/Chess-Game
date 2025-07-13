import pygame

#-------------------------------------
# Creation of the Parent Class : Piece
#-------------------------------------
# With attributes and method
class Piece:
    def __init__(self, color, sprite, name):
        self.color = color
        self.__sprite = sprite
        self.name = name


    def get_sprite(self):
        return self.__sprite

#--------------------------------------------------------------------------
# Creation of Subclasses of class "Pieces" for each piece on the chessboard
#--------------------------------------------------------------------------

class Pawn(Piece):
    def __init__(self, color, sprite,name):
        super().__init__(color,sprite,name)

class King(Piece):
    def __init__(self, color, sprite,name):
        super().__init__(color,sprite,name)

class Queen(Piece):
    def __init__(self, color, sprite,name):
        super().__init__(color,sprite,name)

class Bishop(Piece):
    def __init__(self, color, sprite,name):
        super().__init__(color,sprite,name)

class Knight(Piece):
    def __init__(self, color, sprite,name):
        super().__init__(color,sprite,name)

class Rook(Piece):
    def __init__(self, color, sprite,name):
        super().__init__(color,sprite,name)

#loading all the sprites for each pieces

W_pawn_sprite = pygame.image.load("sprite/WhitePawn.png")
W_king_sprite = pygame.image.load("sprite/WhiteKing.png")
W_queen_sprite = pygame.image.load("sprite/WhiteQueen.png")
W_bishop_sprite = pygame.image.load("sprite/WhiteBishop.png")
W_knight_sprite = pygame.image.load("sprite/WhiteKnight.png")
W_rook_sprite = pygame.image.load("sprite/WhiteRook.png")

B_pawn_sprite = pygame.image.load("sprite/BlackPawn.png")
B_king_sprite = pygame.image.load("sprite/BlackKing.png")
B_queen_sprite = pygame.image.load("sprite/BlackQueen.png")
B_bishop_sprite = pygame.image.load("sprite/BlackBishop.png")
B_knight_sprite = pygame.image.load("sprite/BlackKnight.png")
B_rook_sprite = pygame.image.load("sprite/BlackRook.png")

#creation of all class instances for each pieces

W_pawn = Pawn("white",W_pawn_sprite,"pawn")
W_king = King("white",W_king_sprite,"king")
W_queen = Queen("white",W_queen_sprite,"queen")
W_bishop = Bishop("white",W_bishop_sprite,"bishop")
W_knight = Knight("white",W_knight_sprite,"knight")
W_rook = Rook("white",W_rook_sprite,"rook")

B_pawn = Pawn("black",B_pawn_sprite,"pawn")
B_king = King("black",B_king_sprite,"king")
B_queen = Queen("black",B_queen_sprite,"queen")
B_bishop = Bishop("black",B_bishop_sprite,"bishop")
B_knight = Knight("black",B_knight_sprite,"knight")
B_rook = Rook("black",B_rook_sprite,"rook")















