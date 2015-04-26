# getting ready to implement elo and win/loss

from __future__ import division

class popularity(object):

	# iterates popularity by one
	def alter(self, current):
		pop = current[0]
		return (pop + 1,)
	default = (1,)

class elo(object):
	def __init__(self, new):
		if new == 0:
			new = 2000
		self.new = new 
		self.default = (new,)

    # overrides with higher elo
	def alter(self, current):
		rating = current[0]
		if self.new > rating:
			return (self.new,)
		else: return current

class winloss(object):
	def __init__(self, new):
		self.new = new 

		# tie
		if self.new == "t":
			self.default = (1,1,1)
		# win
		elif self.new == "w":
			self.default = (2,2,1)
		# loss
		else:
			self.default = (0,0,1)

	def alter(self, current):
		(weight,win,loss) = current

		#tie
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



