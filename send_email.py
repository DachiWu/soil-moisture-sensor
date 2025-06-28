import smtplib
from email.message import EmailMessage

from_email_addr = "1354267684@qq.com"
from_email_pass = "zbivegopkacvffbd"
to_email_addr = "1354267684@qq.com"

msg = EmailMessage()
body = "Hello from Raspberry Pi"
msg.set_content(body)

msg['From'] = from_email_addr
msg['To'] = to_email_addr
msg['Subject'] = 'TEST EMAIL FROM RASPBERRY PI'

server = smtplib.SMTP('smtp.qq.com', 587)
server.starttls()
server.login(from_email_addr, from_email_pass)
server.send_message(msg)

print('Email sent')

server.quit()
