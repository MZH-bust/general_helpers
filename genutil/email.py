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
    def __init__(self, host: str, username: str, password: str,
                 port: int = 25, timeout: int = 300, debuglevel: int = 0):
        self.host = host
        self.username = username
        self.password = password
        self.port = port
        self.timeout = timeout
        self.debuglevel = debuglevel
        self.session = None

    def __repr__(self):
        pass

    def connect(self):
        """
        Stellt die Verbindung her und führt den Login durch.
        :return:
        :rtype:
        """
        try:
            self.session = smtplib.SMTP(host=self.host, port=self.port, timeout=self.timeout)
        except (BlockingIOError, socketerror, SMTPException) as err:
            self.session = None
            print(f"Es ist ein Fehler aufgetreten: {err}")
        self.session.debuglevel = self.debuglevel
        self.session.ehlo()
        self.session.starttls()
        self.session.ehlo()
        try:
            self.session.login(self.username, self.password)
        except SMTPAuthenticationError:
            print("SMTP Login nicht erfolgreich")

    def is_connected(self):
        """

        :return: Gibt zurück, ob eine funktionierende Verbindung zum host besteht.
        :rtype: Bool
        """
        try:
            if self.session and (self.session.noop()[0] == 250):
                return True
        except (SMTPServerDisconnected,SMTPResponseException, SMTPException):
            print("Es ist ein Fehler aufgetreten")
        self.session = None
        return False

    def send(self):
        self.session.sendmail(from_addr=self.username, )


class Message:
    def __init__(self, subject: str, text: str = None, html: str = None,
                 to_list: list = None, cc_list: list = None, attachments=None):
        self.all_recipients = None
        self.to_list = to_list
        self.cc_list = cc_list
        self.msg = MIMEMultipart()
        self.set_msg_body(text, html, attachments)
        self.set_msg_recipients()
        print("stop")

    def __repr__(self):
        pass

    def set_msg_body(self, text, html, attachments):
        if not html and not attachments:
            # Simple plain text email
            self.msg = MIMEText(text,'plain', 'utf-8')
        else:
            # Multipart message
            self.msg = MIMEMultipart()
            if html:
                # Add html & plain text alernative parts
                alt = MIMEMultipart('alternative')
                alt.attach(MIMEText(text,'plain', 'utf-8'))
                alt.attach(MIMEText(html,'html', 'utf-8'))
                self.msg.attach(alt)
            else:
                # Just add plain text part
                txt = MIMEText(text,'plain', 'utf-8')
                self.msg.attach(txt)

    def set_msg_recipients(self):
        self.all_recipients = []
        self.to_list and self.add_recipient_type("To", self.to_list)
        self.cc_list and self.add_recipient_type("Cc", self.cc_list)

    def add_recipient_type(self, recipient_type: str, recipient_list: list):
        """

        :param recipient_type: String, welcher Empfängertyp gemeint ist. Optionen: "To" oder "Cc"
        :type recipient_type: str
        :param recipient_list: Liste mit den Empfänger E-Mail Adressen zum jeweiligen Empfängertyp
        :type recipient_list: list
        :raise ValueError, falls ein nicht unterstützter Empfängertyp angegeben wird.
        """
        if recipient_type not in ["To", "Cc"]:
            raise ValueError(f"Nicht unterstützter Empfängertyp: {recipient_type}")
        unique_recipient_list = list(set(recipient_list))
        self.all_recipients += unique_recipient_list
        self.msg[recipient_type] = ', '.join(unique_recipient_list)



