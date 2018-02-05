from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

from email.mime.text import MIMEText
from subprocess import Popen, PIPE

fromaddr = "<emailid>"
toaddr = "<emailid>"

msg = MIMEMultipart()

msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "MEDLIFE- Mail Status"

body ="MEDLIFE- Mail Status"

msg.attach(MIMEText(body, 'plain'))

path="<path>"
filename = "hi.txt"
attachment = open(path+filename, "rb")

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(part)
p = Popen(["/usr/sbin/sendmail", "-t", "-oi"], stdin=PIPE)
p.communicate(msg.as_string())
