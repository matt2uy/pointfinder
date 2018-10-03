# Video files
video_path = "D:/DCIM/100GOPRO/9-18-18 Driving Range"

# opencv video attribute constants
VIDEO_CAPTURE_WIDTH = 3
VIDEO_CAPTURE_HEIGHT = 4
VIDEO_CAPTURE_FRAMES_PER_SECOND = 5

import cv2
import numpy as np
#import matplotlib.pyplot as plt
from moviepy.editor import VideoFileClip, concatenate_videoclips
import sys

##### Video Editing #####

### using moviepy

def trim_video(start_time, end_time, new_file_path, source_file_path):
	''' Trim video using ffmpeg.
	note: not sure what unit 'start_frame' is. Is it frames/seconds/...etc?

	Sample, where video_path = "full_match2.mp4":
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

# export video
def export_video(point_timestamps, origin_files):
	'''
	point_timestamps is in the form of: list[list[start_time, end_time]]
	'''
	list_of_video_paths = []

	for i in range(len(point_timestamps)):
		# video cuts before point ends
		if len(point_timestamps[i]) == 1: 
			trim_video(point_timestamps[i][0], -1, "newvid" + str(i) + ".mp4", origin_files)
		# just a regular point
		else: 
			trim_video(point_timestamps[i][0], point_timestamps[i][1], "newvid" + str(i) + ".mp4", origin_files)
		list_of_video_paths.append("newvid" + str(i) + ".mp4")
	# concatenate all trimmed video files.
	merge_video(list_of_video_paths, "edited_video.mp4")


### using ffmpeg

############################## 

if __name__ == '__main__':

	# the algorithm produces margins that are slightly off, so I manually added some for now
	point_timestamps = [[56.403282,63.256324],[118.467133,126.213666]]
	# removed the floats -> kind of removed one pause for the last point
	# "C:/Users/matt2/Desktop/Videos/8-18-18 Tennis/GOPR2267.mp4"
	export_video(point_timestamps, "D:/DCIM/100GOPRO/9-18-18 Driving Range/GOPR2284.mp4")
