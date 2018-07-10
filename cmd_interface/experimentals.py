# Experimental features


# Use audio to get shots. (12/7/17)

# extract and audio file from the video file
'''import subprocess

ffmpeg_path = "C:/Users/matt2/Downloads/ffmpeg-20171204-71421f3-win64-static/ffmpeg-20171204-71421f3-win64-static/bin/ffmpeg.exe"
command = ffmpeg_path + " -i full_match.mp4 -ab 160k -ac 2 -ar 44100 -vn audio.wav"

subprocess.call(command, shell=True)'''


# plot audio file (.wav)
'''import matplotlib.pyplot as plt
import numpy as np
import wave

file = 'audio.wav'

with wave.open(file,'r') as wav_file:
    #Extract Raw Audio from Wav File
    signal = wav_file.readframes(-1)
    signal = np.fromstring(signal, 'Int16')

    #Split the data into channels 
    channels = [[] for channel in range(wav_file.getnchannels())]
    for index, datum in enumerate(signal):
        channels[index%len(channels)].append(datum)

    #Get time from indices
    fs = wav_file.getframerate()
    Time=np.linspace(0, len(signal)/len(channels)/fs, num=len(signal)/len(channels))

    #Plot
    plt.figure(1)
    plt.title('Signal Wave...')
    for channel in channels:
        plt.plot(Time,channel)
    plt.show()

'''












'''
# find lines in image (1/11/17)


# Python program to illustrate HoughLine
# method for line detection
import cv2
import numpy as np
 
# Reading the required image in 
# which operations are to be done. 
# Make sure that the image is in the same 
# directory in which this python program is
img = cv2.imread('test_files/look_for_lines.jpg')
 
# Convert the img to grayscale
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize = 3)


cv2.imshow('edges', edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
'''

# find blobs in image (1/12/18)

# Standard imports
import cv2
import numpy as np;
 
# Read image
im = cv2.imread("test_files/sample.jpg", cv2.IMREAD_GRAYSCALE)
 
# Set up the detector with default parameters.
detector = cv2.SimpleBlobDetector_create()
 
# Detect blobs.
keypoints = detector.detect(im)
 
# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
 
# Show keypoints
cv2.imshow("Keypoints", im_with_keypoints)
cv2.waitKey(0)