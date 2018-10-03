import subprocess

def split_video():
	# cut out 2 clips (fast)
	# subprocess.call("ffmpeg -i sample_video_files/driver_source.mp4 -ss 00:00:01 -to 00:00:02 -c copy sample_video_files/out1.mp4")
	# subprocess.call("ffmpeg -i sample_video_files/driver_source.mp4  -ss 00:00:3 -to 00:00:05 -c copy sample_video_files/out2.mp4")

	# cut out 2 clips (slow)
	subprocess.call("ffmpeg -i sample_video_files/driver_source.mp4 -ss 00:00:00 -to 00:00:01 -async 1 sample_video_files/out1.mp4")

	subprocess.call("ffmpeg -i sample_video_files/driver_source.mp4 -ss 00:00:01 -to 00:00:03 -async 1 sample_video_files/out2.mp4")

def join_video():
	### Concatenate video clips
	# add files to clip_list.txt in chronological order.
	subprocess.call("(echo file 'out2.mp4' & echo file 'out1.mp4' )>sample_video_files/clip_list.txt", shell=True)

	# concatenate all videos in clip_list.txt
	subprocess.call("ffmpeg -safe 0 -f concat -i sample_video_files/clip_list.txt -c copy sample_video_files/output.mp4")

def rotate_clip(source_path, output_path, degrees_cw):
	subprocess.call('ffmpeg -i ' + source_path + ' -filter:v "rotate=' + str(degrees_cw) + '*PI/180" ' + output_path)

def resize_and_translate_clip(source_path, output_path, scale_factor, translate_x, translate_y):

	'''	scale + move the frame around a bit
	syntax: crop=height_of_output:width_of_output:left_border:top_border
	
	derived an equation to find left/top border: (in_w/h-scale_factor)/2
	also added translate_x/y (in pixels): translate_x/y + (in_w/h-scale_factor)/2
		- note: when a 'left_border' or 'right_border' values causes the 
			frame to go 'out of bounds', ffmpeg keeps the frame 'in bounds'
			by restricting any further x or y translation.

	docs: http://ffmpeg.org/ffmpeg-filters.html#crop
	'''
	subprocess.call('ffmpeg -i ' + source_path + ' -vf "crop=in_w*'+str(scale_factor)+':in_h*'+str(scale_factor)+':x=' + str(translate_x) + '+(in_w-in_w*'+str(scale_factor)+')/2:y=' + str(translate_y) + '+(in_h-in_h*'+str(scale_factor)+')/2" ' + output_path)




#rotate_clip("sample_video_files/driver_source.mp4", "sample_video_files/rotated.mp4", 5)
resize_and_translate_clip("sample_video_files/driver_source.mp4", "sample_video_files/scaled2.mp4", 0.3, -20, 150)

# split_video()
# join_video()


'''
timestamps
var timestamps = [[0,0]];


reframe instances

// this format: [[start_time, end_time, zoom, rotation, translate_x, translate_y], [reframe_instance2], [reframe_instance3]];
	var reframe_instances = [[0, null, 1, 0, 0, 0]];//
'''