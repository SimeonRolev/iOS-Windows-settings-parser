import pathlib

from config_parser.ios_settings_parser import IOSSettingsParser
from config_parser.win_settings_parser import WINSettingsParser


SETTINGS_PATH = pathlib.Path('./settings.plist')
OS = 'iOS'


class SettingsParser:
    def __init__(self, os):
        self.os = os
        self.parser = IOSSettingsParser() if self.os == 'iOS' else WINSettingsParser()

    def value(self, name, default):
        category, variable = name.split('/')
        return self.parser.value(category, variable, default)

    def setValue(self, name, value):
        category, variable = name.split('/')
        self.parser.setValue(category, variable, value)

    def save(self):
        self.parser.save()
