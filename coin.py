#! /usr/bin/env python

import random
possible = ['h', 't'] # heads & tails

name = raw_input("What's your name? ") # probably the users name won't change in one game so I put it outside.

while True:
	score = 0; life = 2.0 # initializing
	highScores = []
	
	try:
		fileH = open("score.dat", "r+")
		fileC = open("score.cod", "r+")
		fileHighs = fileH.readlines()
		fileCode = int(fileC.read()) # Encrypt "key"
		for i in range(len(fileHighs)): # Each data (score + name)
			ScoreAndName = fileHighs[i].split()
			highScores.append([int(ScoreAndName[0]) ^ fileCode, ScoreAndName[1]]) # This is the decryption part -- a XOR b XOR b = a -- that's my "encryption"
		print("\nCoin Guessing Game.   All time high score: {} (by {})".format(highScores[0][0],highScores[0][1]))
	except:
		fileH = open("score.dat", "w") # no files then create one
		fileC = open("score.cod", "w")
		print("\nCoin Guessing Game.   No high score yet.")
	
	
	while True: # Guessing
		while True:
			guess = raw_input("\nPredict heads or tails: ")
			if(guess[0].lower() not in possible): # "donkey"
				print("I don't understand.")
			else:
				break
		if(guess[0].lower() == random.choice(possible)): 
			score += 1
			life += 0.8 # Yes this will madly increase the time
			print("You got it! You have {} lives. Your score is {}.".format(round(life, 1), score))
		else:
			life -= 1
			print("It's not right. You have {} lives.".format(round(life, 1)))
			
			
			if(life <= 0): # Game over
				highScores.append([score, name]) # add the new one's score
				highScores.sort(reverse = True) # and sort it
				highScores = highScores[:5]
				print("\nGame over. Your score: {}. ".format(score))
				
				for i in range(5):
					try:
						print("High score {}: {} (by {}).".format(i + 1, highScores[i][0], highScores[i][1]))
					except:
						break
				
				code = random.randint(1,100)
				fileH = open("score.dat", "w") # Each time, "refresh" them
				fileC = open("score.cod", "w")
				
				fileC.write(str(code)) # put in the new code
				for highScore in highScores:
					fileH.write(str(highScore[0] ^ code) + ' ' + highScore[1] + '\n') # This is the encryption part -- a XOR b XOR b = a -- that's my "encryption"
					
				break
	fileH.close() # close them
	fileC.close()
	
	again = raw_input("\nWould you want to play again? ")
	if(again[0].lower() != 'y'):
		break