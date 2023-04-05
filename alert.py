import smtplib
from email.message import EmailMessage

def alert_mail(title, price, email_addr,link):
        email_id = 'spidyscraper@gmail.com'
        password = '#####' #Password
        msg = EmailMessage()
        msg['Subject'] = 'Price dropped'
        msg['From'] = email_id
        msg['To'] = email_addr
        msg.set_contentprint(f"Hi, The price of {title} is drooped to {price}.\n Link: {link}")
        with smtplib.SMTP_SSL('smtp.gmail.com',587) as smtp:
            smtp.login(email_id,password)
            smtp.send_message(msg)
            print('Mail Sent')
            smtp.quit()
