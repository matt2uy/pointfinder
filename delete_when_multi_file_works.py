import json
import video_export
import video_export_no_reframe

########## 10/25/18
#stringified_array = '[{"filename":"GOPR2331.MP4","start_time":77.046674,"end_time":92.702836,"trim_complete":true,"scale_factor":1.9500000000000008,"degrees_cw":1.5,"translate_x":295,"translate_y":0},{"filename":"GOPR2331.MP4","start_time":183.183415,"end_time":185.866399,"trim_complete":true,"scale_factor":1.9500000000000008,"degrees_cw":1.5,"translate_x":295,"translate_y":0},{"filename":"GP012331.MP4","start_time":435.153243,"end_time":440.275001,"trim_complete":true,"scale_factor":2.000000000000001,"degrees_cw":1.5,"translate_x":270,"translate_y":0},{"filename":"GP022331.MP4","start_time":142.793787,"end_time":163.843519,"trim_complete":true,"scale_factor":1.9500000000000008,"degrees_cw":1.5,"translate_x":295,"translate_y":0},{"filename":"GP022331.MP4","start_time":177.272604,"end_time":183.498521,"trim_complete":true,"scale_factor":1.9500000000000008,"degrees_cw":1.5,"translate_x":295,"translate_y":0},{"filename":"GP022331.MP4","start_time":245.449689,"end_time":257.55096,"trim_complete":true,"scale_factor":1.9500000000000008,"degrees_cw":1.5,"translate_x":295,"translate_y":0},{"filename":"GP022331.MP4","start_time":368.195745,"end_time":379.271995,"trim_complete":true,"scale_factor":1.9500000000000008,"degrees_cw":1.5,"translate_x":295,"translate_y":0}]'

####### 11/24/18 Tennis

