import subprocess

def split_video(timestamps, source_folder, output_folder):

	# 0. Fix time format.
	# convert int time format in 'timestamps' to 'hh:mm:ss:'
	# for timestamp in timestamps:
	# 	import time
	# 	timestamp[1] = time.strftime('%H:%M:%S', time.gmtime(timestamp[1]))
	# 	timestamp[2] = time.strftime('%H:%M:%S', time.gmtime(timestamp[2]))

	for i in range(len(timestamps)):

		### 1. Assemble the source and output paths.
		source_path = source_folder + str(timestamps[i][0])
		output_path = output_folder + "trimmed"+str(i)+".mp4"
		


		### 2. trim and export the clip 

		# Slow export ('perfect'(?) cuts and playback)
		subprocess.call('ffmpeg -i ' + source_path + ' -ss ' + str(timestamps[i][1]) + ' -to ' + str(timestamps[i][2]) + ' -async 1 ' + output_path)
		
		# Fast export (inaccurate cuts, random jumping) 
		# subprocess.call('ffmpeg -i ' + source_path + ' -ss ' + str(timestamps[i][1]) + ' -to ' + str(timestamps[i][2]) + ' -c copy ' + output_path)



		### 3. "reframe" the clip.

		# Tweak 'reframe' attributes (should we do these calculations from the client side?)
		timestamps[i][3][2] = 1/timestamps[i][3][2]
		timestamps[i][3][4] = -timestamps[i][3][4]/100
		timestamps[i][3][5] = -timestamps[i][3][5]/100
		# reframing involves exporting a new file (differentiated with a '_reframed' suffix)
		reframe_clip(output_path, output_path[:-4]+"_reframed"+output_path[-4:], timestamps[i][3][2], timestamps[i][3][3], timestamps[i][3][4], timestamps[i][3][5])
		video_clip_paths.append(output_path[:-4]+"_reframed"+output_path[-4:])

		# delete the intermediate (pre-reframe) file
		delete_files([output_path])

	return video_clip_paths

def join_video(video_clip_paths):
	### Concatenate video clips

	# add file paths to clip_list.txt in chronological order.
	clip_list_file = open("sample_video_files\\clip_list.txt","w+")
	
	for i in range(len(video_clip_paths)):
		clip_list_file.write("file '" + str(video_clip_paths[i][19:])+"'"+"\n")
		
	clip_list_file.close() # remember to close the file!


	import datetime

	

	# concatenate all videos in clip_list.txt
	subprocess.call('ffmpeg -safe 0 -f concat -i sample_video_files/clip_list.txt -c copy sample_video_files\\output.mp4')
	
	# delete the 'intermediate' files
	delete_files(video_clip_paths)
	delete_files(["sample_video_files\\clip_list.txt"])

def reframe_clip(source_path, output_path, scale_factor, degrees_cw, translate_x, translate_y):

	'''	scale + move the frame around a bit
	syntax: crop=height_of_output:width_of_output:left_border:top_border
	
	derived an equation to find left/top border: (in_w/h-scale_factor)/2
	also added translate_x/y (in pixels): translate_x/y + (in_w/h-scale_factor)/2
		- note: when a 'left_border' or 'right_border' values causes the 
			frame to go 'out of bounds', ffmpeg keeps the frame 'in bounds'
			by restricting any further x or y translation.

	docs: http://ffmpeg.org/ffmpeg-filters.html#crop
	''' 
	# og one that works.
	#subprocess.call('ffmpeg -i ' + source_path + ' -vf "crop=in_w*'+str(scale_factor)+':in_h*'+str(scale_factor)+':x=' + str(translate_x) + '+(in_w-in_w*'+str(scale_factor)+')/2:y=' + str(translate_y) + '+(in_h-in_h*'+str(scale_factor)+')/2, rotate=' + str(degrees_cw) + '*PI/180" ' + output_path)

	# rotate then crop ... then trim (shouldn't it be the other way around - to be more efficient?)
	#subprocess.call('ffmpeg -i ' + source_path + ' -vf "rotate=' + str(degrees_cw) + '*PI/180, crop=in_w*'+str(scale_factor)+':in_h*'+str(scale_factor)+':x=(in_w*' + str(-ref_inst[4]/100) + ')+(in_w-in_w*'+str(scale_factor)+')/2:y=(in_h*' + str(-ref_inst[5]/100) + ')+(in_h-in_h*'+str(scale_factor)+')/2"' + ' -ss ' + timestamps[i][1] + ' -to ' + timestamps[i][2] + ' -async 1 -preset veryfast -crf 23 ' + output_path)
		

	# rotate then crop.
	subprocess.call('ffmpeg -i ' + source_path + ' -vf "rotate=' + str(degrees_cw) + '*PI/180, crop=in_w*'+str(scale_factor)+':in_h*'+str(scale_factor)+':x=(in_w*' + str(translate_x) + ')+(in_w-in_w*'+str(scale_factor)+')/2:y=(in_h*' + str(translate_y) + ')+(in_h-in_h*'+str(scale_factor)+')/2" ' + output_path)
		
