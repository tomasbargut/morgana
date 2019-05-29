import subprocess

import pytest
from click.testing import CliRunner

from morgana import cli, config

@pytest.mark.parametrize('program',[("firefox")])
def test_runner_store(program, clean_workspace):
    runner = CliRunner()
    result = runner.invoke(cli, ["runner", "store"], input=program)
    assert result.exit_code == 0
    assert "\n" in result.output
    assert result.output.strip() == program
    with open(config.HISTORY_FILE) as f:
        history = f.read()
    history = history.split('\n')
    assert history[-1] == program


def test_runner_store_offset(clean_workspace):
    runner = CliRunner()
    for _ in range(51):
        runner.invoke(cli, ['runner', 'store'], input='firefox')
    with open(config.HISTORY_FILE) as file:
        history = file.read()
    assert len(history.split()) <= 50
    

# @pytest.fixture()
# def compgen():
#     result = subprocess.run('compgen -c')
#     return result.stdout

# def test_runner_sort(compgen):
#     runner = CliRunner()



    