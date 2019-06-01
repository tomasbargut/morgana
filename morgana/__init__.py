"""
A collection of awesome scripts (inho)
"""
import collections
import importlib
import os
import shutil
import sqlite3

import click

from morgana.config import COMMANDS


@click.group()
def cli():
    """
    Main entry for the applicaction
    """
    pass # pylint: disable= unnecessary-pass

for command in COMMANDS:
    module_name = f'morgana.{command}'
    module = importlib.import_module(module_name)
    cli.add_command(module.cli)
