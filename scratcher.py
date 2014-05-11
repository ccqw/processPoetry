# Run this on the command line:
# python scratcher.py <yourInputText.txt >yourOutputText.txt
# output text is optional, without it, it will print output to screen


import sys
import random

# Make a varaible to hold the initial poem
poemInit = ""

# prepare the text by populating poemInit with the initial poem
for line in sys.stdin:
	line = line.strip()
	poemInit += line + " "

poemInit = poemInit.split()

# determine points within the poem at which to perform scratch
def scratchDice(initialText):
	target = ""
	for n in range(len(initialText)):
		dice = random.randint(1,10)
		if dice > 8:
			# How many scratches?
			reps = random.randint(2,4)
			# For each time we want to scratch
			# pick a scratch length,
			for i in range(reps):
				sliceSizer = random.randint(1,5)
				# take a slice from the current word
				# to the end of the slice length
				sliceSize = n + sliceSizer
				sliced = ""
				sliceToJoin = initialText[n:sliceSize]
				#Add a space if it's not the last word in the join slice
				for word in sliceToJoin:
					if word == sliceToJoin[-1]:
						sliced += word
					else:
						sliced += word + " "

				target += sliced + " "
		else:
			target += initialText[n] + " "
	print target

# call the master function, feed it our input poem
scratchDice(poemInit)


