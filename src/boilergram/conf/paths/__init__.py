__all__ = ['path_settings']

import pathlib
from boilergram.conf.paths import settings, paths

path_settings = settings.PathSettings(paths, pathlib.Path(__file__).parent.parent.parent)
