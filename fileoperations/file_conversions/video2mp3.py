import os

import moviepy.editor as mp


def convert(subdir, file):
    try:
        clip = mp.VideoFileClip("/home/ila/Music/video_songs/elangathu.mp4").duration
        desti = file.split(".")[0]
        clip.audio.write_audiofile(desti + ".mp3")
        print(file, "converted successfully")
    except Exception as e:
        print("!!! ERROR  while converting ", file, e)


for subdir, dirs, files in os.walk("/home/ila/Music/video_songs"):
    for file in files:
        convert(subdir, file)
