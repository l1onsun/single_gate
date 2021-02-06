from aiohttp import UnixConnector

control_connector = UnixConnector(path="/var/run/control.unit.sock")
