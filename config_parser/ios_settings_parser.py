import pathlib
from plistlib import *


SETTINGS_PATH = pathlib.Path('./settings.plist')


class IOSSettingsParser:
    def __init__(self):
        self.settings = {}
        try:
            with open(SETTINGS_PATH, 'rb') as fp:
                self.settings = load(fp, fmt=FMT_XML)
        except EnvironmentError:  # parent of IOError, OSError *and* WindowsError
            with open(SETTINGS_PATH, 'wb+') as fp:
                dump(dict(example="Example setting"), fp, fmt=FMT_XML)
                fp.seek(0)
                self.settings = load(fp, fmt=FMT_XML)

    def value(self, category, variable, default):
        return self.settings.get(category, {}) \
                            .get(variable, default)

    def setValue(self, category, variable, value):
        if not self.settings.get(category, False):
            self.settings[category] = {}

        self.settings[category][variable] = value

    def save(self):
        with open(SETTINGS_PATH, 'wb') as fp:
            dump(self.settings, fp, fmt=FMT_XML)
