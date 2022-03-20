
from Debug import Debug

class Config:

    # TODO -- Replace every "Config.configs[configName][1] == None" with a function called isNull()

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
    def extractConfig(args: list = None):

        # Config.loadconfigFile()

        args.pop(0)

        if args == None: pass

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
    def getConfigGroup(group: str) -> dict:
        configSet = {}

        for configName in Config.configGroups[group]:

            if Config.configs[configName][1] == None:
                try:
                    configSet[configName] = Config.configDefaults[configName]
                except:
                    pass
            else:
                configSet[configName] = Config.configs[configName][1]

        return configSet

    @staticmethod
    def setNeeded(groups: list): # TODO -- Make this function accept a single string
        for group in groups:
            
            for configName in Config.configGroups[group]:
                if Config.configs[configName][1] == None:

                    try:
                        Config.setConfig(configName, Config.configDefaults[configName])
                    except:
                        pass

                    if Config.configs[configName][1] == None:
                        pass
                    else:
                        continue
                    
                    validated = False
                    configValue = None
                    while not validated: # TODO -- Make and directori with a better config name for the user
                        configValue = input("Please give us the {} >>> ".format(configName))
                        configValue = str(configValue)

                        # TODO -- check if value is valid, maybe a other class for that?
                        validated = True
                    
                    Config.setConfig(configName, configValue)
        
    @staticmethod
    def loadconfigFile( ):
        pass
