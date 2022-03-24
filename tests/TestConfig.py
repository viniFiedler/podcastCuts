import unittest

from Config import Config


class TestConfig(unittest.TestCase):

    # TODO -- Test no valid parameter with a mock
    # TODO -- Test for the setNeeded()

    def tearDown(self) -> None:
        # Resets the Config Class
        for configName in Config.configs:
            Config.setConfig(configName, None)

    def test_get(self):
        self.assertEqual(Config.getConfig('videoId'), None)

    def test_set(self):
        
        Config.setConfig('videoId', 'video_link')

        self.assertEqual(Config.getConfig('videoId'), 'video_link')

    def test_set_extract(self):
        params = ['-v', 'video_link', '-r', 'resolution']

        Config.extractConfig(params)

        self.assertEqual(Config.getConfig('videoId'), 'video_link')
        self.assertEqual(Config.getConfig('resolution'), 'resolution')

    def test_is_none(self):

        first_state = Config.isNone('videoId')

        Config.setConfig('videoId', 'video_link')
        second_state = Config.isNone('videoId')

        self.assertEqual(first_state, True)
        self.assertEqual(second_state, False)

    def test_get_group(self):

        configs = {
            "videoId": "video_link",
            "downloadPath": "download_path",
            "resolution": "random_res"
        }

        for config in configs:
                Config.setConfig(config, configs[config])

        self.assertEqual(Config.getGroup('download'), configs)
