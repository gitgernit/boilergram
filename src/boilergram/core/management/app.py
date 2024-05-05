import typer

app = typer.Typer(add_completion=False)


@app.command()
def init():
    print('Hello, world!')


if __name__ == "__main__":
    app()
