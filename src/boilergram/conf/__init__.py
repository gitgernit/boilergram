__all__ = ['path_settings']

import pathlib
from boilergram.conf import paths


class PathSettings:
    def __init__(self, package_root: pathlib.Path):
        self.PACKAGE_ROOT = package_root.resolve()

        for setting, value in (
                (setting, getattr(paths, setting))
                for setting in dir(paths)
        ):
            if setting.isupper() and '.' in value:
                pathlike_value = value.replace('.', '/')
                path_value = pathlib.Path(self.PACKAGE_ROOT / '/'.join(
                    pathlike_value.split('/')[1:]
                )).resolve()

                setattr(self, setting, path_value)

    def __getattr__(self, item) -> pathlib.Path:
        return super().__getattribute__(self, item)


path_settings = PathSettings(pathlib.Path(__file__).parent.parent)
