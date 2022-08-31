
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
        "downloadPath": os.path.join(os.getcwd(), "videosFolder"),
        "resolution": '360p',
    }

    configGroups = {
        "download": ["videoId", "downloadPath", "resolution"]
    }

    @staticmethod
    def extractConfig(args: list):

        # Config.loadconfigFile()

        for index, param in enumerate(args):

            if param not in Config.configParams:
                # TODO -- Build a Error System, or maybe i could just print a warning and move on
                continue

            configName = Config.configParams[param]
            configValue = args[index + 1]

            if Config.valueParamNeeded[configName]:
                Config.setConfig(configName, configValue)
            else:
                Config.setConfig(configName, True)

    @staticmethod
    # NOTE -- Maybe the getConfig() and setConfig() should be renamed to set() and get()
    def getConfig(configName: str):
        return Config.configs[configName]

    @staticmethod
    def setConfig(configName: str, configValue):
        Config.configs[configName] = configValue

    @staticmethod
    def isNone(configName: str) -> bool:
        if Config.getConfig(configName) is None:
            return True
        else:
            return False

    @staticmethod
    def getGroup(group: str) -> dict:
        configSet = {}

        for configName in Config.configGroups[group]:
            configSet[configName] = Config.getConfig(configName)

        return configSet

    @staticmethod
    def setNeeded(groups: list | str):

        if not isinstance(groups, str):
            groups = [groups]

        for group in groups:

            for configName in Config.configGroups[group]:
                if Config.isNone(configName):

                    validated = False
                    configValue = None
                    while not validated:  # TODO -- Make and directory with a better config name for the user
                        configValue = input(
                            f"Please give us the {configName} >>> ")

                        # TODO -- check if value is valid, maybe other class for that?
                        validated = True

                    Config.setConfig(configName, configValue)

    @staticmethod
    def loadconfigFile():
        pass
