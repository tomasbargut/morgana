"""
A collection of awesome scripts (inho)
"""
import os
import shutil
import collections
import sqlite3
import click
import importlib

COMMANDS = [
    'backup','init','runner' #DJANGO LIKE
]

@click.group()
@click.pass_context
def cli(ctx):
    """
    Main entry for the applicaction
    """
    ctx.ensure_object(dict)
    ctx.obj['APP_NAME'] = 'morgana'
    ctx.obj['CONFIG_DIR'] = click.get_app_dir(ctx.obj['APP_NAME'])
    ctx.obj['HISTORY_FILE'] = os.path.join(ctx.obj['CONFIG_DIR'], 'runner_history')
    ctx.obj['DB_URI'] = os.path.join(ctx.obj['CONFIG_DIR'], 'database.db')

for command in COMMANDS:
    module_name = f'morgana.{command}'
    module = importlib.import_module(module_name)
    cli.add_command(module.cli)
