import subprocess

def split_video(timestamps, source_path, output_path):
	# cut out 2 clips (fast)
	# subprocess.call("ffmpeg -i sample_video_files/driver_source.mp4 -ss 00:00:01 -to 00:00:02 -c copy sample_video_files/out1.mp4")
	# subprocess.call("ffmpeg -i sample_video_files/driver_source.mp4  -ss 00:00:3 -to 00:00:05 -c copy sample_video_files/out2.mp4")

	# convert int time format in 'timestamps' to 'hh:mm:ss:'
	for timestamp in timestamps:
		import time
		timestamp[1] = time.strftime('%H:%M:%S', time.gmtime(timestamp[1]))
		timestamp[2] = time.strftime('%H:%M:%S', time.gmtime(timestamp[2]))

	for i in range(len(timestamps)):
		# trim and export a clip (slow)
		#subprocess.call("ffmpeg -i " + source_path + " -ss " + str(timestamps[i][0]) + " -to " + str(timestamps[i][1]) + " -async 1 " + output_path[:-4]+str(i)+".mp4")
		# fast
		subprocess.call("ffmpeg -i " + source_path + str(timestamps[i][0]) + " -ss " + str(timestamps[i][1]) + " -to " + str(timestamps[i][2]) + " -c copy " + output_path+"trimmed"+str(i)+".mp4")
		video_clip_paths.append(output_path+"trimmed"+str(i)+".mp4")

	return video_clip_paths

def join_video(video_clip_paths):
	### Concatenate video clips

	# add file paths to clip_list.txt in chronological order.
	clip_list_file = open("sample_video_files/clip_list.txt","w+")
	
	for i in range(len(video_clip_paths)):
		clip_list_file.write("file '" + str(video_clip_paths[i][19:])+"'"+"\n")
		
	clip_list_file.close() # remember to close the file!

	# concatenate all videos in clip_list.txt
	subprocess.call("ffmpeg -safe 0 -f concat -i sample_video_files/clip_list.txt -c copy sample_video_files/output.mp4")
	

def reframe_clip(source_path, output_path, scale_factor, translate_x, translate_y, degrees_cw):

	'''	scale + move the frame around a bit
	syntax: crop=height_of_output:width_of_output:left_border:top_border
	
	derived an equation to find left/top border: (in_w/h-scale_factor)/2
	also added translate_x/y (in pixels): translate_x/y + (in_w/h-scale_factor)/2
		- note: when a 'left_border' or 'right_border' values causes the 
			frame to go 'out of bounds', ffmpeg keeps the frame 'in bounds'
			by restricting any further x or y translation.

	docs: http://ffmpeg.org/ffmpeg-filters.html#crop
	'''
	subprocess.call('ffmpeg -i ' + source_path + ' -vf "crop=in_w*'+str(scale_factor)+':in_h*'+str(scale_factor)+':x=' + str(translate_x) + '+(in_w-in_w*'+str(scale_factor)+')/2:y=' + str(translate_y) + '+(in_h-in_h*'+str(scale_factor)+')/2, rotate=' + str(degrees_cw) + '*PI/180" ' + output_path)





timestamps = []
timestamps += [["GP02282.mp4", 127.719732,135.404922],["GP02282.mp4", 211.784388,216.323946],["GP02282.mp4", 336.763287,349.366786],["GP02282.mp4", 407.764612,412.360611],["GP02282.mp4", 471.744653,479.411002]]



timestamps += [["GP012282.mp4", 5.764312,13.26873],["GP012282.mp4", 180.900563,188.198835],["GP012282.mp4", 225.357598,232.880334],["GP012282.mp4", 279.278609,287.316795],["GP012282.mp4", 361.696992,369.769528],["GP012282.mp4", 415.022046,425.08302],["GP012282.mp4", 468.750865,475.132285],["GP012282.mp4", 487.647566,496.491205],["GP012282.mp4", 510.233005,515.388323],["GP012282.mp4", 524.335805, 532.52]]

timestamps += [["GP022282.mp4", 0,12.174976],["GP022282.mp4", 45.474425,69.497312],["GP022282.mp4", 482.1359,490.330911]]

timestamps += [["GP032282.mp4", 242.969949,261.949609]]

timestamps += [["GP042282.mp4", 48.778993,54.724027],["GP042282.mp4", 466.419216,475.79125],["GP042282.mp4", 485.063597,492.078307],["GP042282.mp4", 503.45959,509.570341]]

timestamps += [["GP052282.mp4", 133.288234,139.578014],["GP052282.mp4", 371.181167,374.730225],["GP052282.mp4", 394.740634,407.004446],["GP052282.mp4", 515.872244,526.523133]]

timestamps += ([["GP062282.mp4", 16.503022,46.07626],["GP062282.mp4", 100.401208,114.978135],["GP062282.mp4", 343.551817,364.925568]])



# video_clip_paths will be in chronological order.
video_clip_paths = []
video_clip_paths = split_video(timestamps, "sample_video_files/", "sample_video_files/")

#reframe_clip("sample_video_files/driver_source.mp4", "sample_video_files/scaled2.mp4", 0.5, -20, 150, 5)

join_video(video_clip_paths)







'''
timestamps
var timestamps = [[0,0]];


reframe instances

// this format: [[start_time, end_time, zoom, rotation, translate_x, translate_y], [reframe_instance2], [reframe_instance3]];
	var reframe_instances = [[0, null, 1, 0, 0, 0]];//
'''