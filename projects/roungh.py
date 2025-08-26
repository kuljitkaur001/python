# chess step validator 

#  Step 1: Define Board Structure
# Use coordinates (e.g., "a1" to "h8" or 0-7, 0-7) or directly use chess notation.

#  Step 2: Map Piece Movement Rules
# Create movement validation functions for:

# King: moves one square in any direction

# Queen: any number of squares in any direction

# Rook: horizontal or vertical

# Bishop: diagonal only

# Knight: L-shape (2+1 or 1+2)

# Pawn: one step forward, two on first move, diagonal to capture

#  Takes input: piece name, start position, end position
#  Checks if the move is valid based on simple rules
#  Outputs: “Valid Move” or “Invalid Move”


# class chess_validator():
columns_map = { "a" : 0,
               "b" : 1,
               "c" :2,
               "d": 3, 
               "e" : 4,
               "f" :5,
               "g" :6,
               "h" :7
                }
#function to convert values.. in integer form 
def userinput_to_interger(position):
    col = columns_map(position[0].lower())
    return col



piece_name = input("enter the piece name you want to move from following:-  \n 1. king \n 2. queen \n 3. bishop \n 4. Knight \n 5. rook \n 6. pawn \n ")
piece_start_pos = input("enter the starting position of piece ")
piece_end_pos = input("enter the end position piece name ")

userinput_to_interger(piece_name)