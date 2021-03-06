import os
from .. import settings_parser, settings


s = settings_parser.SettingsParser()
extension = '.ini' if s.os == 'Windows' else '.plist'
s.parser.path = './test-config' + extension


def scenario():
    # Set two unexisting values
    s.setValue(settings.account_password, 'password')
    s.setValue(settings.account_username, 'username')

    assert s.value(settings.account_password, '30') == 'password'
    assert s.value(settings.account_username, '30') == 'username'

    # Override one of the values
    s.setValue(settings.account_password, 'new_password')

    assert s.value(settings.account_password, '30') == 'new_password'
    assert s.value(settings.account_username,  '30') == 'username'


def delete_config_file():
    try:
        os.remove(s.parser.path)
    except OSError:
        pass


class TestWINParser:
    def test_value_from_init(self):
        delete_config_file()

        # Default value test
        assert s.value(settings.account_password, '30') == '30'

        scenario()

    def test_override_scenario(self):
        scenario()
        delete_config_file()
