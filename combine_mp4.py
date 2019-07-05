# concatenate .mp4 files

import subprocess
import os

def join_video(video_clip_paths):
	### Concatenate video clips from the list 'video_clip_paths'

	# Use an intermediary file (clip_list.txt) to store 'video_clip_paths'
	# add file paths to clip_list.txt in chronological order.
	clip_list_file = open("sample_video_files\\clip_list.txt","w+")

	for i in range(len(video_clip_paths)):
		clip_list_file.write("file '" + str(video_clip_paths[i])+"'"+"\n")
		
	# remember to close the file!
	clip_list_file.close() 


	# Append a timestamp to the output filename.
	import datetime
	output_name = "out"+str(datetime.datetime.now().strftime("%m-%d-%y[%H-%M-%S]"))+".mp4"
	
	# concatenate all videos in clip_list.txt
	subprocess.call('ffmpeg -safe 0 -f concat -i sample_video_files/clip_list.txt -c copy sample_video_files\\'+output_name)

def get_video_filenames():
	# 1. ask the user for what files (and order to put them in)
	from tkinter.filedialog import askopenfilename
	# uno

	filename_list = []
	currently_selecting_files = True

	while currently_selecting_files:

		filename = os.path.basename(askopenfilename())
		# get filename.


		# user clicked 'cancel' or no file was selected.
		if filename == '':
			currently_selecting_files = False
		# a 'non-empty' file was selected.
		else:
			filename_list.append(filename)



		print(filename_list)

	# note: maybe use some type of try/catch structure up ahead.
	#	...or even in the previous code block.

	# if no files have been selected.
	if len(filename_list) == 0:
		print("No file has been selected.")
	# files have been selected.
	else:
		print("You have selected these files (in order):", filename_list)
		# concatenate all videos in clip_list.txt
		join_video(filename_list)

if __name__ == '__main__':
	get_video_filenames()
		