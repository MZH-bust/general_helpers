import pytest
from pytest_socket import disable_socket, enable_socket
from socket import error as socketerror
from genutil import email
from tests.config import config


class TestEmailConnection:

    @pytest.fixture
    def connection(self):
        self.mailconfig = config.data.email
        return email.Connection(host=self.mailconfig.host,
                                username=self.mailconfig.username,
                                password=self.mailconfig.password)

    def test_constructor(self, connection):
        assert isinstance(connection, email.Connection)
        assert all([connection.host == self.mailconfig.host,
                   connection.username == self.mailconfig.username,
                    connection.password == self.mailconfig.password,
                    connection.port == 25,
                    connection.timeout == 300])

    def test_connect(self, connection):
        connection.connect()
        assert str(type(connection.session)) == "<class 'smtplib.SMTP'>"
        assert connection.is_connected() is True

    def test_connect_fails(self, connection):
        connection.timeout = 0
        isinstance(connection.connect(), BlockingIOError)
        connection.timeout = 300
        connection.host = "Nonexistinghost"
        isinstance(connection.connect(), socketerror)
        assert connection.is_connected() is False
