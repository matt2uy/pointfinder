import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'sample_video_files/'
ALLOWED_EXTENSIONS = set(['html'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':

    	### these error handlers don't seem to work.
        # # check if the post request has the file part
        # if 'file' not in request.files:
        #     flash('No file part')
        file = request.files['file']
        # # if user does not select file, browser also
        # # submit an empty part without filename
        # if file.filename == '':
        #     flash('No selected file')

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    return render_template('working_upload.html')

if __name__ == '__main__':
	app.run(debug=True)