#stringified_array = '[{"filename":"output.mp4","start_time":430.345698,"end_time":452.051524,"trim_complete":true,"scale_factor":1.2000000000000002,"degrees_cw":0.5,"translate_x":20,"translate_y":15},{"filename":"output.mp4","start_time":479.852208,"end_time":493.752535,"trim_complete":true,"scale_factor":1.2000000000000002,"degrees_cw":0.5,"translate_x":20,"translate_y":15},{"filename":"output.mp4","start_time":511.099193,"end_time":522.556426,"trim_complete":true,"scale_factor":1.2000000000000002,"degrees_cw":0.5,"translate_x":20,"translate_y":15},{"filename":"output.mp4","start_time":559.245609,"end_time":567.697206,"trim_complete":true,"scale_factor":1.2000000000000002,"degrees_cw":0.5,"translate_x":20,"translate_y":15},{"filename":"output.mp4","start_time":706.27513,"end_time":714.678994,"trim_complete":true,"scale_factor":1.2000000000000002,"degrees_cw":0.5,"translate_x":20,"translate_y":15},{"filename":"output.mp4","start_time":836.761651,"end_time":847.300217,"trim_complete":true,"scale_factor":1.2000000000000002,"degrees_cw":0.5,"translate_x":20,"translate_y":15},{"filename":"output.mp4","start_time":902.054947,"end_time":905.125213,"trim_complete":true,"scale_factor":1.2000000000000002,"degrees_cw":0.5,"translate_x":20,"translate_y":15},{"filename":"output.mp4","start_time":1060.676243,"end_time":1068.944946,"trim_complete":true,"scale_factor":1.2000000000000002,"degrees_cw":0.5,"translate_x":20,"translate_y":15},{"filename":"output.mp4","start_time":1134.762563,"end_time":1150.153324,"trim_complete":true,"scale_factor":1.2000000000000002,"degrees_cw":0.5,"translate_x":20,"translate_y":15},{"filename":"output.mp4","start_time":1170.526069,"end_time":1179.342277,"trim_complete":true,"scale_factor":1.2000000000000002,"degrees_cw":0.5,"translate_x":20,"translate_y":15},{"filename":"output.mp4","start_time":1209.712047,"end_time":1214.690108,"trim_complete":true,"scale_factor":1.2000000000000002,"degrees_cw":3.5,"translate_x":-85,"translate_y":-30},{"filename":"output.mp4","start_time":1261.475159,"end_time":1267.526318,"trim_complete":true,"scale_factor":1.2000000000000002,"degrees_cw":3.5,"translate_x":-85,"translate_y":-30},{"filename":"output.mp4","start_time":1284.039089,"end_time":1292.911533,"trim_complete":true,"scale_factor":1.2000000000000002,"degrees_cw":3.5,"translate_x":-85,"translate_y":-30},{"filename":"output.mp4","start_time":1367.520975,"end_time":1379.102284,"trim_complete":true,"scale_factor":1.2000000000000002,"degrees_cw":3.5,"translate_x":-85,"translate_y":-10},{"filename":"output.mp4","start_time":1579.109713,"end_time":1595.929933,"trim_complete":true,"scale_factor":1.2000000000000002,"degrees_cw":3.5,"translate_x":-85,"translate_y":-10},{"filename":"output.mp4","start_time":1780.557587,"end_time":1783.493072,"trim_complete":true,"scale_factor":1.2000000000000002,"degrees_cw":3.5,"translate_x":-85,"translate_y":-10},{"filename":"output.mp4","start_time":1798.716475,"end_time":1802.177016,"trim_complete":true,"scale_factor":1.2000000000000002,"degrees_cw":3.5,"translate_x":-85,"translate_y":-10},{"filename":"output.mp4","start_time":1864.910729,"end_time":1880.471309,"trim_complete":true,"scale_factor":1.2000000000000002,"degrees_cw":3.5,"translate_x":-85,"translate_y":-10},{"filename":"output.mp4","start_time":1951.834718,"end_time":1965.415983,"trim_complete":true,"scale_factor":1.2000000000000002,"degrees_cw":3.5,"translate_x":-85,"translate_y":-10},{"filename":"output.mp4","start_time":2060.097897,"end_time":2088.736477,"trim_complete":true,"scale_factor":1.2000000000000002,"degrees_cw":3.5,"translate_x":-85,"translate_y":-10},{"filename":"output.mp4","start_time":2172.870897,"end_time":2177.461825,"trim_complete":true,"scale_factor":1.2000000000000002,"degrees_cw":3.5,"translate_x":-85,"translate_y":-10},{"filename":"output.mp4","start_time":2199.025931,"end_time":2205.650206,"trim_complete":true,"scale_factor":1.2000000000000002,"degrees_cw":3.5,"translate_x":-85,"translate_y":-10},{"filename":"output.mp4","start_time":2217.891859,"end_time":2228.166597,"trim_complete":true,"scale_factor":1.2000000000000002,"degrees_cw":3.5,"translate_x":-85,"translate_y":-10},{"filename":"output.mp4","start_time":2284.314153,"end_time":2307.10436,"trim_complete":true,"scale_factor":1.2000000000000002,"degrees_cw":3.5,"translate_x":-85,"translate_y":-10},{"filename":"output.mp4","start_time":2348.457754,"end_time":2372.58186,"trim_complete":true,"scale_factor":1.2000000000000002,"degrees_cw":3.5,"translate_x":-85,"translate_y":-10},{"filename":"output.mp4","start_time":2424.93805,"end_time":2430.875605,"trim_complete":true,"scale_factor":1.2000000000000002,"degrees_cw":3.5,"translate_x":-85,"translate_y":-10},{"filename":"output.mp4","start_time":2443.050378,"end_time":2452.109267,"trim_complete":true,"scale_factor":1.2000000000000002,"degrees_cw":3.5,"translate_x":-85,"translate_y":-10},{"filename":"output.mp4","start_time":2583.486581,"end_time":2591.962129,"trim_complete":true,"scale_factor":1.2000000000000002,"degrees_cw":3.5,"translate_x":-85,"translate_y":-10},{"filename":"output.mp4","start_time":2694.9507,"end_time":2705.588031,"trim_complete":true,"scale_factor":1.2000000000000002,"degrees_cw":3.5,"translate_x":-85,"translate_y":-10},{"filename":"output.mp4","start_time":2762.629595,"end_time":2768.999046,"trim_complete":true,"scale_factor":1.2000000000000002,"degrees_cw":3.5,"translate_x":-85,"translate_y":-10},{"filename":"output.mp4","start_time":2807.230948,"end_time":2819.333235,"trim_complete":true,"scale_factor":1.2000000000000002,"degrees_cw":3.5,"translate_x":-85,"translate_y":-10},{"filename":"output.mp4","start_time":2832.227822,"end_time":2847.70315,"trim_complete":true,"scale_factor":1.2000000000000002,"degrees_cw":3.5,"translate_x":-85,"translate_y":-10}]'
#stringified_array = '[{"filename":"output.mp4","start_time":430.345698,"end_time":452.051524,"trim_complete":true,"scale_factor":1.2000000000000002,"degrees_cw":0.5,"translate_x":20,"translate_y":15},{"filename":"output.mp4","start_time":479.852208,"end_time":493.752535,"trim_complete":true,"scale_factor":1.2000000000000002,"degrees_cw":0.5,"translate_x":20,"translate_y":15}]'


