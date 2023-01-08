
from moviepy.editor import *
import os

# setting environment variable for FFMPEG
# os.environ["IMAGEIO_FFMPEG_EXE"] = "/opt/homebrew/Cellar/ffmpeg/5.1.2_1/bin/ffmpeg"

"""
function for coverting mp4 to mp3
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
