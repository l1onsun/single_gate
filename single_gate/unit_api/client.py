from aiohttp import UnixConnector


class UnitClient:
    def __init__(self, path="/var/run/control.unit.sock"):
        self.control_connector = UnixConnector(path=path)
