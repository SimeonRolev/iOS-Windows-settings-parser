import pathlib
from plistlib import *


class OSXSettingsParser:
    def __init__(self):
        self.settings = {}
        self.path = pathlib.Path('~/Library/Preferences/org.pythonmac.unspecified.VectorworksCloudServices.plist')

        try:
            with open(self.path, 'rb') as fp:
                self.settings = load(fp, fmt=FMT_XML)
        except EnvironmentError:  # parent of IOError, OSError *and* WindowsError
            with open(self.path, 'wb+') as fp:
                dump(dict(), fp, fmt=FMT_XML)
                fp.seek(0)
                self.settings = load(fp, fmt=FMT_XML)

    def value(self, category, variable, default):
        return self.settings.get(category, {}) \
                            .get(variable, default)

    def setValue(self, category, variable, value):
        if not self.settings.get(category, False):
            self.settings[category] = {}

        self.settings[category][variable] = value
        self.save()

    def save(self):
        with open(self.path, 'wb') as fp:
            dump(self.settings, fp, fmt=FMT_XML)
