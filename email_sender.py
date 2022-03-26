import smtplib
email = "SENDER_EMAIL"
password = "PASSWORD"
my_email = "RECIEVING_EMAIL"

class EmailSender:
    def __init__(self, message):
        print('sending_email')
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(from_addr=email,
                                to_addrs=my_email,
                                msg=f"subject:Mail Recieved From Your Website\n\n{message}"
                                )
