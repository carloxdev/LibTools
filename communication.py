# -*- coding: utf-8 -*-

# Python's Libraries
from smtplib import SMTP
from os.path import basename
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate

# Own's Libraries
from data import Error


class Postman(object):

    def __init__(self, _user, _password, _smtp_server, _to_address):
        self.user = _user
        self.password = _password
        self.smtp_server = _smtp_server
        self.to_address = _to_address

    def send_Message(self, subject, text, file_path=""):

        origin = "Postman.send_Message()"

        try:

            from_address = self.user

            msg = MIMEMultipart(
                From=from_address,
                To=self.to_address,
                Date=formatdate(localtime=True),
                Subject=subject
            )

            msg.attach(MIMEText(text))
            msg['Subject'] = subject
            msg['From'] = from_address
            msg['To'] = self.to_address

            if file_path != "":

                msg.attach(MIMEApplication(
                    open(file_path, "rb").read(),
                    Content_Disposition='attachment; filename="{0}"'.format(
                        basename(file_path)),
                    Name=basename(file_path)
                ))

            server = SMTP(self.smtp_server)
            server.login(self.user, self.password)
            dirs = self.to_address.replace(',', ' ')
            destinatario = dirs.split()
            server.sendmail(from_address, destinatario, msg.as_string())
            server.quit()
            print "Envio de Mensaje.......OK"

        except Exception as error:

            print "Envio de Mensaje.......%s" % (str(error))

            raise Error(
                type(error).__name__,
                origin,
                "",
                str(error)
            )

    def send_Gmail_Message(self, subject, text, file_path=""):

        origin = "Postman.send_Gmail_Message()"

        try:

            from_address = self.user

            msg = MIMEMultipart(
                From=from_address,
                To=self.to_address,
                Date=formatdate(localtime=True),
                Subject=subject
            )

            msg.attach(MIMEText(text))
            msg['Subject'] = subject
            msg['From'] = from_address
            msg['To'] = self.to_address

            if file_path != "":

                msg.attach(MIMEApplication(
                    open(file_path, "rb").read(),
                    Content_Disposition='attachment; filename="{0}"'.format(
                        basename(file_path)),
                    Name=basename(file_path)
                ))

            server = SMTP(self.smtp_server)
            server.ehlo()
            server.starttls()
            server.login(self.user, self.password)
            dirs = self.to_address.replace(',', ' ')
            destinatario = dirs.split()
            server.sendmail(from_address, destinatario, msg.as_string())
            server.quit()
            print "Envio de Mensaje.......OK"

        except Exception as error:

            print "Envio de Mensaje.......%s" % (str(error))

            raise Error(
                type(error).__name__,
                origin,
                "",
                str(error)
            )
