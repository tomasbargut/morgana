"""
A collection of awesome scripts (inho)
"""
import os
import shutil
import collections
import sqlite3
import click
import importlib

from morgana.config import COMMANDS

@click.group()
def cli():
    """
    Main entry for the applicaction
    """
    pass    

for command in COMMANDS:
    module_name = f'morgana.{command}'
    module = importlib.import_module(module_name)
    cli.add_command(module.cli)
