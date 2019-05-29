import pytest
from click.testing import CliRunner

from morgana import cli

@pytest.fixture
def clean_workspace():
    runner = CliRunner()
    runner.invoke(cli, 'init', '-f')