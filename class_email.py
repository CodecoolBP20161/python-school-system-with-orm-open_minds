class Email:

    def __init__(self, **kwargs):
        self.user = None
        self.pwd = None
        self.to = None
        self.subject = None
        self.body = None

        for key, value in kwargs.items():
            setattr(self, key, value)

    def email_sender(self):
        import smtplib

        self.to = self.to if type(self.to) is list else [self.to]

        # Prepare message
        message = """From: %s\nTo: %s\nSubject: %s\n\n%s
       """ % (self.user, ", ".join(self.to), self.subject, self.body)
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo()
            server.starttls()
            server.login(self.user, self.pwd)
            server.sendmail(self.user, self.to, message)
            server.close()
        except:
            print("Failed to send the email.")
