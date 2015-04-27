import chess as ch
import copy
import glob
import graph
import weighting
import sys
import reg_exp

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
    weight_type = sys.argv[1]

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

        reg_result = reg_exp.reg_exp(f)


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
                #reg_result = reg_exp.reg_exp(f, piece_color)
                elo = reg_result[1]
                if reg_result[2] == "black":
                    wlt = 'w'
                elif reg_result[2] == "white":
                    wlt = 'l'
                else:
                    wlt = 't'
                    
            else:
                piece_color = "w"
                #print piece_color
                #print move
                #reg_result = reg_exp.reg_exp(f, piece_color)
                elo = reg_result[0]
                if reg_result[2] == "black":
                    wlt = 'l'
                elif reg_result[2] == "white":
                    wlt = 'w'
                else:
                    wlt = 't'
            

            if weight_type == "pop":
                weight_obj = weighting.popularity()
            elif weight_type == "elo":
                weight_obj = weighting.elo(elo)
            elif weight_type == "wl":
                weight_obj = weighting.winloss(wlt)
            elif weight_type == "lightblue":
                weight_obj = weighting.lightblue(elo, wlt)
            elif weight_type == "static":
                weight_obj = weighting.static()
            else: 
                raise "Usage: python parser.py weight_type"

            all_elements.append(
                (weight_obj, str(old_board_copy), str(move), piece_color, str(new_board_copy))
            )
            #all_elements.append(elements)

        #print elements[0][3]
        print count

        #print all_elements
        pgn_file.close()

    graph.initialize()

    for (a, b, c, d, e) in all_elements:
        graph.recommend(a,b,c,d,e)

    graph.save("Carlsen20" + weight_type)
    
    for x in graph.graph:
        for y in graph.graph[x]:
            print graph.graph[x][y][1]

    #print graph.graph[str(starting_game.board)]
    #print graph.firstrecommend()


if __name__ == '__main__':
	main()
