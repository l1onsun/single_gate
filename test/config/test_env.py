from single_gate.config.env import get_env


def test_get_env():
    assert get_env() == {}
