#!/usr/bin/env python
import smtplib
import email.message

class EmailForwarder:
    # Init SMTP info for forwarding
    def __init__(self, email_address, password, smtp_host, smtp_port):
        self.email_address = email_address
        self.password = password

        self.smtp_host = smtp_host
        self.smtp_port = smtp_port

    def forward(self, email_message, recipient):
        message = email.message_from_string(email_message)

        # replace headers (could do other processing here)
        message.replace_header("From", self.email_address)
        message.replace_header("To", recipient)
        message.replace_header("Subject", "Fwd: " + message["subject"])

        #header = 'To:' + recipient + '\r\n' + 'From: ' + self.email_address + '\r\n' + 'Subject:' + "Fwd: " + message["subject"] + '\r\n'

        # open authenticated SMTP connection and send message with
        # specified envelope from and to addresses
        smtp = smtplib.SMTP(self.smtp_host, self.smtp_port)
        smtp.starttls()
        smtp.login(self.email_address, self.password)
        #smtp.sendmail(self.email_address, recipient, header + '\r\n' + message.as_string())
        smtp.sendmail(self.email_address, recipient, message.as_string())
        smtp.quit()
