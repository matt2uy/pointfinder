import subprocess

def split_video(timestamps, source_folder, output_folder): # add parameter: speed? quality?

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
	
	brightness = 0.04 # from -1.0 to 1.0 (default = 0)

	# rotate then crop.
	subprocess.call('ffmpeg -i ' + source_path + ' -vf "eq=brightness=' + str(brightness) + ', rotate=' + str(degrees_cw) + '*PI/180, crop=in_w*'+str(scale_factor)+':in_h*'+str(scale_factor)+':x=(in_w*' + str(translate_x) + ')+(in_w-in_w*'+str(scale_factor)+')/2:y=(in_h*' + str(translate_y) + ')+(in_h-in_h*'+str(scale_factor)+')/2" ' + output_path)
		
def delete_files(list_of_files):
	for file_path in list_of_files:
		print('deleting', file_path)
		subprocess.call('del ' + file_path, shell=True)

if __name__ == '__main__':

	# 1. Gather up the 'timestamps' from the client.
	timestamps = []



	#edit 1....#####################################


	# 10/12/18
	# Video frame settings: [[0,80.953419,1,0,0,0],[80.953419,83.288432,1.05,0,0,0],[83.288432,84.189093,1.8000000000000007,-5,-40,10],[84.189093,null,1.8500000000000008,-5,-40,10]]
	temp_segment1 = [["GOPR2326.mp4", 161.466227,175.511756],["GOPR2326.mp4", 193.481382,207.849141],["GOPR2326.mp4", 388.835685,406.281275],["GOPR2326.mp4", 425.615758,434.036654]]
	for timestamp in temp_segment1:
		timestamp.append([84.189093,0,1.8500000000000008,-5,-40,10])

	timestamps += temp_segment1


	# Video frame settings: [[0,104.223804,1,0,0,0],[104.223804,105.447595,1,-0.5,0,0],[105.447595,106.181362,1.8500000000000008,-9.5,-36,9],[106.181362,null,1.8000000000000007,-9.5,-36,9]]
	temp_segment2 = [["GP012326.mp4", 104.223804,108.718032],["GP012326.mp4", 435.093209,449.006654],["GP012326.mp4", 460.02222,470.617283]]
	for timestamp in temp_segment2:
		timestamp.append([106.181362,0,1.8000000000000007,-9.5,-36,9])

	timestamps += temp_segment2




	#edit 2#####################################

	# # 9/30/18 2.5mins

	# Start Points: [[0,0],[240.053048,252.237701],[259.771077,266.388262],[474.93429,481.632931]]
	# Video frame settings: [[0,240.053048,1,0,0,0],[240.053048,null,1.05,0,0,0]]

	#edit 3 ###################################
	#GOPR2330.mp4
	 [[47.26088,56.227589],[72.620567,82.634407],[211.488545,217.786116],[232.219151,238.497642],[273.794221,277.134785],[297.344729,302.66336],[317.197952,321.425013],[370.669293,378.863889],[455.485985,464.237035],[482.259749,493.568311]]
Video frame settings: [0,0,1.4000000000000004,-4.5,-21,0]
Can play type "video/mp4": maybe1

GP012330.mp4
[[0,0],[14.205457,26.219543],[66.701287,75.374617],[196.80708,203.183831]]
Video frame settings: 

GP022330.mp4
: [[0,0],[88.300326,91.725963],[120.131193,124.568342],[134.932153,142.509433]]
Video frame settings: [[0,2.540332,1,0,0,0],[2.540332,386.485838,1.05,0,0,0],[386.485838,388.377343,1.4500000000000004,-6,-20,14],[388.377343,390.956158,1.4500000000000004,-6,-20,21],[390.956158,null,1.4500000000000004,-6,-20,20]]
Can play type "video/mp4": maybe1

GP032330.mp4
 [[0,0],[12.740137,19.324157],[97.563118,107.437755],[236.319476,242.880827],[439.031037,453.26413]]


 GP042330.mp4
 [[0,0],[223.898429,232.019371],[405.799101,427.277771]]


 GP062330.mp4
 [[0,0],[240.294115,257.975342],[317.270735,339.975056],[361.382775,364.545566],[412.530853,425.325298],[453.823032,460.103991]]


 GP072330.mp4 lol
 [[0,0],[240.294115,257.975342],[317.270735,339.975056],[361.382775,364.545566],[412.530853,425.325298],[453.823032,460.103991]]


 GP082330.mp4



 GP092330.mp4



 GP022330.mp4
	'''
	# maybe make a function that consolidates the reframe and timestamps lists.
	# sketch a few diagrams...
	for timestamp in timestamps
		for reframe_instance in reframe_instances:
			# ensure that the file is correct (try another way to do this as well)
			if timestamp[0] == reframe_instance[0]: # note: reframe_instance[0] = file path
				# if timestamp is in a reframe instance: append the reframe instance to the timestamp.
				if timestamp[1] > reframe_instance[1] and timestamp[2] < reframe_instance[2]:
					timestamp.append(reframe_instance)

				# elif timestamp is in between two reframe instances: split the timestamp once more? and repeat.
				elif timestamp[1] > reframe_instance[1] and timestamp[2] > reframe_instance[2]:
					# split up the timestamp?
					timestamp.append(reframe_instance)
				elif timestamp[1] < reframe_instance[1] and timestamp[2] < reframe_instance[2]:
					# split up the timestamp?
					timestamp.append(reframe_instance)
	'''

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