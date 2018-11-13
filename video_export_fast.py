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

		video_clip_paths.append(output_path)


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

	

	# concatenate all videos in clip_list.txt
	subprocess.call('ffmpeg -safe 0 -f concat -i sample_video_files/clip_list.txt -c copy sample_video_files\\output.mp4')
	
	# delete the 'intermediate' files
	#delete_files(video_clip_paths)
	#delete_files(["sample_video_files\\clip_list.txt"])

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