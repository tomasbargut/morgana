"""Config module"""
import os
import click
import yaml
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


APP_NAME = 'morgana'
CONFIG_DIR = os.path.expanduser(click.get_app_dir(APP_NAME))
HISTORY_FILE = os.path.join(CONFIG_DIR, 'runner_history')
DB_URI = os.path.join(CONFIG_DIR, 'database.db')
CONFIG_FILE = os.path.join(CONFIG_DIR, 'config.yml')

COMMANDS = [
    'backup', 'init', 'runner' #DJANGO LIKE
]

class Config:
    """
    Config class
    """
    _dict = {}

    def __init__(self):
        if not Config._dict:
            with open(CONFIG_FILE) as file:
                Config._dict = yaml.load(stream=file, Loader=Loader)

    def __getitem__(self, key):
        return self._dict[key]

    def __setitem__(self, key, value):
        self._dict[key] = value
