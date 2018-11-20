import json
import video_export
import video_export_no_reframe

########## 10/25/18
#stringified_array = '[{"filename":"GOPR2331.MP4","start_time":77.046674,"end_time":92.702836,"trim_complete":true,"scale_factor":1.9500000000000008,"degrees_cw":1.5,"translate_x":295,"translate_y":0},{"filename":"GOPR2331.MP4","start_time":183.183415,"end_time":185.866399,"trim_complete":true,"scale_factor":1.9500000000000008,"degrees_cw":1.5,"translate_x":295,"translate_y":0},{"filename":"GP012331.MP4","start_time":435.153243,"end_time":440.275001,"trim_complete":true,"scale_factor":2.000000000000001,"degrees_cw":1.5,"translate_x":270,"translate_y":0},{"filename":"GP022331.MP4","start_time":142.793787,"end_time":163.843519,"trim_complete":true,"scale_factor":1.9500000000000008,"degrees_cw":1.5,"translate_x":295,"translate_y":0},{"filename":"GP022331.MP4","start_time":177.272604,"end_time":183.498521,"trim_complete":true,"scale_factor":1.9500000000000008,"degrees_cw":1.5,"translate_x":295,"translate_y":0},{"filename":"GP022331.MP4","start_time":245.449689,"end_time":257.55096,"trim_complete":true,"scale_factor":1.9500000000000008,"degrees_cw":1.5,"translate_x":295,"translate_y":0},{"filename":"GP022331.MP4","start_time":368.195745,"end_time":379.271995,"trim_complete":true,"scale_factor":1.9500000000000008,"degrees_cw":1.5,"translate_x":295,"translate_y":0}]'

########## streetsville
# part 1
#stringified_array = '[{"filename":"GOPR2295.MP4","start_time":147.26991,"end_time":151.571239,"trim_complete":true,"scale_factor":1.3000000000000003,"degrees_cw":0,"translate_x":-10,"translate_y":30},{"filename":"GOPR2295.MP4","start_time":191.082617,"end_time":195.025877,"trim_complete":true,"scale_factor":1.3000000000000003,"degrees_cw":0,"translate_x":-10,"translate_y":30},{"filename":"GOPR2295.MP4","start_time":231.648278,"end_time":235.004628,"trim_complete":true,"scale_factor":1.3000000000000003,"degrees_cw":0,"translate_x":-10,"translate_y":30},{"filename":"GOPR2295.MP4","start_time":327.453251,"end_time":331.860195,"trim_complete":true,"scale_factor":1.7500000000000007,"degrees_cw":0,"translate_x":0,"translate_y":70},{"filename":"GOPR2295.MP4","start_time":485.903017,"end_time":492.196396,"trim_complete":true,"scale_factor":1,"degrees_cw":0,"translate_x":0,"translate_y":0},{"filename":"GOPR2295.MP4","start_time":518.417833,"end_time":522.836021,"trim_complete":true,"scale_factor":2.25,"degrees_cw":0,"translate_x":0,"translate_y":75},{"filename":"GP012295.MP4","start_time":8.002138,"end_time":13.430266,"trim_complete":true,"scale_factor":2.799999999999998,"degrees_cw":0,"translate_x":0,"translate_y":100},{"filename":"GP012295.MP4","start_time":26.37621,"end_time":31.774662,"trim_complete":true,"scale_factor":2.799999999999998,"degrees_cw":0,"translate_x":0,"translate_y":100},{"filename":"GP012295.MP4","start_time":46.595955,"end_time":50.883776,"trim_complete":true,"scale_factor":2.799999999999998,"degrees_cw":0,"translate_x":0,"translate_y":100},{"filename":"GOPR2296.MP4","start_time":60.409566,"end_time":66.925772,"trim_complete":true,"scale_factor":1.2500000000000002,"degrees_cw":0,"translate_x":-90,"translate_y":50},{"filename":"GOPR2296.MP4","start_time":94.672897,"end_time":100.058973,"trim_complete":true,"scale_factor":2.1000000000000005,"degrees_cw":0,"translate_x":-90,"translate_y":70},{"filename":"GOPR2296.MP4","start_time":162.230581,"end_time":166.927318,"trim_complete":true,"scale_factor":1.8000000000000007,"degrees_cw":0,"translate_x":-75,"translate_y":65},{"filename":"GOPR2296.MP4","start_time":321.894106,"end_time":325.577808,"trim_complete":true,"scale_factor":1.5500000000000005,"degrees_cw":18.5,"translate_x":-75,"translate_y":10},{"filename":"GOPR2296.MP4","start_time":499.277368,"end_time":503.519922,"trim_complete":true,"scale_factor":3.7999999999999945,"degrees_cw":-5,"translate_x":0,"translate_y":35},{"filename":"GP012296.MP4","start_time":4.07687,"end_time":12.929501,"trim_complete":true,"scale_factor":4.299999999999993,"degrees_cw":-5,"translate_x":0,"translate_y":70},{"filename":"GP012296.MP4","start_time":28.564089,"end_time":35.174814,"trim_complete":true,"scale_factor":4.299999999999993,"degrees_cw":-5,"translate_x":0,"translate_y":70},{"filename":"GP012296.MP4","start_time":46.989309,"end_time":51.316524,"trim_complete":true,"scale_factor":4.299999999999993,"degrees_cw":-5,"translate_x":0,"translate_y":70},{"filename":"GP012296.MP4","start_time":174.631866,"end_time":181.283562,"trim_complete":true,"scale_factor":2.499999999999999,"degrees_cw":-4,"translate_x":-40,"translate_y":35},{"filename":"GP012296.MP4","start_time":213.217851,"end_time":218.03822,"trim_complete":true,"scale_factor":2.499999999999999,"degrees_cw":-4,"translate_x":-40,"translate_y":35},{"filename":"GP012296.MP4","start_time":253.481027,"end_time":258.111059,"trim_complete":true,"scale_factor":2.499999999999999,"degrees_cw":-4,"translate_x":-40,"translate_y":35},{"filename":"GP012296.MP4","start_time":420.013703,"end_time":426.707158,"trim_complete":true,"scale_factor":1.8000000000000007,"degrees_cw":0,"translate_x":-15,"translate_y":20},{"filename":"GP012296.MP4","start_time":461.033368,"end_time":465.277007,"trim_complete":true,"scale_factor":2.6999999999999984,"degrees_cw":5,"translate_x":-85,"translate_y":20},{"filename":"GP012296.MP4","start_time":480.632583,"end_time":490.044156,"trim_complete":true,"scale_factor":2.6999999999999984,"degrees_cw":5,"translate_x":-85,"translate_y":20},{"filename":"GP012296.MP4","start_time":498.144816,"end_time":501.322529,"trim_complete":true,"scale_factor":2.6999999999999984,"degrees_cw":5,"translate_x":-85,"translate_y":20},{"filename":"GOPR2297.MP4","start_time":24.357485,"end_time":29.425846,"trim_complete":true,"scale_factor":1.9000000000000008,"degrees_cw":-2,"translate_x":-35,"translate_y":65},{"filename":"GOPR2297.MP4","start_time":63.030202,"end_time":68.24121,"trim_complete":true,"scale_factor":1.9000000000000008,"degrees_cw":-2,"translate_x":-35,"translate_y":65},{"filename":"GOPR2297.MP4","start_time":97.022586,"end_time":100.942384,"trim_complete":true,"scale_factor":1.9000000000000008,"degrees_cw":-2,"translate_x":-35,"translate_y":50},{"filename":"GOPR2298.MP4","start_time":31.709626,"end_time":36.921192,"trim_complete":true,"scale_factor":1,"degrees_cw":0,"translate_x":0,"translate_y":0},{"filename":"GOPR2298.MP4","start_time":66.170793,"end_time":72.152462,"trim_complete":true,"scale_factor":1,"degrees_cw":0,"translate_x":0,"translate_y":0},{"filename":"GOPR2299.MP4","start_time":74.132966,"end_time":79.981565,"trim_complete":true,"scale_factor":1.1500000000000001,"degrees_cw":-1,"translate_x":-25,"translate_y":0},{"filename":"GOPR2299.MP4","start_time":116.713893,"end_time":129.566697,"trim_complete":true,"scale_factor":1.5000000000000004,"degrees_cw":0,"translate_x":-180,"translate_y":0}]'


