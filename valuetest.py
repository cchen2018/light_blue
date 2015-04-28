import graph
import chess as ch
import sys

weight_type = sys.argv[1]
graph.load("Carlsen20" + weight_type)
starting_game = ch.Game()
starting_game.setup()
startpos = str(starting_game.board)

print graph.graph[startpos]