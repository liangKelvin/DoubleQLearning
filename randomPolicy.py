import blackjack
from pylab import *
import random
numEpisodes = 1

returnSum = 0.0
# initial state at the start of a new blackjack game


#seed random
#random.seed(a = None, version = 2)


for episodeNum in range(numEpisodes):
	G = 0
	gamma = 1 
	action = random.randint(0,1)
	state = blackjack.init()
	stateAction = blackjack.sample(state, action)
	reward = stateAction[0]
	state = stateAction[1]
	G = G + reward
	print("reward1, newstate", reward, state)

	# go through every state in the game of blackJ
	while state != False :

		action = random.randint(0,1)
		stateAction = blackjack.sample(state, action)
		reward = stateAction[0]
		state = stateAction[1]
		print("reward, newstate", reward, state)
		G = G + reward
		
	print("Episode: ", episodeNum, "Return: ", G)
	returnSum = returnSum + G
print("Average return: ", returnSum/numEpisodes)
