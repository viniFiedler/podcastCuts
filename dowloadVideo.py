from pytube import YouTube

def dowloadVideo():
    link = input("Please enter a Youtube link\n")
    pathToVideos = '/home/vinicius/codes/dowloadAndEdit/videosFolder'
    resolution = "360p"

    yt = YouTube(link)
    stream = yt.streams.filter(res=resolution).first()
    stream.download(pathToVideos)


if __name__ == "__main__":
    dowloadVideo()