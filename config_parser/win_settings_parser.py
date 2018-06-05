import pathlib
import configparser


SETTINGS_PATH = pathlib.Path('./config.ini')


class WINSettingsParser:
    def __init__(self):
        self.config = configparser.ConfigParser()

        try:
            self.config.read('SETTINGS_PATH')
        except EnvironmentError:
            with open('example.ini', 'w+') as configfile:
                self.config.write(configfile)

    def value(self, category, variable, default):
        return self.config[category][variable] or default

    def setValue(self, category, variable, value):
        self.config[category][variable] = value

    def save(self):
        with open(SETTINGS_PATH, 'wb') as fp:
            dump(self.settings, fp, fmt=FMT_XML)
