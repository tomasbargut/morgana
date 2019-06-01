import pytest
from click.testing import CliRunner

from morgana import cli

@pytest.fixture(scope='function')
def clean_runner():
    runner = CliRunner()
    runner.invoke(cli, ['init', '-f'])
    return runner