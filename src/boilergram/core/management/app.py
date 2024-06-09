import typer
import asyncio
from boilergram.core.management.inits import create_new_bot

app = typer.Typer(add_completion=False)


@app.command()
def init():
    print('Lets boil-up!')
    bot_name = typer.prompt('Enter the name of your bot')
    create_new_bot(bot_name)


@app.command()
def ping():
    print('pong!')


if __name__ == "__main__":
    app()
