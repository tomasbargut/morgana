import pytest
from click.testing import CliRunner

from morgana import cli

@pytest.fixture
def clickrunner():
    return CliRunner()