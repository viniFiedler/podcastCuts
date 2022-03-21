
from Debug import *
import os

class Config:

    # Link CLI Parameter with the Config Name
    configParams = {
        "-v": "videoId",
        "--video": "videoId",
        "-r": "resolution",
        "--resolution": "resolution"
    }

    valueParamNeeded = {
        "videoId": True,
        "resolution": True,
        "downloadPath": True,
    }

    configs = {
        "videoId": None,
        "downloadPath": None,
        "resolution": None,     
    }

    configDefaults = {
        "downloadPath": os.path.join(os.getcwd(), "videosFolder" ),
        "resolution": "360p"
    }

    configGroups = {
        "download": [ "videoId", "downloadPath", "resolution" ]
    }

    @staticmethod
    def extractConfig(args: list):

        # Config.loadconfigFile()

        for param in args:

            if param not in Config.configParams:
                # TODO -- Build a Error System, or maybe i could just print a warning and move on
                continue

            paramIndex = args.index(param)
            configName = Config.configParams[param]
            configValue = args[paramIndex + 1]

            if Config.valueParamNeeded[configName]:
                Config.setConfig(configName, configValue)
            else:
                Config.setConfig(configName, True)

    @staticmethod
    def getConfig(configName: str):
        return Config.configs[configName]

    @staticmethod
    def setConfig(configName: str, configValue):
        Config.configs[configName] = configValue

    @staticmethod
    def isNone(configName: str) -> bool:
        if Config.getConfig(configName) == None:
            return True
        else:
            return False

    @staticmethod
    def getDefault(configName: str):
        return Config.configDefaults[configName]

    @staticmethod
    def getConfigGroup(group: str) -> dict:
        configSet = {}

        # TODO -- Error if group doesnt exist

        for configName in Config.configGroups[group]:

            if Config.isNone(configName):
                try:
                    configSet[configName] = Config.getDefault(configName)
                except:
                    pass
            else:
                configSet[configName] = Config.getConfig(configName)

        return configSet

    @staticmethod
    def setNeeded(groups: list | str):

        if type(groups) == str:
            groups = [groups]

        for group in groups:
            
            for configName in Config.configGroups[group]:
                if Config.isNone(configName):

                    try:
                        Config.setConfig(configName, Config.configDefaults[configName])
                    except KeyError:
                        validated = False
                        configValue = None
                        while not validated: # TODO -- Make and directory with a better config name for the user
                            configValue = input("Please give us the {} >>> ".format(configName))

                            # TODO -- check if value is valid, maybe other class for that?
                            validated = True
                        
                        Config.setConfig(configName, configValue)                    
        
    @staticmethod
    def loadconfigFile( ):
        pass
