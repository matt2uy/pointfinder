'''
Matthew Uy 2017

Notes:

0. Look at t-10, 8, 6, 4, 2 frames to get scoreboard changes.

0.5. Look at the studies in the chrome tabs on the right.

1. why is it so slow? optimize (remove redundant stuff when traversing through each frame) 
	- maybe because I am "traversing" through every pixel in the frame.
	- isn't this advised against in the opencv documentation? because it's a "numpy array" or something?

2. clean up code -> remove cruft -> variable names -> refactor (modularize)

after: should we track colour change in rgb?
	- or (convert to greyscale first)?
	- or (convert to the opposite colour of the tennis court first)?

- - - - - - - - - - 

Resources:

- usask paper on tracking a tennis ball: http://www.collectionscanada.gc.ca/obj/s4/f2/dsk3/SSU/TC-SSU-08302006125935.pdf
- tennis ball + player tracking: http://epubs.surrey.ac.uk/733265/1/BMVC05.pdf

- read/display/write to a video: https://www.learnopencv.com/read-write-and-display-a-video-using-opencv-cpp-python/
- loop through pixels: https://pythonspot.com/en/image-data-and-operations/
- sample gameplay image: https://i.ytimg.com/vi/nQ7fkaJJyF0/maxresdefault.jpg

- hough circle http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_houghcircles/py_houghcircles.html
- faster pixel loop? https://www.pyimagesearch.com/2017/08/28/fast-optimized-for-pixel-loops-with-opencv-and-python/

- more resources http://answers.opencv.org/question/69691/informative-websites-related-to-opencv/
- 'tennis' query: http://answers.opencv.org/questions/scope:all/sort:activity-desc/page:1/query:tennis/
- computer vision textbook: http://szeliski.org/Book/drafts/SzeliskiBook_20100903_draft.pdf

- edit a video with this? https://pypi.python.org/pypi/moviepy
... or this? https://gist.github.com/nkint/8576156

'''

# Video files
video_path = "full_match.mp4" 

# opencv video attribute constants
VIDEO_CAPTURE_WIDTH = 3
VIDEO_CAPTURE_HEIGHT = 4
VIDEO_CAPTURE_FRAMES_PER_SECOND = 5

import cv2
import numpy as np
import matplotlib.pyplot as plt
from moviepy.editor import VideoFileClip, concatenate_videoclips
import sys

##### Video Editing #####

def trim_video(start_time, end_time, new_file_path, source_file_path):
	''' Trim video using ffmpeg.
	note: not sure what unit 'start_frame' is. Is it frames/seconds/...etc?

	Sample, where video_path = "full_match.mp4":
	>>> trim_video(1000, 1100, "source_match.mp4", new_video_path)
	'''	
	video = VideoFileClip(source_file_path)

	# if the video ends before the point is finished:
	if end_time == -1:
		trimmed_video = video.subclip(start_time)
	else:
		trimmed_video = video.subclip(start_time, end_time)

	trimmed_video.write_videofile(new_file_path, codec='libx264') # codec is a default?
 
# note: is specifying the parameter type for only one function "inconsistent"?
# note: is there any video quality downgrade/lost artifacts? 

def merge_video(list_of_video_paths, new_file_path):

	list_of_videos = []
	for video_path in list_of_video_paths:
		list_of_videos.append(VideoFileClip(video_path))
	# note: why do the trimmed/merged clips freeze sometimes? is it ffmpeg?
	edited_video = concatenate_videoclips(list_of_videos)
	edited_video.write_videofile(new_file_path)

def cut_video_in_points_of_interest(point_timestamps):
	'''
	point_timestamps is in the form of: list[list[start_time, end_time]]
	'''
	list_of_video_paths = []

	for i in range(len(point_timestamps)):
		# video cuts before point ends
		if len(point_timestamps[i]) == 1: 
			trim_video(point_timestamps[i][0], -1, "auto_generated_files/newvid" + str(i) + ".mp4", video_path)
		# just a regular point
		else: 
			trim_video(point_timestamps[i][0], point_timestamps[i][1], "auto_generated_files/newvid" + str(i) + ".mp4", video_path)
		list_of_video_paths.append("auto_generated_files/newvid" + str(i) + ".mp4")
	# concatenate all trimmed video files.
	merge_video(list_of_video_paths, "edited_video.mp4")


