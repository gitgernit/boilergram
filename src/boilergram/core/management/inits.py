import shutil
import pathlib

from boilergram.conf.paths import path_settings


def copy_bot_template(target_dir: pathlib.Path) -> None:
    template_path = path_settings.PROJECT_TEMPLATE_MODULE.parent

    shutil.copytree(template_path, target_dir, dirs_exist_ok=True)


def rename_bot_template(bot_parent_dir: pathlib.Path, bot_name: str) -> None:
    bot_path = bot_parent_dir / 'bot'
    bot_path = bot_path.rename(bot_path.with_name(bot_name))

    inner_bot_path = bot_path / 'bot'
    inner_bot_path.rename(inner_bot_path.with_name(bot_name))


def create_new_bot(bot_name: str) -> None:
    current_path = pathlib.Path.cwd().resolve()

    copy_bot_template(current_path)
    rename_bot_template(current_path, bot_name)


if __name__ == '__main__':
    create_new_bot('testbot')
