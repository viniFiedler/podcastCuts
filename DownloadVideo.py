from pytube import YouTube
from Config import *
import os
import os.path
import json


## Create json if dont't exists, and if does, append video info to json
class videoJson ():

    def __init__(self, link):
        yt = YouTube(link)
        self._link = link
        self._video_title = yt.title
        self._video_length = yt.length
        self._video_author = yt.channel_url
        self._path_json = os.path.join(os.getcwd(), "videosFolder/video.json" )
        
        self._dictionary = {
            "video_title" : self._video_title,
            "video_length" : self._video_length,
            "video_link"  : self._link,
            "channel_url" : self._video_author,
                }

    @property
    def title(self):
        return self._video_title

    @property
    def length(self):
        return self._video_length
    
    @property
    def author(self):
        return self._video_author
    
    @property
    def path(self):
        return self._path_json
    
    @property
    def dictionary(self):
        return self.dictionary
    

    ## use object in config.py to found path
    ## path_json = os.path.join(os.getcwd(), "videosFolder/video.json" ) (old version)

    
    ##check if the json exits, if don't, creates it
    def _createJson(self):
        if(os.path.exists(self._path_json) == False):
                first_dictionary = {"video_details":[]}
                json_object = json.dumps(first_dictionary, indent = 3)
                with open(self._path_json, "w") as outfile:
                    outfile.write(json_object) 
                    outfile.close() 
       


    
    ## Append json in correct format
    def addJson(self):

        self._createJson()

        try:
            with open(self._path_json,'r+') as outfile:
                    file_data = json.load(outfile)

                    file_data["video_details"].append(self._dictionary)

                    outfile.seek(0)

                    json.dump(file_data,outfile,indent = len(self._dictionary))

                    outfile.close() 
        except:
            print("Error in Appending video.json")
            



def dowloadVideo():
    link = input("Please enter a Youtube link\n")

    pathToVideos = os.path.join(os.getcwd(), "videosFolder" )

    dowloadedVideoJson = videoJson(link)

    dowloadedVideoJson.addJson()

    resolution = "360p"


    
    
    yt = YouTube(link)
    stream = yt.streams.filter(res=resolution).first()
    stream.download(pathToVideos)


if __name__ == "__main__":
    dowloadVideo()
