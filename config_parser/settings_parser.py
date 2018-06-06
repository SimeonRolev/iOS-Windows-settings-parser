import sys

from config_parser.osx_settings_parser import OSXSettingsParser
from config_parser.win_settings_parser import WINSettingsParser


class SettingsParser:
    def __init__(self):
        self.os = 'OSX' if sys.platform == 'darwin' else 'Windows'
        self.parser = OSXSettingsParser() if self.os == 'OSX' else WINSettingsParser()

    def value(self, name, default):
        category, variable = name.split('/')
        return self.parser.value(category, variable, default)

    def setValue(self, name, value):
        category, variable = name.split('/')
        self.parser.setValue(category, variable, value)

    def save(self):
        self.parser.save()
