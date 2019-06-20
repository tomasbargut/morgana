import subprocess

import pytest

from morgana import cli, config

@pytest.mark.parametrize('program',[("firefox")])
def test_runner_store(program, clean_runner, norm_conf):
    result = clean_runner.invoke(cli, ["runner", "store"], input=program)
    result = clean_runner.invoke(cli, ["runner", "store"], input=program)
    assert result.exit_code == 0
    assert "\n" in result.output
    assert result.output.strip('\n') == program
    with open(config.HISTORY_FILE) as file:
        history = file.read()
    history = history.split('\n')
    assert history[-1] == program


def test_runner_store_offset(clean_runner, norm_conf):
    for _ in range(norm_conf['history_size'] + 1):
        clean_runner.invoke(cli, ['runner', 'store'], input='firefox')
    with open(config.HISTORY_FILE) as file:
        history = file.read()
    assert len(history.split('\n')) == norm_conf['history_size']
    

@pytest.fixture()
def compgen():
    result = subprocess.check_output(['/bin/bash', '-c', 'compgen -c'])
    return result

@pytest.mark.parametrize(
    'history,expected_result', [
        (['firefox\n'] * 3 + ['spotify\n'] * 2, ['firefox', 'spotify']),
        (['firefox\n'] * 3, ['firefox'])
    ]
)
def test_runner_sort(compgen, clean_runner, history, expected_result, norm_conf):
    with open(config.HISTORY_FILE, 'a') as file:
        file.writelines(history)
    result = clean_runner.invoke(cli, ['runner', 'sort'], input=compgen)
    result = result.output.split('\n')
    for i, item in enumerate(expected_result):
        assert item == result[i]
        
# pylint: skip-file 