'''# 8:50pm, 11/21/17
- remove later... once cut_video_in_points_of_interest is finished

- note that clean_up_noisy_timestamps() returns the provided parameter.
'''
'''
# the algorithm produces margins that are slightly off, so I manually added some for now
point_timestamps = [[13.0, 21.933333333333334-2], [37.4-1, 39.0+2], [56.833333333333336, 61.666666666666664], [82.4, 88.43333333333334], [95.3]]
# removed the floats -> kind of removed one pause for the last point
#point_timestamps = [[12-2, 22], [34-2, 39+2], [54-2, 62+2], [82-2, 88+2], [95]]

cut_video_in_points_of_interest(point_timestamps)
'''

##### Video Capture #####

def capture_video():
	cap = cv2.VideoCapture(video_path)
	fgbg = cv2.createBackgroundSubtractorMOG2()

	# Check if camera opened successfully
	if (cap.isOpened() == False): 
		print("Error opening video stream or file")

	historical_colour_value = []

	# get video properties
	width = int(cap.get(VIDEO_CAPTURE_WIDTH))
	height = int(cap.get(VIDEO_CAPTURE_HEIGHT))
	frames_per_second = float(cap.get(VIDEO_CAPTURE_FRAMES_PER_SECOND))
	num_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) # used for video length

	##### framing properties:
	### entire view
	left = 0#(width//10)
	right = width#width - (width//10)
	top = 0 #+ (height//3)
	bottom = height

	current_frame = 0

	# Read until video is completed
	while(cap.isOpened()):
		
		# 1. capture the OG frame
		ret, frame = cap.read()
		# 2. apply canny edge
		frame = cv2.Canny(frame,200,255,apertureSize = 3)
		# 3. apply background subtraction
		frame = fgbg.apply(frame)


		current_frame += 1

		if ret == True:
			############### Entire view
			total_colour_value = 0

			# 1. Look at the entire screen
			#cv2.rectangle(frame,(left, top),(right, bottom),(0,255,0),5) # test: draw it on top of the video
			
			# traverse every pixel in the image. 
			#(maybe iterate through every (12?) pixels to increase speed?) -> scale x,y?

			for pixel_y in range(top, bottom, 12):
				for pixel_x in range(left, right, 12):
					# save the 'total' average pixel value
					total_colour_value += frame[pixel_y][pixel_x]

		

			# smooth out data:
			if total_colour_value > 10000:
				total_colour_value = 10000

			# append current frame data
			historical_colour_value.append(total_colour_value)


			# print percentage of video "traversed".
			i = int(round(current_frame/num_frames*100, 1))
			sys.stdout.write("\r%d%%" % i) # is there documentation for this? looks interesting.
			sys.stdout.flush()
			'''if i >= 99: # Add a newline when the progress text is complete.
				sys.stdout.write("\r%d%%" % 100)
				print ("")'''

			# Display the resulting frame
			cv2.imshow('Frame', frame)

		 
			# Press Q on keyboard to exit
			if cv2.waitKey(1) & 0xFF == ord('q'):
				break
	 
		# Break the loop
		else: 
			break
	 
	# When everything is done, release the video capture object
	cap.release()
	 
	# Closes all the frames
	cv2.destroyAllWindows()

	# "complete" the progress display
	sys.stdout.write("\r%d%%" % 100)
	print ("")

	return historical_colour_value

##### Video Data Processing #####
def get_serve_attempt_timestamps(low_points, high_points):
	''' Compare the high and low points, and maybe group them -> 
    -> thin the herd 
    -> get a distinct set of serve attempts (call the list 'point_start')

	'''
	high_low_delta = 1
	serve_attempts = []
	serve_attempt_delta = 5.0

	for low_point in low_points:
		for high_point in high_points:
			if low_point[0] < high_point[0] + high_low_delta and low_point[0] > high_point[0] - high_low_delta: 
		
				# narrow down serve_attempts
				serve_attempt_is_validated = True
				# if they are within serve_attempt_delta seconds of each other
				for serve_attempt in serve_attempts:
					if low_point[0] < serve_attempt + serve_attempt_delta and low_point[0] > serve_attempt - serve_attempt_delta:
						serve_attempt_is_validated = False
					

				if serve_attempt_is_validated:
					#print (low_point[0])
					serve_attempts.append(low_point[0])
	return serve_attempts

