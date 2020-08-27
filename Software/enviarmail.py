from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def mail(mensaje, asunto):
    # create message object instance
    msg = MIMEMultipart()
          
    message = mensaje
     
    # setup the parameters of the message
    password = "26011995Enzo"
    msg['From'] = "muthadorcoc@gmail.com"
    msg['To'] = "muthadorgaming@gmail.com"
    msg['Subject'] = asunto
     
    # add in the message body
    msg.attach(MIMEText(message, 'plain'))
     
    #create server
    server = smtplib.SMTP('smtp.gmail.com: 587')
     
    server.starttls()
     
    # Login Credentials for sending the mail
    server.login(msg['From'], password)
     
     
    # send the message via the server.
    server.sendmail(msg['From'], msg['To'], msg.as_string())
     
    server.quit()
    
    print ("successfully sent email to: %s", msg['To'])