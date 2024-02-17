import typer

app = typer.Typer()


@app.command()
def keygen() -> None:
    typer.echo("Implement your keygen for crackme_659fde9deef082e477ff59ba here.")


if __name__ == "__main__":
    app()
