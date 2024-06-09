import shutil
import pathlib


def copy_bot_template(target_dir):
    template_path = (pathlib.Path(__file__).parent.parent / 'templates').resolve()

    shutil.copytree(template_path, target_dir, dirs_exist_ok=True)


def rename_bot_template(template_parent_dir, bot_name):
    bot_path = template_parent_dir / 'bot'

    bot_path = bot_path.rename(bot_name).resolve()

    inner_bot_path = bot_path / 'bot'
    inner_bot_path.rename(bot_path / bot_name)


def create_new_bot(bot_name):
    current_path = pathlib.Path.cwd().resolve()

    copy_bot_template(current_path)
    rename_bot_template(current_path, bot_name)
