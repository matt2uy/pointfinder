'''
Add some info on the webpage later:
- who?
- repository
- nltk link, wordnet link
- how it works (a loop, lol)
	- there is probably a more efficient way (constant time/memory?)
'''


from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template

from contextlib import closing

# dictionary libraries
from nltk.corpus import wordnet
import itertools

# configuration

# application:
app = Flask(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent = True) # if there is no FLASKR_SETTINGS, then run the one below
app.config.from_object(__name__)
   
@app.route('/')
def translate():
    return render_template('calculate.html')
    
@app.route('/calculate', methods=['POST'])
def add_entry(): 
	##### get the expression from the user-inputted form
	letters = str(request.form['text'])

	### temporary logging:
	print("----- user input: ", letters) # print out user input

	if len(letters) > 7:
		raise ValueError("Length of user input is too long")

	# user input bug handling:
	# convert to lowercase
	letters = letters.lower()
	# remove spaces
	letters = letters.replace(" ", "")

	# get a list of all valid permutations of "letters"

	def generate_word_permutations(given_letters):
		english_words = []

		minimum_word_length = 3
		for count in range(minimum_word_length, len(given_letters)+1):
			# find all permutations of the given_letters.
			for item in itertools.product(given_letters, repeat=count):
				# check if it's an english word first...
				potential_word = "".join(item)
				if wordnet.synsets(potential_word):
					# check if there are no letter duplicates...
					letter_valid = True
					temp_letters = given_letters
					for letter in potential_word:
						if letter in temp_letters:
							temp_letters = temp_letters.replace(letter, "", 1)
						else:
							letter_valid = False
					# then show it...
					if letter_valid:
						english_words.append(potential_word)

		# remove word duplicates
		possible_words = []

		for word in english_words:
			if word not in possible_words:
				possible_words.append(word)
		return possible_words

	unformatted_word_list = generate_word_permutations(letters)

	# gotta format the output into nice strings with commas inside them.
	word_list = ""
	output = "Original letters: " + letters + "<br/><br/>"

	# assuming that there are no 1 letter words in wordscapes.
	for curr_word_length in range(2, len(letters)):
		for word in unformatted_word_list:
			if len(word) == curr_word_length:
				word_list = word_list + word + ", "
		if word_list != "":
			output = output + str(curr_word_length) + " letters: " + word_list + "<br/><br/>"
		word_list = ""


	# (kind of) a "one-off" bug fix. Remove the final ", " in word_list.
	#word_list = word_list[:-2]

	# in case input is empty:
	if output ==  ("Original letters: " + letters + "<br/><br/>"):
		output += "There are no valid words. Maybe double check your letters?"

	return render_template('calculate.html', answer_text=output)


    
    
if __name__ == '__main__':
    app.run()
