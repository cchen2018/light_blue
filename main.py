import chess as ch
import copy

'''
At the moment, this code prints out one game in this format:
Old Board Configuration
New Board Configuration
Player Color who just moved
And the Move that was just made
'''




''' Function I created to return player tag info
 Used the import_pgn function in the chess module for reference'''
def get_tags(self, pg):
        tags = {}
        for line in pg:

            line = line.strip()

            match = ch.Game.tag_re.match(line)

            if match is None:
                break

            tag_tokens = ch.Game.tag_re.match(line).groups()

            if len(tag_tokens) >= 2:

                tag_name = tag_tokens[0].strip()
                tag_value = tag_tokens[1].strip('"')

                #print tag_name, tag_value

                tags[tag_name] = tag_value
        return tags



        
# main funtion for returning tuple format to graph
def main():
	game = ch.Game()
	new_game = ch.Game()
	# game.reset()

	pgn_file = open("MagnusCarlsen.pgn", "r")
	pgn = game.import_pgn(pgn_file)

        # Messing around
	''' print game.board.occupied_squares()
	for x in game.board.occupied_squares():
		print x'''

        # attempt to return player info in dict
        '''tag_dict = get_tags(new_game,pgn_file)
        print tag_dict'''

        elements = []
        piece_color = ""
	new_game.setup()

	for move in game.moves:
                #old_board = new_game.board

                # second attempt for returning player tags in dict
                '''t = get_tags(new_game,pgn_file)
                print t'''

                '''Trying to grab old_board value
                without just expressing new_board.
                When printed before move it works, 
                when printed after move it doesn't'''
                old_board = new_game.board
                old_board_copy = copy.deepcopy(old_board)
                #print new_game.board
                print old_board
                new_game.move(move)
                new_board = new_game.board
                #print new_game.board
                #print old_board
                print new_board
                elements.append(old_board_copy)

                # Getting piece colors - works
                if new_game.board.get_turn() == 0:
                        piece_color = "Black"
                        print piece_color
                else:
                        piece_color = "White"
                        print piece_color
                print move

                '''Eventually this will be the output
                format - a list of tuples containing
                these values'''

                ''' 
                elements.append((old_board,\
                                 move,\
                                 Win/Loss,\
                                 Elo,\
                                 Piece Color,\
                                 new_game.board))
                elements.append((,\
                                 move,\
                                 ,\
                                 ,\
                                 piece_color,\
                                 new_game.board))
                '''

        print elements
        '''for element in elements:
                print element'''

        # Another attempt to get player info tags
        '''tg = get_tags(new_game,pgn_file)
        print tg'''


if __name__ == '__main__':
	main()
