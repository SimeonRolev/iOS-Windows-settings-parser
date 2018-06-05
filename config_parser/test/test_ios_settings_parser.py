import os, pathlib, pytest
from .. import ios_settings_parser, win_settings_parser, settings_parser, settings


SETTINGS_PATH = './settings.plist'


class TestIOSParser:
    def test_value(self):
        try:
            os.remove(SETTINGS_PATH)
        except OSError:
            pass

        s = settings_parser.SettingsParser('iOS')
        assert s.value(settings.account_password, '30') == '30'

        s.setValue(settings.account_password, 'password')
        s.save()

        assert s.parser.settings['account']['password'] == 'password'
        assert not s.parser.settings.get('not_existing_prop', False)

        s.setValue(settings.account_password, 'new_password')
        s.save()

        assert s.parser.settings['account']['password'] == 'new_password'
        assert s.value(settings.account_password, 'new_password')
