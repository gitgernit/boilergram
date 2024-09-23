__all__ = []

import pathlib
import types


class PathSettings:
    def __init__(
        self,
        source: types.ModuleType,
        package_root: pathlib.Path,
    ) -> None:
        self.PACKAGE_ROOT = package_root.resolve()

        for setting, value in (
            (setting, getattr(source, setting)) for setting in dir(source)
        ):
            if setting.isupper() and '.' in value:
                pathlike_value = value.replace('.', '/')
                path_value = pathlib.Path(
                    self.PACKAGE_ROOT
                    / '/'.join(pathlike_value.split('/')[1:]),
                ).resolve()

                setattr(self, setting, path_value)

    def __getattribute__(self, item: str) -> pathlib.Path:
        return super().__getattribute__(item)
