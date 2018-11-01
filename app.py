from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template

from contextlib import closing

import sys
import json # json parsing from the client side.
import video_export # video processing module.



# application:
app = Flask(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent = True) # if there is no FLASKR_SETTINGS, then run the one below
app.config.from_object(__name__)
 
#### video processing ####
sys.path.append('cmd_interface')
#import demo

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


#####                 #####

@app.route('/')
def home():
    return render_template('watch.html')
    
@app.route('/edit_video', methods=['POST'])
def edit_video(): #change to 'watch'

	# get the video export data from the client.
	stringified_array = request.form['export_data'] # seems like we are just getting a string, not json.

	##### parse the json...

	# convert the stringified list into an actual list
	stringified_list = json.loads(stringified_array)

	# save the clips in a list of dicts
	video_clips = []

	for stringified_dict in stringified_list:
		video_clips.append(stringified_dict)


	#####

	print('exporting video...')

	# process the video
	video_export.export(video_clips)

	print('finished export.')


	return render_template('watch.html')



# @app.route('/export', methods=['GET'])
# def export_video():
# 	reframe_instances = # get these from the user

# 	return # estimated time left
    
    
if __name__ == '__main__':
    app.run(debug=True)