#12/9/18
stringified_array = '[{"filename":"ooot.mp4","start_time":28.27574,"end_time":47.750977,"trim_complete":true,"scale_factor":1,"degrees_cw":0,"translate_x":0,"translate_y":0},{"filename":"ooot.mp4","start_time":79.871485,"end_time":94.717527,"trim_complete":true,"scale_factor":1,"degrees_cw":0,"translate_x":0,"translate_y":0},{"filename":"ooot.mp4","start_time":185.200277,"end_time":190.325373,"trim_complete":true,"scale_factor":1,"degrees_cw":0,"translate_x":0,"translate_y":0},{"filename":"ooot.mp4","start_time":204.563875,"end_time":208.101467,"trim_complete":true,"scale_factor":1,"degrees_cw":0,"translate_x":0,"translate_y":0},{"filename":"ooot.mp4","start_time":276.09826,"end_time":288.970874,"trim_complete":true,"scale_factor":1,"degrees_cw":0,"translate_x":0,"translate_y":0},{"filename":"ooot.mp4","start_time":305.75491,"end_time":321.401965,"trim_complete":true,"scale_factor":1,"degrees_cw":0,"translate_x":0,"translate_y":0},{"filename":"ooot.mp4","start_time":352.120743,"end_time":365.099769,"trim_complete":true,"scale_factor":1,"degrees_cw":0,"translate_x":0,"translate_y":0},{"filename":"ooot.mp4","start_time":487.733697,"end_time":494.228122,"trim_complete":true,"scale_factor":1,"degrees_cw":0,"translate_x":0,"translate_y":0},{"filename":"ooot.mp4","start_time":544.706554,"end_time":552.707959,"trim_complete":true,"scale_factor":1,"degrees_cw":0,"translate_x":0,"translate_y":0},{"filename":"ooot.mp4","start_time":562.131104,"end_time":569.079029,"trim_complete":true,"scale_factor":1,"degrees_cw":0,"translate_x":0,"translate_y":0},{"filename":"ooot.mp4","start_time":582.675063,"end_time":591.021901,"trim_complete":true,"scale_factor":1,"degrees_cw":0,"translate_x":0,"translate_y":0},{"filename":"ooot.mp4","start_time":612.746726,"end_time":628.003487,"trim_complete":true,"scale_factor":1,"degrees_cw":0,"translate_x":0,"translate_y":0},{"filename":"ooot.mp4","start_time":649.055877,"end_time":663.353982,"trim_complete":true,"scale_factor":1,"degrees_cw":0,"translate_x":0,"translate_y":0},{"filename":"ooot.mp4","start_time":837.848223,"end_time":848.249301,"trim_complete":true,"scale_factor":1,"degrees_cw":0,"translate_x":0,"translate_y":0},{"filename":"ooot.mp4","start_time":863.227133,"end_time":879.090318,"trim_complete":true,"scale_factor":1,"degrees_cw":0,"translate_x":0,"translate_y":0},{"filename":"ooot.mp4","start_time":928.658438,"end_time":943.995747,"trim_complete":true,"scale_factor":1,"degrees_cw":0,"translate_x":0,"translate_y":0},{"filename":"ooot.mp4","start_time":1118.568114,"end_time":1141.705942,"trim_complete":true,"scale_factor":1,"degrees_cw":0,"translate_x":0,"translate_y":0},{"filename":"ooot.mp4","start_time":1225.129205,"end_time":1229.020307,"trim_complete":true,"scale_factor":1,"degrees_cw":0,"translate_x":0,"translate_y":0},{"filename":"ooot.mp4","start_time":1783.500993,"end_time":1794.680701,"trim_complete":true,"scale_factor":1,"degrees_cw":0,"translate_x":0,"translate_y":0},{"filename":"ooot.mp4","start_time":1807.112167,"end_time":1813.974502,"trim_complete":true,"scale_factor":1,"degrees_cw":0,"translate_x":0,"translate_y":0},{"filename":"ooot.mp4","start_time":1849.769778,"end_time":1858.025115,"trim_complete":true,"scale_factor":1,"degrees_cw":0,"translate_x":0,"translate_y":0},{"filename":"ooot.mp4","start_time":1944.935875,"end_time":1966.540406,"trim_complete":true,"scale_factor":1,"degrees_cw":0,"translate_x":0,"translate_y":0},{"filename":"ooot.mp4","start_time":2090.706133,"end_time":2099.658669,"trim_complete":true,"scale_factor":1,"degrees_cw":0,"translate_x":0,"translate_y":0},{"filename":"ooot.mp4","start_time":2131.425922,"end_time":2141.402155,"trim_complete":true,"scale_factor":1,"degrees_cw":0,"translate_x":0,"translate_y":0},{"filename":"ooot.mp4","start_time":2163.019994,"end_time":2171.90231,"trim_complete":true,"scale_factor":1,"degrees_cw":0,"translate_x":0,"translate_y":0},{"filename":"ooot.mp4","start_time":2234.630202,"end_time":2243.545284,"trim_complete":true,"scale_factor":1,"degrees_cw":0,"translate_x":0,"translate_y":0},{"filename":"ooot.mp4","start_time":2275.492676,"end_time":2288.869136,"trim_complete":true,"scale_factor":1,"degrees_cw":0,"translate_x":0,"translate_y":0},{"filename":"ooot.mp4","start_time":2419.937636,"end_time":2435.727413,"trim_complete":true,"scale_factor":1,"degrees_cw":0,"translate_x":0,"translate_y":0},{"filename":"ooot.mp4","start_time":2480.832407,"end_time":2500.276225,"trim_complete":true,"scale_factor":1,"degrees_cw":0,"translate_x":0,"translate_y":0},{"filename":"ooot.mp4","start_time":2536.482616,"end_time":2546.24328,"trim_complete":true,"scale_factor":1,"degrees_cw":0,"translate_x":0,"translate_y":0},{"filename":"ooot.mp4","start_time":2786.295378,"end_time":2799.959192,"trim_complete":true,"scale_factor":1,"degrees_cw":0,"translate_x":0,"translate_y":0},{"filename":"ooot.mp4","start_time":3159.648461,"end_time":3175.871927,"trim_complete":true,"scale_factor":1,"degrees_cw":0,"translate_x":0,"translate_y":0},{"filename":"ooot.mp4","start_time":3295.033008,"end_time":3327.528726,"trim_complete":true,"scale_factor":1,"degrees_cw":0,"translate_x":0,"translate_y":0},{"filename":"ooot.mp4","start_time":3465.562212,"end_time":3473.422818,"trim_complete":true,"scale_factor":1,"degrees_cw":0,"translate_x":0,"translate_y":0},{"filename":"ooot.mp4","start_time":3644.437737,"end_time":3662.317463,"trim_complete":true,"scale_factor":1,"degrees_cw":0,"translate_x":0,"translate_y":0}]'




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
#video_export.export(video_clips)
# .. quickly (no reframe)
video_export_no_reframe.export(video_clips)

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