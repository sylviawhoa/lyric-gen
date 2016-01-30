import sys, io

linecount = 0;

# test_word = sys.argv[1]
file_name = sys.argv[1]

phoneme_dict = {}
syllable_dict = {}
vowel_dict = {}

# return array where
# [0] is string of 0 1 2 corresponding to the stress of the vowel phonemes
# [1] is array of vowel phonemes + stress
def count_syls(phonemes):
	ret = ['', [] ]
	for i in phonemes:
		for j in range(0, 3):
			if str(j) in i:
				ret[0] = ret[0] + str(j)
				ret[1].append(i)
	return ret


# make dict of phonemes...
for line in open('cmudict-0.7b.txt', 'r'):
	line = line.strip()
	words = line.split()
	word = words[0]
	phonemes = words[1:]

	# convert to array of syllables as 0, 1, 2
	syls_array = count_syls(phonemes)
	syls = syls_array[0]
	vowels = syls_array[1]


	syllable_dict[word] = syls
	phoneme_dict[word] = phonemes
	vowel_dict[word] = vowels




# convert song lyrics to syllables
song_syls = ''

for line in open(file_name, 'r'):
	line = line.strip()
	words = line.split()
	for word in words:
		word = word.upper()
		for char in word:
			# filter out non alpha but leave apostrophes
			if not char.isalpha() and char is not "'":
				word = word.replace(char, "")
		song_syls += str(syllable_dict[word])
	song_syls += '\n'
#	print song_syls

# print song_syls


# print phoneme_dict[test_word]
# print syllable_dict[test_word]
# print vowel_dict[test_word]


def writenewline(current_line):
	newsong_line = ""

	# for each line create a string current_line of syllables in the input song
	# and a string newsong_line of new lyrics
	# pick words from a markov chain to match the syllables/emphasis in the current line 


	c = len(current_line)
#	limit = 0
#	while (c > 0) and (limit < 5):			#for testing
	while c > 0: 
		# use markov function to choose a next word
		nextword = markovchainword()
#		nextword = "SYLVIA"			#for testing	

		# get syllable string for next word
		nextword_syl = syllable_dict[nextword]  
		print nextword_syl
		n = len(nextword_syl)
		# if the next word chosen by the markov chain has the correct
		# syllable count, it will be added to the new song lyrics
		# otherwise a new word will be chosen 
		if c > n:
			for i in range(0,n-1):
				if current_line[i] != nextword_syl[i]:
					break
				else:	
					current_line = current_line[n:c]
					newsong_line += nextword
	
		limit += 1
#	return newsong_line 
	print newsong_line

writenewline("10010001010100")

# TO DO: create signature for lyrics
# for line in open(file_name, 'r'):
