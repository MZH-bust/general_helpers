import pytest
from pytest_socket import disable_socket, enable_socket
from smtplib import SMTPConnectError
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
        assert connection.is_connected() is False

        connection.timeout = 300
        connection.host = "Nonexistinghost"
        assert connection.is_connected() is False


class TestMessageClass:
    @pytest.fixture
    def textmessage_noattachment(self):
        self.messageconfig = config.data.message
        return email.Message(subject=self.messageconfig.subject,
                             text=self.messageconfig.text,
                             to_list=self.messageconfig.to_list,
                             cc_list=self.messageconfig.cc_list)

    def test_constructor(self, textmessage_noattachment):
        assert set(textmessage_noattachment.all_recipients) == set(self.messageconfig.to_list +
                                                                   self.messageconfig.cc_list)