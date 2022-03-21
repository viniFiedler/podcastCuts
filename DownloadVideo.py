
from fileinput import close
from importlib.resources import path
from venv import create
from pytube import YouTube
import os
import os.path
import json


## Create json if dont't exists, and if does, append video info to json
class videoJson ():

    def __init__(self, link):
        yt = YouTube(link)
        self.video_title = yt.title
        self.video_length = yt.length
        self.video_author = yt.channel_url
        self.path_json = os.path.join(os.getcwd(), "videosFolder/video.json" )

        self.dictionary = {
        "video_title" : self.video_title,
        "video_length" : self.video_length,
        "video_link"  : link,
        "channel_url" : self.video_author,
                }

    ## use object in config.py to found path
    ## path_json = os.path.join(os.getcwd(), "videosFolder/video.json" ) (old version)

    
    ##check if the json exits, if don't, creates it
    def _createJson(self):
        try:    
            if(os.path.exists(self.path_json) == False):
                print(self.path_json)
                first_dictionary = {"video_details":[]}

                json_object = json.dumps(first_dictionary, indent = len(self.dictionary))
                with open(self.path_json, "w") as outfile:
                    outfile.write(json_object) 
                    outfile.close() 
        except:
            print("Error in Creating video.json")


    
    ## Append json in correct format
    def addJson(self):

        self._createJson()
        
        try:
            with open(self.path_json,'r+') as outfile:
                file_data = json.load(outfile)
                file_data["video_details"].append(self.dictionary)
                outfile.seek(0)
                json.dump(file_data,outfile,indent = len(self.dictionary))
                outfile.close() 
        except:
            print("Error in Appending video.json")
            



def dowloadVideo():
    link = input("Please enter a Youtube link\n")

    pathToVideos = os.path.join(os.getcwd(), "videosFolder" )
    dowloadedVideoJson = videoJson(link)
    dowloadedVideoJson
    resolution = "360p"

    
    
    yt = YouTube(link)
    stream = yt.streams.filter(res=resolution).first()
    stream.download(pathToVideos)


if __name__ == "__main__":
    dowloadVideo()
