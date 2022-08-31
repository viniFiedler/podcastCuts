import numpy as np
from PIL import Image
import moviepy
import moviepy.editor as mp
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip


class cutter():

    def __init__(self, videoPath: str):
        self._video_path = videoPath
        self._time = 0
        self._cut_name = ""

    def time_cutter(self, startTime: int, endTime: int, type: str = 'seconds'):

        if(type == 'seconds'):
            pass
            self._time = endTime - startTime

        elif(type == 'minutes'):
            startTime *= 60
            endTime *= 60
            self._time = endTime - startTime

        self._cut_name = str((int)(startTime)) + "-" + \
            str((int)(endTime)) + ".mp4"
        ffmpeg_extract_subclip(self._video_path, startTime,
                               endTime, targetname=self._cut_name)

    # TODO create a blur background using the video image instead of using a black image
    def _background_creator(self, width: int, height: int):
        img = Image.new('RGB', (width, height))
        img.save('blackBackGround.png')

    # TODO DURATION OF IMAGE get from cut
    def format_cutter(self, height: int, width: int):

        self._background_creator(height, width)
        logo = (mp.ImageClip("blackBackGround.png")).set_duration(self._time)
        video = mp.VideoFileClip(self._cut_name)
        final = mp.CompositeVideoClip(
            [logo, video.set_position("center")])
        final.write_videofile("test.mp4")


if __name__ == '__main__':
    teste = cutter(
        "videosFolder/Criei um VÍRUS com apenas 10 linhas de código (PYTHON).mp4")
    teste.time_cutter(0, 15)
    teste.format_cutter(500, 500)
