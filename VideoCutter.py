from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip


class cutter():

    def __init__(self, videoName: str):
        self._video_name = videoName

    def cutter(self, startTime: int, endTime: int, type: str = 'seconds'):

        if(type == 'seconds'):
            pass

        elif(type == 'minutes'):
            startTime *= 60
            endTime *= 60

        ffmpeg_extract_subclip(self._video_name, startTime,
                               endTime, targetname=str((int)(startTime)) + "-" + str((int)(endTime))+".mp4")


if __name__ == '__main__':
    teste = cutter(
        "videosFolder/Criei um VÍRUS com apenas 10 linhas de código (PYTHON).mp4")
    teste.cutter(0, 15)
