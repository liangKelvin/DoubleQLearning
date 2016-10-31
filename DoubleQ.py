import blackjack
from pylab import *
from numpy import *
 
numEpisodes = 1000
returnSum = 0.0

alpha = 0.001
epsilon = 1
gamma = 1

q1 = 0.00001*rand(181,2)
q2 = 0.00001*rand(181,2)

 

for episodeNum in range(numEpisodes):
	s = blackjack.init() # initial state
	G = 0
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
	print("reward1, newstate1", reward, newState)

	#probabilty of 0.5 for update
	p = random.randint(0,1)
	
	if p == 0 and newState != False :
		q1[s,a] = q1[s,a] + alpha * (reward + (gamma * q2[newState, argmax(q1[newState, :])]) - q1[s,a])

	elif p == 1 and newState != False :
		q2[s,a] = q2[s,a] + alpha * (reward + (gamma * q1[newState, argmax(q2[newState, :])]) - q2[s,a])
	

	s = newState
	G = reward + G

	while s != False :

		G = 0
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
		print("reward, newstate", reward, newState)

		#probabilty of 0.5 for update
		p = random.randint(0,1)
		
		if p == 0 and newState != False :
			q1[s,a] = q1[s,a] + alpha * (reward + (gamma * q2[newState, argmax(q1[newState, :])]) - q1[s,a])

		elif p == 1 and newState != False :
			q2[s,a] = q2[s,a] + alpha * (reward + (gamma * q1[newState, argmax(q2[newState, :])]) - q2[s,a])
		

		s = newState
		G = reward + G
	

	print("Episode: ", episodeNum, "Return: ", G)
	returnSum = returnSum + G
print("Average return: ", returnSum/numEpisodes)