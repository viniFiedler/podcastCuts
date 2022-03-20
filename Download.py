from pytube import YouTube

class Downloader:

    @staticmethod
    def download(config : dict):
        #link = "https://www.youtube.com/watch?v=JfWESF3cSPc"
        #pathToVideos = "/home/nate/workspace/proj/podcastCuts/videos/"
        #resolution = "360p"

        link = config["videoId"]
        pathToVideos = config["downloadPath"]
        resolution = config["resolution"]

        yt = YouTube(link)
        stream = yt.streams.filter(res=resolution).first()
        stream.download(pathToVideos)
                     

"""""
def dowloadVideo():
    link = input("Please enter a Youtube Video ID or full link > ")
    pathToVideos = '/home/nate/workspace/proj/podcastCuts/'
    resolution = "360p"

    yt = YouTube(link)
    stream = yt.streams.filter(res=resolution).first()
    stream.download(pathToVideos)
"""