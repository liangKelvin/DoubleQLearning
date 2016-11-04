import blackjack
from pylab import *
from numpy import *
import random
 
numEpisodes = 1000000

alpha = 0.052
epsilon = 0.022
gamma = 1

q1 = 0.00001*rand(182,2)
q2 = 0.00001*rand(182,2)
q1[181, :] = 0
q2[181, :] = 0
qtotal = q1 + q2

def policy(s) :
	qTotal = q1 + q2
	return argmax(qTotal[s, :])

def learn(alpha, eps, numTrainingEpsiodes):
	returnSum = 0.0
	for episodeNum in range(numTrainingEpsiodes):
		s = blackjack.init() # initial state
		G = 0
		# pick a random number between 0 and 1
		# this represents the random greedy probability
		i = random.uniform(0,1) 
		
		# use random policy from part 1
		if i < epsilon :
			a = random.randint(0,1)

		else :
			qTotal = q1 + q2
			a = argmax(qTotal[s, :])

		stateAction = blackjack.sample(s,a)
		newState = stateAction[1]
		reward = stateAction[0]

		if newState == False :
			newState = 181

		#probabilty of 0.5 for update
		p = random.randint(0,1)
		
		if p == 0 :
			q1[s,a] = q1[s,a] + alpha * (reward + (gamma * q2[newState, argmax(q1[newState, :])]) - q1[s,a])

		elif p == 1 :
			q2[s,a] = q2[s,a] + alpha * (reward + (gamma * q1[newState, argmax(q2[newState, :])]) - q2[s,a])

		if newState == 181 :
			newState = False 
		

		s = newState
		G = G + reward

		while s != False :

			i = random.uniform(0,1) 
			
			# use random policy from part 1
			if i < epsilon :
				a = random.randint(0,1)
				
			else :
				qTotal = q1 + q2
				a = argmax(qTotal[s, :])

			stateAction = blackjack.sample(s,a)
			newState = stateAction[1]
			reward = stateAction[0]
			# allow for terminal state annoucement
			if newState == False :
				newState = 181

			#probabilty of 0.5 for update
			p = random.randint(0,1)
			# update q1
			if p == 0 :
				q1[s,a] = q1[s,a] + alpha * (reward + (gamma * q2[newState, argmax(q1[newState, :])]) - q1[s,a])
			# update q2
			elif p == 1 :
				q2[s,a] = q2[s,a] + alpha * (reward + (gamma * q1[newState, argmax(q2[newState, :])]) - q2[s,a])

			# reset the state assignment
			if newState == 181 :
				newState = False 
			
			s = newState
			G = G + reward
			
		#if episodeNum % 10000 == 0 and episodeNum != 0:
			#print("Average return so far: ", returnSum/episodeNum)
		returnSum = returnSum + G
	print("Average return: ", returnSum/numTrainingEpsiodes)
	blackjack.printPolicy(policy)


def evaluate(numEvaluationEpisodes):
	returnSum = 0.0
	for episodeNum in range(numEvaluationEpisodes):
		G = 0
		s = blackjack.init() # initial state
		a = policy(s)
		stateAction = blackjack.sample(s,a)
		newState = stateAction[1]
		reward = stateAction[0]
		G = G + reward

	# go through every state in the game of blackJ
		while newState != False :

			a = policy(newState)
			stateAction = blackjack.sample(newState, a)
			reward = stateAction[0]
			newState = stateAction[1]
			G = G + reward
		
		# Use deterministic policy from Q1 and Q2 to run a number of
		# episodes without updates. Return average return of episodes.
		returnSum = returnSum + G
	return returnSum / numEvaluationEpisodes

 
learn(alpha, epsilon, numEpisodes)
x = evaluate(numEpisodes)
print("return: ", x)
