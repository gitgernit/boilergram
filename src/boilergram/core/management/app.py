import pathlib

from rich import print as rprint
import typer

from boilergram.core.management.inits import copy_bot_template
from boilergram.core.management.inits import rename_bot_template

app = typer.Typer(add_completion=False)


@app.command()
def init() -> None:
    rprint('Lets boil-up!')
    bot_name = typer.prompt('Enter the name of your bot')

    current_path = pathlib.Path.cwd().resolve()

    copy_bot_template(current_path)
    rename_bot_template(current_path, bot_name)


@app.command()
def ping() -> None:
    rprint('pong!')


if __name__ == '__main__':
    app()
