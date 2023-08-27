import typer

app = typer.Typer()


@app.command("module")
def module(name: str):
    typer.echo(f"Hello module {name}!")


if __name__ == "__main__":
    app()
