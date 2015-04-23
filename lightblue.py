import parser
import chess as ch

print "Welcome to Light Blue!"

graph.load("database")

quit = false

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
	quit = true
else:
	print "You should make one of these moves:"
	for item in lst:
		(x,y) = lst[item]
		print "One possible move is:", x
		print "It should give you:"
		print y

current_game = ch.Game()
current_game.setup()

color = 'w'

while quit == false:
	mv = raw_input("What is your move?")
	if mv = "quit":
		break
	before = str(current_game.board)
	current_game.board.move(mv)
	after = str(current_game.board)
	if color = 'w':
		color = 'b'
	else: color = 'w'
	lst2 = graph.recommend(before,mv,color,after)
	lst2len = len(lst2)
	if lst2len == 1:
		(x,y) = lst2[0]
		print "You should make this move:", x
		print "It should give you:"
		print y
	elif lst2len == 0:
		print "Error: No Data"
		quit = true
	else:
		print "You should make one of these moves:"
		for item in lst2:
			(x,y) = lst2[item]
			print "One possible move is:", x
			print "It should give you:"
			print y
