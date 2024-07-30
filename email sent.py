#normal mail
##import smtplib
##from email.message import EmailMessage
##
##msg=EmailMessage()
##msg['Subject'] = 'python training'
##msg['From'] = 'srishtykiran111@gmail.com'
##msg['To'] = 'btbts22044_srishti@banasthali.in'
##msg.set_content('d8di31')
##
##server=smtplib.SMTP_SSL('smtp.gmail.com',465)
##server.login('srishtykiran111@gmail.com','skvgqmqkggheulyv')
##server.send_message(msg)
##server.quit()
#send any otp by random 
import smtplib
import random
from email.message import EmailMessage 

p='0123456789qwertyghdiohdiuiophidjbndjkjunjhikj'
otp=random.sample(p,6)
#print(otp)
passs=''.join(otp)
#print(passs)

msg=EmailMessage()
msg['Subject'] = 'python training'
msg['From'] = 'srishtykiran111@gmail.com'
msg['To'] = 'btbts22044_srishti@banasthali.in'
msg.set_content(passs)

server=smtplib.SMTP_SSL('smtp.gmail.com',465)
server.login('srishtykiran111@gmail.com','skvgqmqkggheulyv')
server.send_message(msg)
server.quit()
