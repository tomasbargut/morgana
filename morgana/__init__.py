"""
A collection of awesome scripts (inho)
"""
import os
import shutil
import collections
import sqlite3
import click

APP_NAME = 'morgana'
CONFIG_DIR = click.get_app_dir(APP_NAME)
HISTORY_FILE = os.path.join(CONFIG_DIR, 'runner_history')
DB_URI = os.path.join(CONFIG_DIR, 'database.db')


@click.group()
def cli():
    """
    Main entry for the applicaction
    """
    pass # pylint: disable=unnecessary-pass


@cli.command()
@click.option(
        "-f", '--force', 'force', is_flag=True, help="Force the init process"
)
def init(force):
    """
    Initialize the application
    """
    config_dir_exists = os.path.exists(CONFIG_DIR)
    if config_dir_exists and force:
        shutil.rmtree(CONFIG_DIR)
    if not os.path.exists(CONFIG_DIR):
        os.mkdir(CONFIG_DIR)

    if not os.path.exists(HISTORY_FILE):
        click.open_file(HISTORY_FILE, 'a').close()

    sqlite3.connect(DB_URI).close()



@cli.group()
def runner():
    """
    Collection of scripts to help a runner composed by fzf, compgen and swaymsg
    """
    pass # pylint: disable=unnecessary-pass


@runner.command()
def sort():
    """
    Take from the stdin the compgen output
    and print it to stdout ordered by use
    """
    commands = click.get_text_stream('stdin').read().split('\n')
    with click.open_file(os.path.expanduser(HISTORY_FILE), 'r+') as file:
        history = file.read().split('\n')
    commands += history
    commands = collections.Counter(commands)
    for command, _ in commands.most_common():
        click.echo(command)


@runner.command()
def store():
    """
    Take from stdin a program name, store it into the history file
    and print the name of the command again to be passed to swaymsg
    """
    command = click.get_text_stream('stdin').read()
    click.echo(command)
    with click.open_file(HISTORY_FILE, 'a') as file:
        file.write(command)


if __name__ == "__main__":
    cli()
