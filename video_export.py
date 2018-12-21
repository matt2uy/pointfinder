import subprocess

def split_video(video_clips, source_folder, output_folder): # add parameter: speed? quality?

	# 0. Fix time format.
	# convert int time format in 'timestamps' to 'hh:mm:ss:'
	# for timestamp in timestamps:
	# 	import time
	# 	timestamp[1] = time.strftime('%H:%M:%S', time.gmtime(timestamp[1]))
	# 	timestamp[2] = time.strftime('%H:%M:%S', time.gmtime(timestamp[2]))
	video_clip_paths = []
	for i in range(len(video_clips)):

		### 1. Assemble the source and output paths.
		source_path = source_folder + str(video_clips[i]["filename"])
		output_path = output_folder + "trimmed"+str(i)+".mp4"
		


		### 2. trim and export the clip 

		# Slow export ('perfect'(?) cuts and playback)
		subprocess.call('ffmpeg -i ' + source_path + ' -ss ' + str(video_clips[i]["start_time"]) + ' -to ' + str(video_clips[i]["end_time"]) + ' -async 1 ' + output_path)
		
		# Fast export (inaccurate cuts, random jumping) 
		#subprocess.call('ffmpeg -i ' + source_path + ' -ss ' + str(video_clips[i]["start_time"]) + ' -to ' + str(video_clips[i]["end_time"]) + ' -c copy ' + output_path)



		### 3. "reframe" the clip.
		# Tweak 'reframe' attributes (should we do these calculations from the client side?)
		video_clips[i]["scale_factor"] = 1/video_clips[i]["scale_factor"]
		#video_clips[i]["degrees_cw"] = -video_clips[i]["degrees_cw"]/100
		video_clips[i]["translate_y"] = -video_clips[i]["translate_y"]
		video_clips[i]["translate_x"] = -video_clips[i]["translate_x"]
		# reframing involves exporting a new file (differentiated with a '_reframed' suffix)
		print("\n\n\n\n\n"+"translate_x"+str(video_clips[i]["translate_x"])+"\n translate_y"+str(video_clips[i]["translate_y"])+"\n\n\n\n\n")
		reframe_clip(output_path, output_path[:-4]+"_reframed"+output_path[-4:], video_clips[i]["scale_factor"]*1.1, video_clips[i]["degrees_cw"], video_clips[i]["translate_x"]+20, video_clips[i]["translate_y"]+20)
		
		video_clip_paths.append(output_path[:-4]+"_reframed"+output_path[-4:])

		# delete the intermediate (pre-reframe) file
		delete_files([output_path])

	return video_clip_paths

