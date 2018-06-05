import pathlib
import configparser


SETTINGS_PATH = pathlib.Path('./config.ini')


class WINSettingsParser:
    def __init__(self):
        self.config = configparser.ConfigParser()

        if not self.config.read(SETTINGS_PATH):
            with open(SETTINGS_PATH, 'w+') as configfile:
                self.config.write(configfile)

    def value(self, category, variable, default):
        if category in self.config:
            return self.config.get(category, variable, fallback=default)
        return default

    def setValue(self, category, variable, value):
        if category not in self.config:
            self.config[category] = {}

        self.config[category][variable] = value

    def save(self):
        with open(SETTINGS_PATH, 'w+') as configfile:
            self.config.write(configfile)
