# make the graph with the initial config, run before using other stuff
def initialize(init):
	global graph
	global startpos
	startpos = init
	graph = {startpos:{}}

# helper function
def mostpopular(config, color):
	global graph
	moves = graph[config]

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

'''
recommends the first move
returns moves in a list of (move, resulting configuration) tuples
'''
def firstrecommend():
	global graph
	global startpos
	return mostpopular(startpos, 'b')

'''
recommends a move
returns moves in a list of (move, resulting configuration) tuples
'''
def recommend(before, move, color, after):
	global graph
	# finds initial config
	if before in graph:
		moves = graph[before]

		# move exists
		if (move, color) in moves:

			edge = moves[(move, color)]

			# verify resulting config
			if edge[0] == after:

				# adds to popularity
				graph[before][(move, color)] = (edge[0], edge[1]+1)

				# finds destination node
				if after in graph:

					#finds most popular move
					return mostpopular(after, color)

				# destination node missing
				else: print 'Error: could not find expected destination node'

			# resulting config incorrect
			else: print 'Error: resulting config different in graph'

		# move doesn't exist
		else: 

			# resulting configuration exists
			if after in graph:

				# new edge
				graph[before][(move,color)] = (after, 1)

				# finds most popular move
				return mostpopular(after, color)


			# resulting configuration doesn't exist
			else: 

				# new node
				graph[after] = {}

				# new edge
				moves[(move, color)] = (after, 1)

				return []

	# didn't find initial config
	else: print 'Error: could not find initial configuration'

# clears graph
def reset(init):
	global graph
	graph = {init:{}}

# load filename
def load(f):
	f = open(f,'r')
	global graph
	graph = f.read()
	graph = eval(graph)
	f.close()

# save filename
def save(f):
	f = open(f,'w') 
	f.write(str(graph))
	f.close()


''' Testing '''

# primitive testing with a premade graph, only read and +1 functionality
'''
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

print 'first recommended move', firstrecommend(graph1)
print 'popularity before the first move', graph1['A'][('mv1','w')][1]
print 'recommend after first move, should be E', recommend(graph1,'A','mv1','w','B')
print 'popularity after the first move', graph1['A'][('mv1','w')][1]
print 'first recommended move after change, should output two things', firstrecommend(graph1)
print 'recommend after first move again', recommend(graph1,'A','mv1','w','B')
print 'popularity after making the first move again', graph1['A'][('mv1','w')][1]
print 'first recommended move after 2 first moves, should output B', firstrecommend(graph1)
print 'here is the second move', recommend(graph1,'B','mv4','b','E')

graphx = graph1
'''

# building graph from scratch, super thorough testing
initialize('A')

# empty graph
assert firstrecommend() == []

# make first move, tests new node, new edge, first recommend
assert recommend('A', 'mv1', 'w', 'B') == []
assert 'B' in graph
assert graph['B'] == {}
assert graph['A'][('mv1','w')] == ('B',1)
assert firstrecommend() == [('mv1', 'B')]

# make second move
assert recommend('B', 'mv2', 'b', 'C') == []
assert recommend('A', 'mv1', 'w', 'B') == [('mv2','C')]

# make third move
assert recommend('B', 'mv3', 'b', 'D') == []
# note: this ordering is mandatory
assert recommend('A', 'mv1', 'w', 'B') == [('mv2', 'C'), ('mv3', 'D')]
assert recommend('B', 'mv3', 'b', 'D') == []
assert recommend('A', 'mv1', 'w', 'B') == [('mv3', 'D')]

# make fourth move, tests new edge with existing node
assert recommend('A', 'mv4', 'w', 'D') == []
assert firstrecommend() == [('mv1', 'B')]
assert recommend('A', 'mv4', 'w', 'D') == []
assert recommend('A', 'mv4', 'w', 'D') == []
assert recommend('A', 'mv4', 'w', 'D') == []
# note: this ordering is mandatory
assert firstrecommend() == [('mv1', 'B'), ('mv4', 'D')]
assert recommend('A', 'mv4', 'w', 'D') == []
assert firstrecommend() == [('mv4', 'D')]

# save graph
save('test')

# clear graph
reset(startpos) 
assert firstrecommend() == []

# load graph
load('test')
assert firstrecommend() == [('mv4', 'D')]