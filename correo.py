import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def correo(mail_content, receiver_address, asunto):

    sender_address = 'pon_tu_correo'
    sender_pass = 'pon_tu_contra'


    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = asunto
    # The subject line

    adjunto = MIMEBase("application", "octect-stream")

    archivo_adjunto = open("John_Cornejo_Curriculum.pdf", 'rb')

    adjunto.set_payload((archivo_adjunto).read())

    encoders.encode_base64(adjunto)

    adjunto.add_header("content-Disposition", 'attachment; filename="JohnCornejoVital.pdf"')
    message.attach(adjunto)

    # The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    # Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
    session.starttls()  # enable security
    session.login(sender_address, sender_pass)  # login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('correo enviado', receiver_address)


