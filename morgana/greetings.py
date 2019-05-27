import click

@click.command(name="greetings")
def cli():
    click.echo("Hi")