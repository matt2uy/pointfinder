import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

from flask import session, g, abort

from contextlib import closing

import sys
import json # json parsing from the client side.

import video_export # video processing module.
import video_export_no_reframe # a variant of the above file


UPLOAD_FOLDER = os.getcwd()+'/sample_video_files'#'/path/to/the/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'mp4'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
	return '.' in filename and \
		   filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():


	if request.method == 'POST':
		# check if the post request has the file part
		if 'file' not in request.files:
			#flash('No file part')
			return redirect(request.url)
		file = request.files['file']
		# if user does not select file, browser also
		# submit an empty part without filename
		if file.filename == '':
			flash('No selected file')
			return redirect(request.url)
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			return redirect(request.url)
	return render_template('upload.html')

	# previously:
	# return ...
	'''<!doctype html>
	<title>Upload new File</title>
	<h1>Upload new File</h1>
	<form method=post enctype=multipart/form-data>
	  <input type=file name=file>
	  <input type=submit value=Upload>
	</form>'''


from flask import send_from_directory


@app.route('/edit_video', methods=['POST'])
def edit_video(): #change to 'watch'

	# get the video export data from the client.
	stringified_array = request.form['export_data'] # seems like we are just getting a string, not json.
	##### parse the json...

	if stringified_array != "":

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

	else:
		print ("empty file")


	return render_template('upload.html')





@app.route('/uploads/<filename>')
def uploaded_file(filename):
	return send_from_directory(app.config['UPLOAD_FOLDER'],
							   filename)


if __name__ == '__main__':
	app.run(debug=True)
