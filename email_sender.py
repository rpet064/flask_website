import smtplib
email = "Pencilcasetester@gmail.com"
password = "xGE81tW3b#$azA"
my_email = "rpether@hotmail.co.nz"


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
