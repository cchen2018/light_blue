print "Instructions:"" 
print "Type in the move each player makes in Standard Algebraic Notation (SAN)"
print "  (a) For pawns, type the piece's origin coordinate, a dash, then the final coordinate"
print "       example: tying 'e2-e4' (without quotes) moves a pawn from e2 to e4"
print "  (b) For pieces other than pawns, first type the first letter of the piece's name in upper-case"
print "      followed by the pawn notation."
print "      example: typing 'Qd1-f3' (without quotes) moves the queen from d1 to f3"
print "      NOTE: the letter for knight is 'N' not 'K' because 'K' is already used to denote the Kings"
print "  (c) For moves where pieces are captured, the dash should be changed to lower-case 'x'"
print "      example: typing 'Qf3xf7' (without quotes) moves the queen from f3 and captures a piece at f7"
print "  (d) Denote castling with upper-case letter O's separated by dashes"
print "      (i) 'O-O' queenside"
print "      (ii) 'O-O-O' kingside"
print "  (e) Moves are denoted the same way, regardless of the side making the move."
print "      The program automatically tracks which side should be moving, allowing it to correctly"
print "      interpret which piece to move."
print "  (f) Illegal moves will be cause the program to terminate with exceptions due to"
print "      code from the chess API that light_blue uses."
print "  (g) Please see http://en.wikipedia.org/wiki/Rules_of_chess for the complete set of chess rules."