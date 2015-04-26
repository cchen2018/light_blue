# getting ready to implement elo and win/loss

class popularity(object):

	# iterates popularity by one
	def alter(self, current):
		pop = current[0]
		return (pop + 1,)
	default = (1,)

class elo(object):
	def __init__(self, new):
		self.new = new 

    # overrides with higher elo
	def alter(self, current):
		rating = current[0]
		if self.new > rating:
			return (self.new,)
		else: return current
	default = (1,)

class winloss(object):
	def __init__(self, new):
		self.new = new 

    # alters win/loss ratio
	def alter(self, current):
		(weight, win, loss) = current
		# tie
		if self.new == "t":
			return current
		# win
		elif self.new == "w":
			win += 1
			return ((win/loss),win,loss)
		# loss
		else:
			loss += 1
			return ((win/loss),win,loss)
	default = (1,1,1)


