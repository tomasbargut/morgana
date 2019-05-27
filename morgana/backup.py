import click

@click.group(name="backup")
def cli():
    pass # pylint: disable=unnecessary-pass


@cli.command()
@click.argument('file')
def store():
    pass