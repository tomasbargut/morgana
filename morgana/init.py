import os
import shutil
import sqlite3

import click

@click.command(name="init")
@click.option(
        "-f", '--force', 'force', is_flag=True, help="Force the init process"
)
@click.pass_context
def cli(ctx,force):
    """
    Initialize the application
    """
    CONFIG_DIR = ctx.obj['CONFIG_DIR']
    HISTORY_FILE = ctx.obj['HISTORY_FILE']
    DB_URI = ctx.obj['DB_URI']

    config_dir_exists = os.path.exists(CONFIG_DIR)
    if config_dir_exists and force:
        shutil.rmtree(CONFIG_DIR)

    if not os.path.exists(CONFIG_DIR):
        os.mkdir(CONFIG_DIR)

    if not os.path.exists(HISTORY_FILE):
        click.open_file(HISTORY_FILE, 'a').close()

    sqlite3.connect(DB_URI).close()