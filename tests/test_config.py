
import pytest

from morgana.config import Config

def test_config_singleton(norm_conf):
    assert Config()._dict is Config()._dict

# pylint: skip-file