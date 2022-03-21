from pytube import YouTube
from ErrorHandler import *
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
    def __createJson(self):
        if(os.path.exists(self._path_json) == False):
                first_dictionary = {"video_details":[]}
                json_object = json.dumps(first_dictionary, indent = 3)
                with open(self._path_json, "w") as outfile:
                    outfile.write(json_object) 
                    outfile.close() 
       


    
    ## Append json in correct format
    def addJson(self):

        self.__createJson()

        try:
            with open(self._path_json,'r+') as outfile:
                    file_data = json.load(outfile)

                    file_data["video_details"].append(self._dictionary)

                    outfile.seek(0)

                    json.dump(file_data,outfile,indent = len(self._dictionary))

                    outfile.close() 
        except:
            showError("Unable To create Json")
            



class dowloader():

    def __init__(self,link, resolution = '360p'):
        self._link = link
        self._path_videos = os.path.join(os.getcwd(), "videosFolder" )
        self.json = videoJson(link)
        self._resolution = resolution

    ## Download Video from Youtube
    def download(self):
        try:
            yt = YouTube(self._link)
            stream = yt.streams.filter(res=self._resolution).first()
            stream.download(self._path_videos)
            self.json.addJson()
        except:
            showError("Unable to Download Video")
        


if __name__ == "__main__":
    TestVideo = dowloader("https://www.youtube.com/watch?v=uT_DcEK6jFU&ab_channel=AulaLivre")
    TestVideo.download()
