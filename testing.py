import graph

graph.initialize()
graph.load("Kasparov20")

lst = graph.firstrecommend()
(x,y) = lst[0]

print "You should make this move:", x
print "It should give you:"
print y
