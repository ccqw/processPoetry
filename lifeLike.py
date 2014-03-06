#life after like:
#run this program in UNIX with two text files as arguments:
#this program takes two files as arguments and uses all the sentences
#in the first file with the word "like" and all the sentences in the
#second file with the word "a" to create new similes and statements
#of fondness

import random
import sys
from sys import argv

#The first argument will be where we get the part of the sentence
#up to and including like
likeFile = sys.argv[1]
#The second argument will be where we get the part of the sentence
#including and after "a"
similiesFile = sys.argv[2]

#initialize buffer strings
likeBuffer = ''
similiesBuffer = ''

#initialize lists for lines split at periods
likeLines = []
similiesLines = []

#initialize lists for lines containing our keywords 
#("like" and "a"), respectively, to be pasted together
likeLinesCut = []
similiesLinesCut = []

#populate a large string with the data from the like file
for line in open(likeFile):
	likeBuffer += line

#split the file into pieces like sentences 
#(use a period as the delimeter)
likeLines = likeBuffer.split('.')

#check our new pseudo sentences for usability
for item in likeLines:
	offset = item.find(" like ") #if they contain "like", find its location
	if offset != -1:
		likeLinesCut.append(item[:offset+6]) #and save the usable part of the sentence

#let's do the same thing for the similies file:
#populate a large string with the data from the similies file
for line in open(similiesFile):
	similiesBuffer += line

#split the file into pieces like sentences 
#(use a period as the delimeter)
similiesLines = similiesBuffer.split('.')

#check our new pseudo sentences for usability
for item in similiesLines:
	offset = item.find(" a ") #if they contain "a", find its location
	if offset != -1:
		similiesLinesCut.append(item[offset+1:]) #and save the usable part of the sentence

#Shuffle the sources
random.shuffle(likeLinesCut)
random.shuffle(similiesLinesCut)

#Find out which set of source material is shorter
if len(likeLinesCut) > len(similiesLinesCut):
	shorter = len(similiesLinesCut)
else:
	shorter = len(likeLinesCut)

#In order to print a reasonable amount of output,
#Print a maximum of 50 lines, or else as many lines
#as there are items in the shorter list material
if shorter > 50:
	for i in range(50):
		newLine = likeLinesCut[i] + similiesLinesCut[i] + ". "
		print newLine
if shorter < 50:
	for i in range(shorter):
		newLine = likeLinesCut[i] + similiesLinesCut[i] + ". "
		print newLine