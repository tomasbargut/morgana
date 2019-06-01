import os

import click
import collections

from morgana.config import (
    HISTORY_FILE
)

@click.group(name="runner")
def cli():
    """
    Collection of scripts to help a runner composed by fzf, compgen and swaymsg
    """
    pass # pylint: disable=unnecessary-pass


@cli.command()
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


@cli.command()
def store():
    """
    Take from stdin a program name, store it into the history file
    and print the name of the command again to be passed to swaymsg
    """
    command = click.get_text_stream('stdin').read()
    command = command.strip()
    click.echo(command)
    with click.open_file(HISTORY_FILE) as file:
        history = file.read()
    history = history.split('\n')
    history_len = len(history)
    if history_len >=50:
        with click.open_file(HISTORY_FILE,'w') as file:
            file.write("\n".join(history[history_len-49:]))
    with click.open_file(HISTORY_FILE, 'a') as file:
        file.write(f'\n{command}')