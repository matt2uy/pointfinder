from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template

from contextlib import closing



# application:
app = Flask(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent = True) # if there is no FLASKR_SETTINGS, then run the one below
app.config.from_object(__name__)
 
#### video processing ####

import sys
sys.path.append('cmd_interface')
import demo

'''
# spit out "high potential" timestamps from a video
def get_video_timestamps():
	# maybe do a 'profile' to see how fast things are going?
	import time 
	start = time.time() # ^ like this?

	# Capture motion data from various "areas" of the video
	print("Capturing video...")
	historical_colour_value, scoreboard_first_row_values = demo.capture_video()

	timestamps = demo.convert_list_to_timestamps(historical_colour_value)
	print("Done...")

	# print out time elapsed.
	end = time.time()
	elapsed = round(end - start, 2)
	print ("Video traversal took about", elapsed, "seconds.")
	return timestamps
'''

#####                 #####

@app.route('/')
def translate():
    return render_template('calculate.html')
    
@app.route('/calculate', methods=['POST'])
def add_entry(): 
	##### get the expression from the user-inputted form

	#timestamps = get_video_timestamps()

	return render_template('calculate.html', answer_text=timestamps)


    
    
if __name__ == '__main__':
    app.run()
