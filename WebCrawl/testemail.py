import smtplib

fromaddr = "aliertest238@gmail.com"
password = "aliertest"

server = smtplib.SMTP('smtp.gmail.com', 587)
 
def LoginEmail():
	global server
	server.ehlo()
	server.starttls()
	server.ehlo()
	server.login(fromaddr,password)

def sendEmail(text):
	global server
	server.sendmail(fromaddr, toaddr, text)

LoginEmail()
i=1
while i < 3 :
	i += 1
	sendEmail("text")
	time.sleep(5)
