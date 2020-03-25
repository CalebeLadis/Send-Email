import smtplib
from email.message import EmailMessage

# Less secure app link to gmail https://myaccount.google.com/lesssecureapps


def connection(email, senha):
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.starttls()
    smtp.ehlo()

    login_status = smtp.login(email, senha)
    return True if login_status[1] == b'2.7.0 Accepted' else False


def send_email(email, senha, subject, body, to):
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(email, senha)

    msg = EmailMessage()
    msg.set_content(body)

    msg['Subject'] = subject
    msg['From'] = email
    msg['To'] = to

    response = smtp.send_message(msg)

    smtp.quit()

    # msg = f'Subject {subject}\n\n{body}'

    print(response)