def delete_files(list_of_files):
	for file_path in list_of_files:
		print('deleting', file_path)
		subprocess.call('del ' + file_path, shell=True)

if __name__ == '__main__':

	# 1. Gather up the 'timestamps' from the client.
	timestamps = []
	timestamps += [["GP02282.mp4", 127.719732,135.404922],["GP02282.mp4", 211.784388,216.323946],["GP02282.mp4", 336.763287,349.366786],["GP02282.mp4", 407.764612,412.360611],["GP02282.mp4", 471.744653,479.411002]]
	timestamps += [["GP012282.mp4", 5.764312,13.26873],["GP012282.mp4", 180.900563,188.198835],["GP012282.mp4", 225.357598,232.880334],["GP012282.mp4", 279.278609,287.316795],["GP012282.mp4", 361.696992,369.769528],["GP012282.mp4", 415.022046,425.08302],["GP012282.mp4", 468.750865,475.132285],["GP012282.mp4", 487.647566,496.491205],["GP012282.mp4", 510.233005,515.388323],["GP012282.mp4", 524.335805, 532.52]]
	timestamps += [["GP022282.mp4", 0,12.174976],["GP022282.mp4", 45.474425,69.497312],["GP022282.mp4", 482.1359,490.330911]]
	timestamps += [["GP032282.mp4", 242.969949,261.949609]]
	timestamps += [["GP042282.mp4", 48.778993,54.724027],["GP042282.mp4", 466.419216,475.79125],["GP042282.mp4", 485.063597,492.078307],["GP042282.mp4", 503.45959,509.570341]]
	timestamps += [["GP052282.mp4", 133.288234,139.578014],["GP052282.mp4", 371.181167,374.730225],["GP052282.mp4", 394.740634,407.004446],["GP052282.mp4", 515.872244,526.523133]]
	timestamps += ([["GP062282.mp4", 16.503022,46.07626],["GP062282.mp4", 100.401208,114.978135],["GP062282.mp4", 343.551817,364.925568]])

	# [for a temporary project]
	for timestamp in timestamps:
		timestamp.append([0,None,1.950000000000001,-4,-45,15])
	# maybe make a function that consolidates the reframe and timestamps lists.
	# sketch a few diagrams...
		# for timestamp in timestamps
			# if timestamp is in a reframe instance: append the reframe instance.
			# elif timestamp is in between two reframe instances: split the timestamp once more? and repeat.

	# 2. Split the video into clips, then reframe those clips.
	video_clip_paths = [] # in chronological order.
	video_clip_paths = split_video(timestamps, "sample_video_files\\", "sample_video_files\\")

	# 3. Concatenate the clips into one video.
	join_video(video_clip_paths)



	# 10/5/18 - 5:28 - temp: an attempt to make the video export faster.
	# pt_times = [[1, 2], [3, 4], [5, 6]]
	# ffmpeg_command = ''
	# # do a 'filter'.
	# ffmpeg_command += 'ffmpeg -i sample_video_files/GP052282.mp4 -filter_complex "'
	
	# # traverse each pt_time[] here?
	# # for i in range(len(pt_times)):

	# # start trimming.
	# # first iteration of the loop (i=0)
	# # clip 1
	# ffmpeg_command += '[0:v]trim=start='+str(pt_times[0][0])+':end='+str(pt_times[0][1])+',setpts=PTS-STARTPTS[av]; '
	# ffmpeg_command += '[0:a]atrim=start='+str(pt_times[0][0])+':end='+str(pt_times[0][1])+',asetpts=PTS-STARTPTS[aa]; '
	# # clip 2
	# ffmpeg_command += '[0:v]trim=start='+str(pt_times[1][0])+':end='+str(pt_times[1][1])+',setpts=PTS-STARTPTS[bv]; '
	# ffmpeg_command += '[0:a]atrim=start='+str(pt_times[1][0])+':end='+str(pt_times[1][1])+',asetpts=PTS-STARTPTS[ba]; '
	# # concatenate clip 1 and 2.
	# ffmpeg_command += '[av][bv]concat[cv]; ' # video
	# ffmpeg_command += '[aa][ba]concat=v=0:a=1[ca]; ' # audio	


	# # second iteration of the loop (i=1)
	# # clip 3
	# ffmpeg_command += '[0:v]trim=start='+str(pt_times[2][0])+':end='+str(pt_times[2][1])+',setpts=PTS-STARTPTS[dv]; '
	# ffmpeg_command += '[0:a]atrim=start='+str(pt_times[2][0])+':end='+str(pt_times[2][1])+',asetpts=PTS-STARTPTS[da]; '
	# # concatenate 2.
	# ffmpeg_command += '[cv][dv]concat[outputv]; ' # video
	# ffmpeg_command += '[ca][da]concat=v=0:a=1[outputa] ' # audio


	# ffmpeg_command += '" -map [outputv] -map [outputa] sample_video_files/stack_overflow_trim.mp4'
	# subprocess.call(ffmpeg_command)