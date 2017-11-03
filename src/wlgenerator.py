import re
import sys
import os
import time

#create variations of baseword such as 55baseword and baseword55
def number_blend(baseword):
	count = 0
	wordlist = [baseword, baseword.title(), baseword.lower(), baseword.upper()]
	common_numbs = ["123", "456", "789", "111", "222", "333", "444", "555", "666", "777", "888", "999"]
	while count < 100:
		wordlist.append(baseword.upper() + str(count))
		wordlist.append(baseword.lower() + str(count))
		wordlist.append(baseword.title() + str(count))
		wordlist.append(str(count) + baseword.upper())
		wordlist.append(str(count) + baseword.lower())
		wordlist.append(str(count) + baseword.title())
		if count < 12:
			wordlist.append(baseword.upper() + str(common_numbs[count]))
			wordlist.append(baseword.lower() + str(common_numbs[count]))
			wordlist.append(baseword.title() + str(common_numbs[count]))
			wordlist.append(str(common_numbs[count]) + baseword.upper())
			wordlist.append(str(common_numbs[count]) + baseword.lower())
			wordlist.append(str(common_numbs[count]) + baseword.title())
		count += 1
                    
	return wordlist

#create variations of words in baselist by replacing some characters with numbers
def leet_blend(baselist):
	wordlist = []

	for item in baselist:
		#singles
		zeros = re.sub("o", "0", item)
		ones = re.sub("i", "1", item)
		threes = re.sub("e", "3", item)
		fours = re.sub("a", "4", item)
		fives = re.sub("s", "5", item)
		wordlist.extend((zeros, ones, threes, fours, fives))

		#combination of all
		mix1 = re.sub("i", "1", zeros)
		mix2 = re.sub("e", "3", mix1)
		mix3 = re.sub("a", "4", mix2)
		finalmix = re.sub("s", "5", mix3)
		wordlist.append(finalmix)

	return wordlist

#create variations of words in baselist by adding special characters
def special_blend(baselist):
	resultlist = []
	special_chars = ["-", "+", "@", "?", "!", "%", "&", "#", "$", "*", "^", "=", "."]
	count = 0

	while count < 13:
		for item in baselist:
			resultlist.append(item)
			resultlist.append(item + special_chars[count])
			resultlist.append(special_chars[count] + item)
		count += 1

	#return unique values
	return set(resultlist)

try:
	inputfile = sys.argv[1]
	outputfile = sys.argv[2]
except IndexError:
	print("Usage: python wlgenerator.py <inputfile> <outputfile>")
	sys.exit()

start_time = time.time()

count = 0
total = 0

#getting wordcount from inputfile
with open(inputfile) as getcount:
	for line in getcount:
		count += 1
        
with open(inputfile) as ip_f:
	progress = 0
	for line in ip_f:
		currentlist = leet_blend(number_blend(line.strip()))
		result = special_blend(currentlist)
		with open(outputfile, 'a') as op_f:
			for value in result:
				total += 1
				op_f.write(value + "\n")
		progress += 1

		#this is for linux/osx, if you use windows, replace 'clear' with 'cls'
		os.system('clear')
		print("Creating variation " + str(progress) + "/" + str(count))

elapsed_time = time.time() - start_time
print("Total of " + str(total) + " password variations created!")
print("Time elapsed: " + str(round(elapsed_time, 2)) + "s")
