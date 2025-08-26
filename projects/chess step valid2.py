# King: moves one square in any direction

# Queen: any number of squares in any direction

# Rook: horizontal or vertical

# Bishop: diagonal only

# Knight: L-shape (2+1 or 1+2)

# Pawn: one step forward, two on first move, diagonal to capture


import sys

class ChessboardValidator:
    def __init__(self, piece):
        self.piece = piece.lower()  # store in lowercase for easy comparison

    def choice(self):
        valid_pieces = ["king", "queen", "rook", "bishop", "knight", "pawn"]
        if self.piece not in valid_pieces:
            print("\nInvalid piece, reload the code and enter from the given options.".title())
            sys.exit()

    def king(self, steps):
        if steps == 1:
            print(f"\n{steps} is a valid move for King")
        else:
            print(f"{steps} is not a valid move for King")

    def queen(self, steps):
        if 1 <= steps <= 7:
            print(f"\n{steps} is a valid move for Queen")
        else:
            print(f"{steps} is not a valid move for Queen")

    def rook(self, steps):
        if 1 <= steps <= 7:
            print(f"\n{steps} is a valid move for Rook")
        else:
            print(f"{steps} is not a valid move for Rook")

    def bishop(self, steps):
        if 1 <= steps <= 7:
            print(f"\n{steps} is a valid move for Bishop")
        else:
            print(f"{steps} is not a valid move for Bishop")

    def knight(self, steps):
        if steps == 3:
            print(f"\n{steps} is a valid move for Knight (L-shape)")
        else:
            print(f"{steps} is not a valid move for Knight")

    def pawn(self, steps):
        if steps == 1 or steps == 2:
            print(f"\n{steps} is a valid move for Pawn")
        else:
            print(f"{steps} is not a valid move for Pawn")

# User interaction 

user = input("Enter piece name from following:\n1. King\n2. Queen\n3. Knight\n4. Bishop\n5. Pawn\n6. Rook\nEnter: ").lower()
obj = ChessboardValidator(user)
obj.choice()

steps = int(input(f"\nHow many steps should {user.title()} take: "))

# Call correct function based on piece
if user == "king":
    obj.king(steps)
elif user == "queen":
    obj.queen(steps)
elif user == "rook":
    obj.rook(steps)
elif user == "bishop":
    obj.bishop(steps)
elif user == "knight":
    obj.knight(steps)
elif user == "pawn":
    obj.pawn(steps)
