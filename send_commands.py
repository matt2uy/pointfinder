from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template

from contextlib import closing



# application:
app = Flask(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent = True) # if there is no FLASKR_SETTINGS, then run the one below
app.config.from_object(__name__)
 


#####                 #####

@app.route('/')
def translate():
    return render_template('calculate.html')
    
@app.route('/calculate', methods=['POST'])
def add_entry(): 
	##### get the expression from the user-inputted form

	
	return render_template('calculate.html', answer_text="bonjour")


    
    
if __name__ == '__main__':
    app.run()