# part 2
stringified_array = '[{"filename":"user_input.mp4","start_time":52.692843,"end_time":53.441332,"trim_complete":true,"scale_factor":1.4000000000000004,"degrees_cw":3.5,"translate_x":-80,"translate_y":-15}]'

# convert the stringified list into an actual list
stringified_list = json.loads(stringified_array)

# save the clips in a list of dicts
video_clips = []

for stringified_dict in stringified_list:
	video_clips.append(stringified_dict)


#####

print('exporting video...')

# process the video...
# normally or ..
video_export.export(video_clips)
# .. quickly (no reframe)
# video_export_no_reframe.export(video_clips)

print('finished export.')


# an example of 'borderfill'
# ffmpeg -i sample_video_files/output.mp4 -vf "fillborders=right=100:top=100:bottom=100:mode='mirror'" sample_video_files/ootpoot.mp4

# # trying to double the output frame size
# ffmpeg -i sample_video_files/og_frame.mp4 -filter:v "crop=w=in_w:h=in_h:x=0:y=0" sample_video_files/ootpoot.mp4

# # trying 'exact'
# ffmpeg -i sample_video_files/og_frame.mp4 -filter:v "crop=w=in_w/2:h=in_h/2:x=10000:y=16000:exact=1" sample_video_files/output.mp4


# # using 'overlay' move horizontally by 500px
# ffmpeg -i sample_video_files/og_frame.mp4 -filter_complex "[0:v][0:v]overlay=500:0[bg]; [bg][0:v]overlay=500-W,format=yuv420p[out]" -map "[out]" -map 0:a -codec:v libx264 -crf 23 -preset medium -c:a copy sample_video_files/ootpoot.mp4

# # a shorter version of the horizontal shift
# ffmpeg -i sample_video_files/og_frame.mp4 -filter_complex "[0:v][0:v]overlay=x=4100:0[bg]; [bg][0:v]overlay=x=4100-W,format=yuv420p[out]" -map "[out]" -map 0:a sample_video_files/ootpoot.mp4

# # a vertical shift
# ffmpeg -i sample_video_files/og_frame.mp4 -filter_complex "[0:v][0:v]overlay=x=4100:1000[bg]; [bg][0:v]overlay=x=4100-W:y=1000,format=yuv420p[out]" -map "[out]" -map 0:a sample_video_files/ootpoot.mp4

# # so far: black background (not the og frame!)
# ffmpeg -i sample_video_files/og_frame.mp4 -i sample_video_files/full_match.MP4 -filter_complex "[1:v][0:v]overlay=x=0:0[bg]; [bg][0:v]overlay=x=410-W:y=500,format=yuv420p[out]" -map "[out]" -map 0:a sample_video_files/ootpoot.mp4

# # so far: overlay video on an image

# ffmpeg -loop 1 -i background.jpg \
#        -vf "movie=overlay.mp4,scale=128:96[inner];[in][inner]overlay=70:70:shortest=1[out]" \
#        -y output.mp4