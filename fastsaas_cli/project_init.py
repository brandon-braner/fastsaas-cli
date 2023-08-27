import typer
from cookiecutter.main import cookiecutter

app = typer.Typer()


@app.command("init")
def project_init(name: str):
    cookiecutter("https://github.com/brandon-braner/fastsaas.git")


if __name__ == "__main__":
    app()
