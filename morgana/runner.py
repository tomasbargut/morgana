import os

import click
import collections

@click.group(name="runner")
def cli():
    """
    Collection of scripts to help a runner composed by fzf, compgen and swaymsg
    """
    pass # pylint: disable=unnecessary-pass


@cli.command()
@click.pass_obj
def sort(ctx):
    """
    Take from the stdin the compgen output
    and print it to stdout ordered by use
    """
    HISTORY_FILE = ctx.obj['HISTORY_FILE']
    commands = click.get_text_stream('stdin').read().split('\n')
    with click.open_file(os.path.expanduser(HISTORY_FILE), 'r+') as file:
        history = file.read().split('\n')
    commands += history
    commands = collections.Counter(commands)
    for command, _ in commands.most_common():
        click.echo(command)


@cli.command()
@click.pass_context
def store(ctx):
    """
    Take from stdin a program name, store it into the history file
    and print the name of the command again to be passed to swaymsg
    """
    HISTORY_FILE = ctx.obj['HISTORY_FILE']
    command = click.get_text_stream('stdin').read()
    click.echo(command)
    with click.open_file(HISTORY_FILE, 'a') as file:
        file.write(command)