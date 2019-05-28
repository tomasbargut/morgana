import click
import os

APP_NAME = 'morgana'
CONFIG_DIR = os.path.expanduser(click.get_app_dir(APP_NAME))
HISTORY_FILE = os.path.join(CONFIG_DIR, 'runner_history')
DB_URI = os.path.join(CONFIG_DIR, 'database.db')
CONFIG_FILE = os.path.join(CONFIG_DIR, 'config')

COMMANDS = [
    'backup','init','runner' #DJANGO LIKE
]