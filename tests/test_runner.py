import subprocess

import pytest
from click.testing import CliRunner

from morgana import cli, config

@pytest.mark.parametrize('program',[("firefox")])
def test_runner_store(program):
    runner = CliRunner()
    result = runner.invoke(cli, ["runner", "store"], input=program)
    assert result.exit_code == 0
    assert result.output.strip() == program
    with open(config.HISTORY_FILE) as f:
        history = f.read()
    history = history.split('\n')
    assert history[-1] == program
    

# @pytest.fixture()
# def compgen():
#     result = subprocess.run('compgen -c')
#     return result.stdout

# def test_runner_sort(compgen):
#     runner = CliRunner()



    