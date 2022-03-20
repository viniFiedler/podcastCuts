
from fileinput import close
from importlib.resources import path
from pytube import YouTube
import os
import os.path
import json


## create json if dont't exists and if does, append video info to json
def writeJson(link):

    print(os.getcwd())

    yt = YouTube(link)
    video_title = yt.title
    video_length = yt.length
    video_author = yt.channel_url
    
    dictionary = {
        "video_title" : video_title,
        "video_length" : video_length,
        "video_link"  : link,
        "channel_url" : video_author,
                }

    
    path_json = os.path.join(os.getcwd(), "videosFolder/video.json" )

    if(os.path.exists(path_json) == False):
        first_dictionary = {"video_details":[]}
        json_object = json.dumps(first_dictionary, indent = len(dictionary))
        with open(path_json, "w") as outfile:
            outfile.write(json_object) 


    with open(path_json,'r+') as outfile:
       file_data = json.load(outfile)
       file_data["video_details"].append(dictionary)
       outfile.seek(0)
       json.dump(file_data,outfile,indent = len(dictionary))

    
    outfile.close() 

def dowloadVideo():
    link = input("Please enter a Youtube link\n")

    pathToVideos = os.path.join(os.getcwd(), "videosFolder" )
    
    resolution = "360p"

    writeJson(link)
    
    yt = YouTube(link)
    stream = yt.streams.filter(res=resolution).first()
    stream.download(pathToVideos)


if __name__ == "__main__":
    dowloadVideo()