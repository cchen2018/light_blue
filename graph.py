graph1 = {
	'A':{('mv1','w'):('B',1),
		 ('mv2','w'):('C',2)},
	'B':{('mv4','b'):('E',3),
		 ('mv5','b'):('F',2)},
	'C':{('mv6','b'):('G',1),
		 ('mv7','b'):('H',1)},
	'D':{},
	'E':{},
	'F':{},
	'G':{},
	'H':{}}


# used to sort tuples
from operator import itemgetter

# helper function, takes 
def mostpopular(config,color):

	moves = graph1[config]

	if moves == {}:
		return []
	else:
		moves2 = {}

		# filters for correct color
		if color == 'b':
			color = 'w'
		else: color = 'b'
		for key in moves:
			if key[1] == color:
				moves2[key] = moves[key]

		# get list of popularities
		lst = []
		for key in moves:
			lst.append(moves[key][1])

		# finds most popular
		top = max(lst)

		# finds all moves with top popularity
		temp = []
		for key in moves:
			if moves[key][1] == top:
				temp.append((key,moves[key][0]))

		# formats list
		nextmoves = []
		for item in temp:
			nextmoves.append((item[0][0],item[1]))

		# returns recommended moves in the form (move, configuration)
		return nextmoves


# recommends first move
def firstrecommend():
	mostpopular('A','b')

print firstrecommend()


# recommends a move
def recommend(before, move, color, after):

	# finds initial config
	if before in graph1:
		moves = graph1[before]

		# move exists
		if (move, color) in moves:

			edge = moves[(move, color)]

			# verify resulting config
			if edge[0] == after:

				edge

				# adds to popularity
				print 'count before', graph1[before][(move, color)][1]
				graph1[before][(move, color)] = (edge[0], edge[1]+1)
				print 'count after', graph1[before][(move, color)][1]

				# finds destination node
				if after in graph1:

					#finds most popular move
					return mostpopular(after,color)

				# destination node missing
				else: print 'Error: could not find expected destination node'

			# resulting config incorrect
			else: print 'Error: resulting config different in graph'

		# move doesn't exist
		else: 

			# resulting configuration exists
			if after in graph1:

				# new edge
				graph1[before][(move,color)] = (after, 1)

				# finds most popular move
				return mostpopular(after,color)


			# resulting configuration doesn't exist
			else: 

				# new node
				graph1[after] = {}

				# new edge
				moves[(move, color)] = (after, 1)

				return []

	# didn't find initial config
	else: print 'Error: could not find initial configuration'

print recommend('A','mv1','w','B')
print recommend('B','mv4','b','E')