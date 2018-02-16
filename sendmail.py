import smtplib
from email.MIMEMultipart import MIMEMultipart from email.MIMEText import MIMEText from email.MIMEBase import MIMEBase from email import encoders

from email.mime.text import MIMEText
from subprocess import Popen, PIPE


class rmail():

  def __init__(self):
  	fromaddr="name@email.com"
  	toaddr="name@email.com"
  	subject=" Mail Status"
  	body=" Mail Status"
  	path="path"
  	filename="hi.txt"
        self.sendmail(fromaddr,toaddr,subject,body,path,filename) 
 
  def sendmail(self,fromaddr,toaddr,subject,body,path,filename):

 
  	msg = MIMEMultipart('alternative')
 
	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = subject
 
	email_content = """
	<head>
  	<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  	<title>Mail Status</title>
        <style type="text/css" media="screen">
    	table{
        background-color: #AAD373;
        empty-cells:hide;
    	}
    	td.cell{
        background-color: white;
    	}
  	</style>
	</head>
	<body>
	<p>Hi!<br>
        Here is the Status<br>
	</body>
	"""
	msg.attach(MIMEText(email_content, 'html'))

	attachment = open(path+filename, "rb")
 
	part = MIMEBase('application', 'octet-stream')
	part.set_payload((attachment).read())
	encoders.encode_base64(part)
	part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
	msg.attach(part)
	p = Popen(["/usr/sbin/sendmail", "-t", "-oi"], stdin=PIPE)
	p.communicate(msg.as_string())
        
def main():
  
       # sendmail(fromaddr,toaddr,subject,body,path,filename) 

        rmail()

if __name__ == '__main__':
      main()
	
#	mail.sendmail(fromaddr,toaddr,subject,body,path,filename)
