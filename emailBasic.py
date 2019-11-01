import smtplib

email = 'goodshepherdiot@gmail.com' # your email
password = 'P@ssword#1' # your email account password
send_to_email = 'shaecarey7@gmail.com' # recipient
message = 'Yes this is the message' # message in body of email

server = smtplib.SMTP('smtp.gmail.com', 587) # connect to the server
server.starttls() # use TLS (Transport Layer Security)
server.login(email, password)
server.sendmail(email, send_to_email, message)
server.quit()
