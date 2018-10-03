import subprocess

'''
Some ffmpeg commands:
(.mp4 to .avi)
ffmpeg -i quality_tester.mp4 -crf 23 quality_23.avi
- maybe use -crf for .mp4 files?

(filters)
- crop: ffmpeg -i in.mp4 -filter:v "crop=w=640:h=480:x=100:y=200" out.mp4
	w=width, h=height, x and y are the upper left corner (optional)
	variable use: w=2/3*in_w, h=2/3*in_h

(scale)
  syntax: ffmpeg -i in.mp4 -filter:v "scale=w=640:h=480" out.mp4
  arithmetic/variables: ffmpeg -i in.mp4 -filter:v "scale=w=2/3*in_w:h=2/3*in_h" out.mp4
  proportional: ffmpeg -i in.mp4 -filter:v "scale=w=in_w:h=-1" out.mp4

(rotate) ffmpeg -i in.mp4 -filter:v "rotate=45*PI/180" out.mp4

(trim) and make a copy: (newer answer) https://stackoverflow.com/questions/18444194/cutting-the-videos-based-on-start-and-end-time-using-ffmpeg
ffmpeg -i in.mp4 -ss 00:00:53 -to 00:01:03 -c copy out.mp4

(concatenate)
- try out step 2: https://stackoverflow.com/questions/7333232/how-to-concatenate-two-mp4-files-using-ffmpeg

'''

### Create video clips:
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

