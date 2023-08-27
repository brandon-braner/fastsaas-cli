import typer
from fastsaas_cli.generators import app as generators_app
from fastsaas_cli.project_init import app as project_init_app

app = typer.Typer()

app.add_typer(generators_app, name="generate")
app.add_typer(project_init_app, name="init")


@app.command()
def hello(name: str):
    typer.echo(f"Hello {name}!")


if __name__ == "__main__":
    app()
