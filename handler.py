""" connection handler """

from netmiko import ConnectHandler


class Handler:
    """ base connection handler class """

    def __init__(self, **kwargs):
        """ constructor """

        self._conn = ConnectHandler(**kwargs)

    def send(self, command):
        """ send command to host """

        # prevent device config changes
        if not command.startswith('show'):
            raise ValueError('Config changes are not supported !')

        return self._conn.send_command(command)

    def disconnect(self):
        """ close connection """

        self._conn.disconnect()

    def __enter__(self):
        """ enter context manager """

        return  self

    def __exit__(self, exc_type, exc_value, exc_tb):
        """ exit context manager """

        self._conn.disconnect()
