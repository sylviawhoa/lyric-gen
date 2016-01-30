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
	print song_syls

print song_syls


# print phoneme_dict[test_word]
# print syllable_dict[test_word]
# print vowel_dict[test_word]


# TO DO: create signature for lyrics
# for line in open(file_name, 'r'):