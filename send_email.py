import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Gmail credentials
username = 'jahnavic910@gmail.com'  # Your Gmail address
password = 'ixzm pqdh jqjp xlci'   # Your App-Specific Password

# User input for recipient's email address
to_email = input("Please enter the recipient's email address: ")

# Set up the email parameters
subject = 'Hello from Python'
body = 'This is an email sent from a Python script!'

# Create a MIME object
msg = MIMEMultipart()
msg['From'] = username
msg['To'] = to_email
msg['Subject'] = subject

# Attach the email body to the MIME object
msg.attach(MIMEText(body, 'plain'))

# Connect to Gmail's SMTP server
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()  # Start TLS encryption
server.login(username, password)  # Log in to the server

# Send the email
server.sendmail(msg['From'], msg['To'], msg.as_string())

# Close the connection
server.quit()

print('Email sent successfully!')
