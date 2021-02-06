from single_gate.asgi import index


def test_index():
    assert index() == {"single": "gate"}
