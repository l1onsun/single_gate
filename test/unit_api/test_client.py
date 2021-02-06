from single_gate.unit_api.client import UnitClient


def test_unit_client():
    client = UnitClient("some/path")
    assert client.control_connector._path == "some/path"
