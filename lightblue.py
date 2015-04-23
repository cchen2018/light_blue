import parser
import chess as ch
import graph

print "Welcome to Light Blue!"
print "Type quit at any time to quit the application."

graph.initialize()
graph.load("Carlsen20")

current_game = ch.Game()
current_game.setup()
color = 'w'
quit = False

print "Here is the board:"
print current_game.board

# first recommend
lst = graph.firstrecommend()
lstlen = len(lst)
if lstlen == 1:
	(x,y) = lst[0]
	print "You should make this move:", x
	print "It should give you:"
	print y
elif lstlen == 0:
	print "Error: No Data"
	quit = True
else:
	print "You should make one of these moves:"
	for item in lst:
		(x,y) = item
		print "One possible move is:", x
		print "It should give you:"
		print y

while quit == False:
	mv = raw_input("What is your move? ")
	if mv == "quit":
		break
	before = str(current_game.board)
	current_game.board.move(mv)
	after = str(current_game.board)
	if color == 'w':
		color = 'b'
	else: color = 'w'
	lst2 = graph.recommend(before,mv,color,after)
	lst2len = len(lst2)
	if lst2len == 1:
		print "Here is the board:"
		print after
		(x,y) = lst2[0]
		print "You should make this move:", x
		print "It should give you:"
		print y
	elif lst2len == 0:
		print "No Data: Make a random move"
		print "Here is the board:"
		print after
	else:
		print "Here is the board:"
		print after
		print "You should make one of these moves:"
		for item in lst2:
			(x,y) = item
			print "One possible move is:", x
			print "It should give you:"
			print y
