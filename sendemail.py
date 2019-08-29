
# Python code to illustrate Sending mail from  
# your Gmail account  
import smtplib 
  
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 

s.ehlo()  
# start TLS for security 
s.starttls() 
# Authentication 
s.login("xxxx", 'xxx') 
# message to be sent 
message = "AWS instance shutdown properly"
# sending the mail 
s.sendmail("xxxxx", "xxxxx", message) 
# terminating the session 
s.quit() 

