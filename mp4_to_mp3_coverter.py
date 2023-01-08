
from moviepy.editor import *
import os

# setting environment variable for FFMPEG
# os.environ["IMAGEIO_FFMPEG_EXE"] = "/opt/homebrew/Cellar/ffmpeg/5.1.2_1/bin/ffmpeg"

"""
function for coverting mp4 to mp3

Note: if you are getting this error - RuntimeError: No ffmpeg exe could be found. Install ffmpeg on your system, or set the IMAGEIO_FFMPEG_EXE environment variable.

Steps to fix this on mac (using brew) -> 
- install brew 
- brew install ffmpeg 

fixed issue for me :) . For other operating system check stack overflow.
"""


def mp4_to_mp3_converter(video_file_path, audio_file_path):
    video_file = AudioFileClip(video_file_path)
    video_file.write_audiofile(audio_file_path)
    print("video coverted to mp3.")
    video_file.close()


# change the video path
video_file_path = "miscellaneous_files/calm_down_song_video.mp4"
# give the location of audio path
audio_file_path = "miscellaneous_files/calm_down_song.mp3"

mp4_to_mp3_converter(video_file_path, audio_file_path)
