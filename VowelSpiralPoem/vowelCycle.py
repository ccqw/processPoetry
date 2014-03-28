"""
This program was orignially intended to output all single syllable words that meet the vowel requirements, but
it only outputs words ending in vowels, which means that some of the vowels in the vowel spiral sequence are
not included, such as the Arpabet "IH" as in the vowel in "bit", because there are no English words that end in
that sound, much less single syllable ones.
"""

import phonemeDict
from phonemeDict import phonemeDictionary

#This is the pattern of vowel progression that we want to match
vowelSpiral = [['IY0','IY1','IY2'],['IH0', 'IH1', 'IH2'],['UW0', 'UW1', 'UW2'],['UH0','UH1','UH2'], ['OW0', 'OW1', 'OW2'], ['AO0', 'AO1', 'AO2'], ['AH1', 'AH2'], ['AA0', 'AA1', 'AA2'], ['AE0', 'AE1', 'AE2'], ['EH0', 'EH1', 'EH2'], ['EY0', 'EY1', 'EY2'], ['AH0']]

#One way to check if something 
#is a vowel phone is whether the phone string contains 
#a number, which indicates stress. This dictionary
#contains 3 stress levels: unstressed (0), primary stress (1),
#and secondary stress (2)
vowelCheck = ['0','1','2'] 

#This is the empty string we will put our spiral poem into
spiralPoem = ""

#Start with first required phone in our vowel spiral poem format
for phone in range(len(vowelSpiral)):
	#We'll look at each word in the phoneme Dictionary
	foundWord = False
	for entry in phonemeDictionary:
		#And at each phone that makes up each word

		#let's initialize our vowel counter
		vowelCount = 0
		for item in phonemeDictionary[entry]:
			for stressIndex in vowelCheck:
				#if it is a vowel...
				if stressIndex in item:
					#then we'll increment the vowel count on the word
					vowelCount += 1
		#if it's a word with one vowel, then we'll check it out
		if vowelCount == 1:
			#then we'll look at each variant of our phone requirement
			#that would fill the requirement
			for variant in range(len(vowelSpiral[phone])):
				for stressIndex in vowelCheck:
					#if it is a vowel...
					if stressIndex in item:
						#and if it matches
						if item == vowelSpiral[phone][variant]:
							#we'll store that word in a temporary variable
							newWord = entry
							#convert it to lowercase, and append it to our
							#poem string, plus a space for formatting/readability
							spiralPoem += newWord.lower() + " "
							foundWord = True
							

print spiralPoem
