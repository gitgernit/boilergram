import pathlib

import pytest


@pytest.fixture(scope='class')
def temporary_template_path(
    tmp_path_factory: pytest.TempPathFactory,
) -> pathlib.Path:
    return tmp_path_factory.mktemp('template')
