from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template

from contextlib import closing

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
	
	# input mathematical expression from buttons here:
	expression_string = "800+10-900"	# no spaces

	##### get the expression from the user-inputted form
	expression_string = str(request.form['text'])

	# the expression is finalized when the '=' button is pressed
	##### -> determine if equal button is pressed
	# equal_button = pressed
	# if equal_button pressed:

	# variables needed for the calculation
	expression_list = [];
	operand_list = ['+', '-', '*', '/']
	answer = 0

	# functions to convert the expression into an answer
	def convert_expression_to_list(expression_string, expression_list):
		# split numbers out
		import re
		expression_list = re.split('([+-])', expression_string)

		return expression_list

	def expression_error_check(expression_list):
		expression_valid = True
		# run through the entire expression
		for item in expression_list:
			# first item is not a constant
			if expression_list.index(item) == 0 and item in operand_list:
				expression_valid = False

		# two operands put together
		# parentheses don't reconcile
		# tell the user what they did wrong
		return expression_valid

	def evaluate_expression(expression_list, answer):
		if expression_error_check(expression_list) == True:
			# go through each 'item', or character in the equation
			for item in expression_list:
				# skip operands, current item is a constant (1, 2, 3...):
				if item not in operand_list:
					# if this is the first item --> set the answer equal to item
					if expression_list.index(item) == 0:
						answer = int(item)
					# previous item was an add operand --> add
					elif expression_list[expression_list.index(item)-1] == '+':         
							answer += int(item)			
					# previous item was a subtract operand --> subtract
					elif expression_list[expression_list.index(item)-1] == '-':         
							answer -= int(item)
			return answer

		# Error found
		else:
			return "Error"


	# convert the expression into an answer
	expression_list = convert_expression_to_list(expression_string, expression_list)
	print (expression_list)

	answer = evaluate_expression(expression_list, answer)
	print (answer)
	
	'''
	- find out a way to configure web app buttons
	- integrate this with the web app
	- multiply/divide
	- negative numbers
	- other funnctions
	- error checking
	'''

	print ("expression string:", answer)

	return render_template('calculate.html', answer_text=answer)


    
    
if __name__ == '__main__':
    app.run()
