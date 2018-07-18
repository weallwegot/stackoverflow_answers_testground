"""
I'm not sure exactly what is being asked but somethings to consider (in no particular order) if you are building a bot that is taking in raw user input.

1. capitalization sensitivity
2. spell check
3. understanding intent simplistically

if your environment allows access to libraries there are some I might consider checking out [TextBlob](https://textblob.readthedocs.io/en/dev/)
"""

# core function

# <!--- language: python ---->

from textblob import TextBlob, Word
import copy

def score_intent(rawstring,keywords,weights=None,threshold=0.01,debug=False):
	"""
	rawstring: string of text with words that you want to detect
	keywords: list of words that you are looking for
	weights: (optional) dictionary with relative weights of words you want
	threshold: spellcheck confidence threshold
	debug: boolean for extra print statements to help debug
	"""
	allwords = TextBlob(rawstring).words
	allwords = [w.upper() for w in allwords]
	keywords = [k.upper() for k in keywords]
	processed_input_as_list = spellcheck_subject_matter_specific(rawstring,keywords,threshold=threshold,debug=debug)
	common_words = intersection(processed_input_as_list,keywords)
	intent_score = len(common_words)
	if weights:
		for special_word in weights.keys():
			if special_word.upper() in common_words:
				# the minus one is so we dont double count a word.
				intent_score = intent_score + weights[special_word] -1 

	if debug:
		print "intent score: %s" %intent_score
		print "words of interest found in text: {}".format(common_words)
	# you could return common_words and score intent based on the list.
	# return common_words, intent_score
	return common_words



# utilities for intersection & spellchecking

# <!--- language: python ---->

def intersection(a,b):
	"""
	a and b are lists
	function returns a list that is the intersection of the two
	"""
	return list(set(a)&set(b))



def spellcheck_subject_matter_specific(rawinput,subject_matter_vector,threshold=0.01,capitalize=True,debug=False):
	"""
	rawinput: all the text that you want to check for spelling
	subject_matter_vector: only the words that are worth spellchecking for (since the function can be sort of sensitive it might correct words that you don't want to correct)
	threshold: the spell check confidence needed to update the word to the correct spelling
	capitalize: boolean determining if you want the return string to be capitalized.
	"""
	new_input = copy.copy(rawinput)

	for w in TextBlob(rawinput).words:
		spellchecked_vec = w.spellcheck()
		if debug:
			print "Word: %s" %w
			print "Spellchecked Guesses & Confidences: %s" %spellchecked_vec
			print "Only spellchecked confidences greater than {} and in this list {} will be included".format(threshold,subject_matter_vector)

		corrected_words = [z[0].upper() for z in spellchecked_vec if z[1] > threshold] 
		important_words = intersection(corrected_words,subject_matter_vector)
		for new_word in important_words:
			# this is hacky, but cs will correc to 'c' and thats bad
			new_input = new_input + ' ' + new_word


	inputBlob = TextBlob(new_input)
	processed_input = inputBlob.words
	if capitalize:
		processed_input = [word.upper() for word in processed_input]

	return processed_input




discord_str = "Hi, i want to talk about codee and pYtHon"
words2detect = ["python","code"]

score_intent(rawstring=discord_str,keywords=words2detect,threshold=0.01,debug=True)









