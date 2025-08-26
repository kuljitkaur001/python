# king move 
# chess 8 * 8
# king can move only one step around itself

# pass king oin the function 
# set cell names. like where it can move


# King: moves one square in any direction

# Queen: any number of squares in any direction

# Rook: horizontal or vertical

# Bishop: diagonal only

# Knight: L-shape (2+1 or 1+2)

# Pawn: one step forward, two on first move, diagonal to capture


# king 
# computer asks directions 

# steps 
# 
import sys
class chessboardvalidator :
# Pawn: one step forward, two on first move, diagonal to capture
    def __init__(self, piece):
        self.piece = piece.lower()

    def choice(self):
        valid_pieces = ["king", "queen","rook" ,"knight", "Knight" ,"bishop", "Bishop" ,"pawn"]
        if (self.piece not in valid_pieces):
            print("\n \n invalid piece, reload the code and enter from given  ".title())
            sys.exit()

    def king_direction_(self, direction):
        self.direction = direction.strip().lower()
        valid_directions =["left", "right", "up", "down"] 
        if direction not in valid_directions:
            print("please choose from given direction")
            # print("valid direction ")
            sys.exit()
        else:
            print("valid ")
            
    def king (self,steps ):
        if (steps == 1 or steps == 2):
            print(f"\n {steps} is a valid move  ".title())
        else :
            print(f"{steps} is not a valid move")

    def queen_direction_(self, direction1):
        self.direction1 = direction1.strip().lower()
        valid_directions1 =["left", "right", "up", "down", "left-diagnoal, right-diagonal"] 
        if direction1 not in valid_directions1:
            print("please choose from given direction")
            # print("valid direction ")
            sys.exit()
        else:
            print("valid ")

    def queen_(self,steps):
        if (steps <= 8):
            print(f"\n {steps} is a valid move  ".title())
        else :
            print(f"\n error!....queen can not move {steps} steps ".title())
      
    def knight_(self, steps ):
        if (steps == 3):
            print(f".{steps } is a valid move ".title())
        
        else: 
            print(f"\n error!......knight can not move {steps} steps ".title())

    def bishop_(self, steps):
        if (steps <= 8):
            print(f".{steps } is a valid move ".title())
        else:
            print(f"\n error!......bishop  can not move {steps} steps ".title())

    def pawn_(self, pawn):

        if (steps == 2):
            print(f"{steps } is a valid move ".title())
        elif(steps == 1):
            print(f"{steps } is a valid move ".title())

        else:
            print(f"\n error!......pawn can not move {steps} steps ".title())
        
    def rook_(self, rook):
        if(steps <= 8):
            print(f"{steps } is a valid move ".title())
        
        else:
            print(f"\n error!......rook can not move {steps} steps ".title())
   
user = input("enter piece name from following  : \n 1.king \n 2.queen  \n 3.knight \n 4.bishop \n 5.pawn \n 6.rook \n enter : ".title())
object1 = chessboardvalidator(user)
object1.choice()

# directions 
directions = input(f"\n directions for {user}  are \n 1.left \n 2.right \n 3.up\n 4.down \n which direction do you want to choose for  {user} : ".title())
object1.king_direction_(directions)

steps = int(input(f"\n how much steps {user} should take : ".title()))

if user == "king":
    object1.king(steps )

elif user == "queen":
    directions = input(f"\n directions for {user}  are \n 1.left \n 2.right \n 3.up \n 4.down \n 5.left-diagonal \n 6. right - diagonaly   which direction do you want to choose for  {user} : ".title())

    object1.queen_(steps)

elif(user == "knight"):
    object1.knight_(steps)

elif (user == "bishop"):
    object1.bishop_(steps)

elif(user == "pawn"):
    object1.pawn_(steps)

elif(user == "rook"):
    object1.rook_(steps)

        