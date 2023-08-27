import typer
from .module.module import app as module_app

app = typer.Typer()

app.add_typer(module_app, name="module")

if __name__ == "__main__":
    app()
