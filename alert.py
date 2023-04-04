import smtplib
from email.message import EmailMessage

def alert_mail():
        email_id = 'spidyscraper@gmail.com'
        password = 'spidy420'
        msg = EmailMessage()
        msg['Subject'] = 'Price dropped'
        msg['From'] = email_id
        msg['To'] = 'aryanbharti9.9@gmail.com'
        msg.set_content("Hi, The price of product is drooped link")
        with smtplib.SMTP_SSL('smtp.gmail.com',587) as smtp:
            smtp.login(email_id,password)
            smtp.send_message(msg)
            print('Mail Sent')
            smtp.quit()