def convert_list_to_timestamps(list_of_values):
	# maybe use this if it takes too long to use 'every' frame. But it probably shouldn't take that long though.
	# scale the values to the appropriate time frame, given the fps of the video.
	# note: how do you get the fps of a video file? from ffmpeg? or OpenCV?
	# note: replace 30 with frames_per_second, once capture_video is refactored properly
	'''for i in range(0, len(raw), 1): 
		# maybe store in a dict instead.
		#frames_per_second = 
		#historical_colour_value[i/frames_per_second] = raw[i]
		historical_colour_value.append(raw[i])'''


	# get the first, second and third derivatives of the historical_colour_value list.
	displacement_list = get_derivative_of_list(list_of_values)
	velocity_list = get_derivative_of_list(displacement_list)
	acceleration_list = get_derivative_of_list(velocity_list)

	# Convert motion average data into a plotter-digestible format
	# displacement
	displacement_average = get_modified_mean(displacement_list, 1)
	displacement_average_list = equalize_list_length(displacement_average, len(displacement_list))

	# velocity
	velocity_average = get_modified_mean(velocity_list, 1)
	velocity_average_list = equalize_list_length(velocity_average, len(velocity_list))

	# acceleration
	acceleration_average = get_modified_mean(acceleration_list, 5)
	acceleration_average_list = equalize_list_length(acceleration_average, len(acceleration_list))

	acceleration_lower_average = get_modified_mean(acceleration_list, 1.5)
	acceleration_lower_threshold_list = equalize_list_length(acceleration_lower_average, len(acceleration_list))

	# note: replace 30 wtih frames_per_second
	high_points = find_points_above_threshold(acceleration_list, acceleration_average, 30)

	# delta is the range of y-values at which we are narrowing down our search.
	# Maybe make it represent an abs() value? ...
	# ... Currently it is not (see the function call below)
	threshold_delta = 100  
	low_points = find_points_within_threshold(acceleration_list, acceleration_lower_average, acceleration_lower_average-threshold_delta, 30)

	low_points = remove_singleton_frames(low_points)

	points_of_interest = get_serve_attempt_timestamps(low_points, high_points)

	# note: temp -> for testing
	#plot_graph([acceleration_list])

	return points_of_interest

def get_derivative_of_list(list_of_values):
	''' Note: the list of derivatives will be one element lower than the input list.
	'''
	derivative_list = []
	#derivative_list.append(0)
	for i in range(len(list_of_values)):
		derivative_list.append(abs(list_of_values[i]-list_of_values[i-1]))
	# ensure that the list index 'lines up' with the chronological timeline
	derivative_list.pop(0)
	return derivative_list


##### Diagnostic/Testing #####

def plot_graph(list_of_plots):
	""" Plot a graph using matplotlib, given a list_of_plots, which is a list
	of list of y values to be plotted. Each x-value in each list is separated 
	by a y-value of 1.	
	
	>>> plot_graph([acceleration_average_list, acceleration_list])
	# plots a graph of the acceleration values and their mean.
	"""

	for plot in list_of_plots:
		plt.plot(plot)
	plt.show() 


############################## 

if __name__ == '__main__':
	# Add test cases later?
	#import doctest
	#doctest.testmod()
	
	# maybe do a 'profile' to see how fast things are going?
	import time 
	start = time.time() # ^ like this?

	# Capture motion data from various "areas" of the video
	print("Capturing video...")
	historical_colour_value = capture_video()
	print("Done...")

	# print out time elapsed.
	end = time.time()
	elapsed = round(end - start, 2)
	print ("Video traversal took about", elapsed, "seconds.")


	# manipulate data
	historical_colour_value = get_derivative_of_list(historical_colour_value)
	historical_colour_value = get_derivative_of_list(historical_colour_value)
	plot_graph([historical_colour_value])