def join_video(video_clip_paths):
	### Concatenate video clips

	# add file paths to clip_list.txt in chronological order.
	clip_list_file = open("sample_video_files\\clip_list.txt","w+")

	print("\n\n\n\n\n joining "+str(video_clip_paths)+"\n\n\n\n\n")
	
	for i in range(len(video_clip_paths)):
		clip_list_file.write("file '" + str(video_clip_paths[i][19:])+"'"+"\n")
		
	clip_list_file.close() # remember to close the file!


	import datetime
	output_name = "out"+str(datetime.datetime.now().strftime("%m-%d-%y[%H-%M-%S]"))+".mp4"
	

	# concatenate all videos in clip_list.txt
	subprocess.call('ffmpeg -safe 0 -f concat -i sample_video_files/clip_list.txt -c copy sample_video_files\\'+output_name)
	
	''' for copy and pasters (instructions for cmd interface):
	ffmpeg -safe 0 -f concat -i sample_video_files/clip_list.txt -c copy sample_video_files/ooot.mp4
	clip_list.txt:
	file 'filename.mp4'
	'''

	# for testing the reframes!
	#subprocess.call('ffplay sample_video_files/output.mp4')
	# delete the 'intermediate' files
	#delete_files(video_clip_paths)
	#delete_files(["sample_video_files\\clip_list.txt"])

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

	# old, buggy crop.
	#subprocess.call('ffmpeg -i ' + source_path + ' -vf "eq=brightness=' + str(brightness) + ', rotate=' + str(degrees_cw) + '*PI/180, crop=in_w*'+str(scale_factor)+':in_h*'+str(scale_factor)+':x=(in_w*' + str(translate_x) + ')+(in_w-in_w*'+str(scale_factor)+')/2:y=(in_h*' + str(translate_y) + ')+(in_h-in_h*'+str(scale_factor)+')/2" ' + output_path)
	# new, maybe working crop (%).
	#print("\n\n\n\n\n\n\n using the new crop ---------------------- \n\n\n\n\n\n\n\n")
	#subprocess.call('ffmpeg -i ' + source_path + ' -vf "eq=brightness=' + str(brightness) + ', rotate=' + str(degrees_cw) + '*PI/180, crop=in_w*'+str(scale_factor)+':in_h*'+str(scale_factor)+':x=(in_w-out_w)/2+(in_w*('+str(translate_x)+'/100)):y=(in_h-out_h)/2+(in_h*('+str(translate_y)+'/100))" ' + output_path)
	# newer, maybe working crop (px).
	print("\n\n\n\n\n\n\n using the new crop ---------------------- \n\n\n\n\n\n\n\n")
	#subprocess.call('ffmpeg -i ' + source_path + ' -vf "eq=brightness=' + str(brightness) + ', rotate=' + str(degrees_cw) + '*PI/180, crop=exact=1:in_w*'+str(scale_factor)+':in_h*'+str(scale_factor)+':x=(in_w-out_w)/2+(in_w*('+str(translate_x)+')):y=(in_h-out_h)/2+(in_h*('+str(translate_y)+'))" ' + output_path)
	# a bug with the above line
	subprocess.call('ffmpeg -i ' + source_path + ' -vf "eq=brightness=' + str(brightness) + ', rotate=' + str(degrees_cw) + '*PI/180, crop=in_w*'+str(scale_factor)+':in_h*'+str(scale_factor)+':x=(in_w-out_w)/2+(in_w*('+str(translate_x)+')):y=(in_h-out_h)/2+(in_h*('+str(translate_y)+'))" ' + output_path)


	'''
	draw a line: ffmpeg -i test_video.mp4 -vf "[in]drawtext=fontsize=20:fontcolor=White:fontfile='/Windows/Fonts/arial.ttf':text='onLine1':x=(w)/2:y=(h)/2, drawtext=fontsize=20:fontcolor=White:fontfile='/Windows/Fonts/arial.ttf':text='onLine2':x=(w)/2:y=((h)/2)+25, drawtext=fontsize=20:fontcolor=White:fontfile='/Windows/Fonts/arial.ttf':text='onLine3':x=(w)/2:y=((h)/2)+50[out]" -y draw.mp4
	empty crop: ffmpeg -i test_video.mp4 -vf "crop=in_w:in_h:0:0" output.mp4
	trim: ffmpeg -i test_video.mp4 -ss 1 -to 3 -async 1 output.mp4

	50_percent_centered_zoom: ffmpeg -i test_video.mp4 -vf "crop=in_w*0.5:in_h*0.5:(in_w-out_w)/2:(in_h-out_h)/2" 50_percent_centered_zoom.mp4
	10_zoom_10_down: ffmpeg -i test_video.mp4 -vf "crop=in_w*0.5:in_h*0.5:(in_w-out_w)/2:(in_h-out_h)/2+(in_h*(10/100))" 50_zoom_10_down2.mp4
	10_zoom_10_down: ffmpeg -i test_video.mp4 -vf "crop=in_w*0.5:in_h*0.5:(in_w-out_w)/2+(in_w*(10/100)):(in_h-out_h)/2+(in_h*(10/100))" 50_zoom_10_down_10_right.mp4

	x=(in_w*' + str(translate_x) + ')+(in_w-in_w*'+str(scale_factor)+')/2
	:
	y=(in_h*10)+(in_h-in_h*0.9)/2
	'''


		
def delete_files(list_of_files):
	for file_path in list_of_files:
		print('deleting', file_path)
		subprocess.call('del ' + file_path, shell=True)

def export(video_clips):

	#edit 1....#####################################
#################

	# # 10/12/18
	# # Video frame settings: [[0,80.953419,1,0,0,0],[80.953419,83.288432,1.05,0,0,0],[83.288432,84.189093,1.8000000000000007,-5,-40,10],[84.189093,null,1.8500000000000008,-5,-40,10]]
	# temp_segment1 = [["GOPR2326.mp4", 161.466227,175.511756],["GOPR2326.mp4", 193.481382,207.849141],["GOPR2326.mp4", 388.835685,406.281275],["GOPR2326.mp4", 425.615758,434.036654]]
	# for timestamp in temp_segment1:
	# 	timestamp.append([84.189093,0,1.8500000000000008,-5,-40,10])

	# timestamps += temp_segment1


	# # Video frame settings: [[0,104.223804,1,0,0,0],[104.223804,105.447595,1,-0.5,0,0],[105.447595,106.181362,1.8500000000000008,-9.5,-36,9],[106.181362,null,1.8000000000000007,-9.5,-36,9]]
	# temp_segment2 = [["GP012326.mp4", 104.223804,108.718032],["GP012326.mp4", 435.093209,449.006654],["GP012326.mp4", 460.02222,470.617283]]
	# for timestamp in temp_segment2:
	# 	timestamp.append([106.181362,0,1.8000000000000007,-9.5,-36,9])

	# timestamps += temp_segment2

#####################

	# 2. Split the video into clips, then reframe those clips.
	video_clip_paths = [] # in chronological order.
	video_clip_paths = split_video(video_clips, "sample_video_files\\", "sample_video_files\\")

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