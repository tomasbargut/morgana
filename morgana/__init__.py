#!/usr/bin/env python
import os
import click
import collections

APP_NAME = 'morgana'
CONFIG_DIR = click.get_app_dir(APP_NAME)
HISTORY_FILE = os.path.join(CONFIG_DIR,'runner_history')

@click.group()
def cli():
    pass

@cli.command()
def init():
    """
    Initialize the application
    """
    if not os.path.exists(CONFIG_DIR):
        os.mkdir(CONFIG_DIR)

    if not os.path.exists(HISTORY_FILE):
        click.open_file(HISTORY_FILE).close()

@cli.group()
def runner():
    """
    Collection of scripts to help a runner composed by fzf, compgen and swaymsg
    """
    pass

@runner.command()
def sort():
    """
    Take from the stdin the output of compgen and print to stdout the same but ordered by use
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
    Take from stdin the output of fzf | tail -n1, which is the name of a command.
    Store it into the history file and print the name of the command again to be passed to swaymsg
    """
    command = click.get_text_stream('stdin').read()
    click.echo(command)
    with click.open_file(HISTORY_FILE, 'a') as file:
        file.write(command)
    

if __name__ == "__main__":
    cli()
# vim: fileype=py