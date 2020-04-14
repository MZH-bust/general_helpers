# -*- coding: utf-8 -*-

import smtplib
from smtplib import SMTPResponseException,SMTPServerDisconnected,SMTPAuthenticationError, SMTPConnectError, \
    SMTPException
from socket import error as socketerror
import mimetypes
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import ntpath


class Connection:
    def __init__(self, host: str, username: str, password: str, port: int = 25, timeout: int = 300):
        self.host = host
        self.username = username
        self.password = password
        self.port = port
        self.timeout = timeout
        self.session = None

    def __repr__(self):
        pass

    def connect(self):
        try:
            self.session = smtplib.SMTP(host=self.host, port=self.port, timeout=self.timeout)
        except (BlockingIOError, socketerror) as err:
            self.session = None
            return err
        self.session.debuglevel = 2
        self.session.ehlo()
        self.session.starttls()
        self.session.ehlo()
        try:
            self.session.login(self.username, self.password)
        except SMTPAuthenticationError:
            print("Login nicht erfolgreich")

    def is_connected(self):
        """

        :return: Gibt zurück, ob eine funktionierende Verbindung zum host besteht.
        :rtype: Bool
        """
        try:
            if self.session and (self.session.noop()[0] == 250):
                return True
        except (SMTPServerDisconnected,SMTPResponseException):
            print("Es ist ein Fehler aufgetreten")
        self.session = None
        return False


