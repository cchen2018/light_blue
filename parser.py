import chess as ch
import copy
import glob
import graph

'''
At the moment, this code prints out one game in this format:
Old Board Configuration
Move that was made
Player Color who just moved
New Board Configuration
'''

        
# main funtion for returning tuple format to graph
def main():
        all_elements = []
        count = 0
        for f in glob.iglob('*.pgn'):
                count += 1
                game = ch.Game()
                new_game = ch.Game()
                print f
                pgn_file = open(f, 'r')
                pgn = game.import_pgn(pgn_file)

                #elements = []
                piece_color = ""
                new_game.setup()

                for move in game.moves:

                        old_board = new_game.board
                        #deepcopy old board to maintain config.
                        old_board_copy = copy.deepcopy(old_board)
                        
                        new_game.move(move)
                        
                        new_board = new_game.board
                        new_board_copy = copy.deepcopy(new_board)

                        # Getting piece colors - works
                        if new_game.board.get_turn() == 0:
                                piece_color = "b"
                                #print piece_color
                        else:
                                piece_color = "w"
                                #print piece_color
                                #print move

                        all_elements.append((str(old_board_copy), str(move), piece_color, str(new_board_copy)))
                        #all_elements.append(elements)
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
                '''
                print elements
                for element in elements:
                        print element[0]
                        print element[1]
                        print element[2]
                        print element[3]
                        print "-----------------------------------"'''
                #print elements[0][3]
                print count
                #print all_elements
                pgn_file.close()
        #print all_elements
        graph.initialize()

        for (a, b, c, d) in all_elements:
            graph.recommend(a, b, c, d)

        graph.save("Carlsen20")

        print graph.graph[str(starting_game.board)]
        print graph.firstrecommend()


if __name__ == '__main__':
	main()
