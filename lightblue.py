import parser
import chess as ch
import graph
import weighting

# intro 
print "Welcome to Light Blue!"
print "Type quit at any time to quit the application."
whiteelo = raw_input("What is the White player's elo rating? (type 0 if unsure) ")
blackelo = raw_input("What is the Black player's elo rating? (type 0 if unsure) ")
print "Available weighting algorithms include:"
print "\"lightblue\""
print "\"pop\""
print "\"elo\""
print "\"wl\""
print "\"static\""
weight_type = raw_input("What kind of weighting would you like to use? ")

# check and checkmate verification
checkmate_message = "Congrats and thanks for using Light Blue."
check_message = "You're in check!"
stalemate_message = "The game is at a draw!"
def stalemate():
	side = current_game.board.get_turn()
	return ch.Board.is_stalemate(current_game.board, side)
def checkmate(): 
	side = current_game.board.get_turn()
	return ch.Board.is_mate(current_game.board, side)
def check():
	side = current_game.board.get_turn()
	return ch.Board.is_check(current_game.board, side)
def checkmate_fun(color, weight_type, mvlst):
	# corrects color again
	if color == 'w':
		print "Checkmate! White Wins!"
	else:
		print "Checkmate! Black Wins!"
	print checkmate_message

	# backtracking
	if weight_type == "wl":

		# generates new weight_objs
		winner_obj = weighting.winloss('w')
		loser_obj = weighting.winloss('l')

		for (a,b,c,d,e) in mvlst:
			if d == color:
				graph.recommend(winner_obj,b,c,d,e)
			else:
				graph.recommend(loser_obj,b,c,d,e)

# selects weighting object
if weight_type == "pop":
    weight_obj = weighting.popularity()
elif weight_type == "elo":
    weight_objw = weighting.elo(whiteelo)
    weight_objb = weighting.elo(blackelo)
elif weight_type == "wl":
    weight_obj = weighting.static()
elif weight_type == "lightblue":
    weight_obj = weighting.lightblue(elo, wlt)
elif weight_type == "static":
    weight_obj = weighting.static()
else: 
    raise "invalid weight type"
mvlst = []

# loads graph
graph.initialize()
graph.load("Carlsen20" + weight_type)

# initializes board
current_game = ch.Game()
current_game.setup()
color = 'w'
quit = False

# prints starting position
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

# recommending moves
while quit == False:

	if color == 'w':
		print "White's Turn"
	else: 
		print "Black's Turn"

	# checks for quitting
	mv = raw_input("What is your move? ")
	if mv == "quit":
		break

	# makes move and grabs configs
	before = str(current_game.board)
	current_game.board.move(mv)
	after = str(current_game.board)

	# prints current board
	print "\n\n\n\n\n\n\n"
	print "---------------------"
	print "Here is the board:"
	print after

	# win loss backtrack storage
	if weight_type == "wl":
		mvlst.append((weight_obj,before,mv,color,after))

	# generate recommendation
	if weight_type == "elo":
		if color == 'w':
			lst2 = graph.recommend(weight_objw,before,mv,color,after)
		else: 
			lst2 = graph.recommend(weight_objb,before,mv,color,after)
	else:
		lst2 = graph.recommend(weight_obj,before,mv,color,after)
	lst2len = len(lst2)
	if lst2len == 1:
		if stalemate():
			print stalemate_message
			print stalemate_message
			break 
		if checkmate():
			checkmate_fun(color, weight_type, mvlst)
			break
		elif check():
			print check_message
		(x,y) = lst2[0]
		print "You should make this move:", x
		print "It should give you:"
		print y
	elif lst2len == 0:
		if stalemate():
			print stalemate_message
			print stalemate_message
			break 
		if checkmate():
			checkmate_fun(color, weight_type, mvlst)
			break
		elif check():
			print check_message
		print "No Data: Make a random move"
	else:
		if stalemate():
			print stalemate_message
			print stalemate_message
			break 
		if checkmate():
			checkmate_fun(color, weight_type, mvlst)
			break
		elif check():
			print check_message
		print "You should make one of these moves:"
		for item in lst2:
			(x,y) = item
			print "One possible move is:", x
			print "It should give you:"
			print y

	# color correction
	if color == 'w':
		color = 'b'
	else: 
		color = 'w'

graph.save("Carlsen20" + weight_type)
