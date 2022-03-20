
from Debug import Debug

class Config:

    # Link CLI Parameter with the Config Name
    configParams = {
        "-v": "videoId",
        "--video": "videoId",
        "-r": "resolution",
        "--resolution": "resolution"
    }

    # [ valueParameterNeeded, Value ] NOTE -- Maybe put the valueParameter Needed in other attribute
    configs = {
        "videoId": [True, None],
        "downloadPath": [True, None],
        "resolution": [True, None],     
    }

    configDefaults = {
        "downloadPath": "/home/nate/workspace/proj/podcastCuts/videos/",
        "resolution": "360p"
    }

    configGroups = {
        "download": [ "videoId", "downloadPath", "resolution" ]
    }

    @staticmethod
    def extractConfig(args: list):

        # Config.loadconfigFile()

        args.pop(0)

        for param in args:

            if param not in Config.configParams:
                # TODO -- Build a Error System, or maybe i could just print a warning and move on
                continue

            paramIndex = args.index(param)
            configName = Config.configParams[param]
            configValue = args[paramIndex + 1]

            if Config.configs[configName][0] == True:
                Config.configs[configName][1] = configValue
            else:
                Config.configs[configName][1] = True

    @staticmethod
    def getConfig(configName: str):
        return Config.configs[configName][1]

    @staticmethod
    def setConfig(configName: str, configValue):
        Config.configs[configName][1] = configValue

    @staticmethod
    def isNone(configName: str) -> bool:
        if Config.configs[configName][1] == None:
            return True
        else:
            return False

    @staticmethod
    def getConfigGroup(group: str) -> dict:
        configSet = {}

        for configName in Config.configGroups[group]:

            if Config.isNone(configName):
                try:
                    configSet[configName] = Config.configDefaults[configName]
                except:
                    pass
            else:
                configSet[configName] = Config.configs[configName][1]

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
                    except:
                        pass

                    if Config.isNone(configName):
                        pass
                    else:
                        continue
                    
                    validated = False
                    configValue = None
                    while not validated: # TODO -- Make and directori with a better config name for the user
                        configValue = input("Please give us the {} >>> ".format(configName))
                        configValue = str(configValue) # NOTE -- I think this cast is not necessary

                        # TODO -- check if value is valid, maybe other class for that?
                        validated = True
                    
                    Config.setConfig(configName, configValue)
        
    @staticmethod
    def loadconfigFile( ):
        pass
