from pytube import YouTube

class Downloader:

    @staticmethod
    def download(config : dict):

        link = config["videoId"]
        pathToVideos = config["downloadPath"]
        resolution = config["resolution"]

        yt = YouTube(link)
        stream = yt.streams.filter(res=resolution).first()
        stream.download(pathToVideos)
