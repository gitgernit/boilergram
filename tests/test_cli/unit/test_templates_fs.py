import pathlib

from boilergram.core.management.inits import copy_bot_template
from boilergram.core.management.inits import rename_bot_template

DESIRED_PATHS = [
    'bot',
    'bot/bot/',
    'bot/bot/__init__.py',
    'bot/bot/settings.py',
    'bot/manage.py',
]
DESIRED_RENAMED_PATHS = [
    'rbot',
    'rbot/rbot/',
    'rbot/rbot/__init__.py',
    'rbot/rbot/settings.py',
    'rbot/manage.py',
]


class TestTemplatesFilesystem:
    def test_copy_bot_template(
        self,
        temporary_template_path: pathlib.Path,
    ) -> None:
        copy_bot_template(temporary_template_path)

        for path in DESIRED_PATHS:
            assert (temporary_template_path / path).exists()

    def test_rename_bot_template(
        self,
        temporary_template_path: pathlib.Path,
    ) -> None:
        rename_bot_template(temporary_template_path, 'rbot')

        for path in DESIRED_RENAMED_PATHS:
            assert (temporary_template_path / path).exists()
