import pathlib, configparser, getpass


# Should get this prop from dcc.build_label
build_label = 'devel'


class WINSettingsParser:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.path = pathlib.Path('c:\\users\\' + getpass.getuser()
                                 + '\\AppData\\Roaming\\Nemetschek\\Vectorworks Cloud Services '
                                 + build_label + '.ini')

        try:
            self.config.read(self.path)
            if not self.config:
                raise EnvironmentError
        except EnvironmentError:
            with open(self.path, 'w+') as configfile:
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
        with open(self.path, 'w+') as configfile:
            self.config.write(configfile)
