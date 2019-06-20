import pytest
from click.testing import CliRunner

from morgana import cli
from morgana.config import (
    Config, CONFIG_FILE
)
import yaml

try:
    from yaml import CDumper as Dumper
except ImportError:
    from yaml import Dumper

@pytest.fixture(scope='function')
def clean_runner():
    runner = CliRunner()
    runner.invoke(cli, ['init', '-f'])
    return runner

@pytest.fixture(scope='function')
def norm_conf():
    conf = {
        'history_size': 50
    }
    yaml.dump(conf, open(CONFIG_FILE, 'w+'), Dumper=Dumper)
    conf = Config()
    return conf

# pylint: skip-file