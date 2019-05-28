import os
import shutil
import sqlite3

import click

from morgana.config import (
    CONFIG_DIR, DB_URI, HISTORY_FILE
)

@click.command(name="init")
@click.option(
        "-f", '--force', 'force', is_flag=True, help="Force the init process"
)
def cli(force):
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