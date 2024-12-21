import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from os.path import basename

def send_email(job_title, recipient_email):
    # Define email content and attachments based on job title
    email_content = {
        'Data Analyst': {
            'subject': 'Application for Data Analyst Position',
            'body': 'I am excited to apply for the Data Analyst position. Attached is my resume.',
            'attachment': 'Data_Analyst_Resume.pdf'
        },
        'Data Engineer': {
            'subject': 'Application for Data Engineer Position',
            'body': 'Please find attached my resume for the Data Engineer position.',
            'attachment': 'Data_Engineer_Resume.pdf'
        },
        'ML Engineer': {
            'subject': 'Interest in ML Engineer Role',
            'body': 'I have attached my resume for the ML Engineer position.',
            'attachment': 'ML_Engineer_Resume.pdf'
        },
        'Data Scientist': {
            'subject': 'Data Scientist Position Application',
            'body': 'Attached is my resume for the Data Scientist position.',
            'attachment': 'Data_Scientist_Resume.pdf'
        }
    }

    content = email_content.get(job_title, email_content['Data Analyst'])  # Default to Data Analyst if not found

    # Gmail credentials
    username = 'jahnavic910@gmail.com'  # Your Gmail address
    password = 'ixzm pqdh jqjp xlci'    # Your App-Specific Password

    # Set up the email
    msg = MIMEMultipart()
    msg['From'] = username
    msg['To'] = recipient_email
    msg['Subject'] = content['subject']
    msg.attach(MIMEText(content['body'], 'plain'))

    # Attach the PDF file specified
    pdf_path = r'C:\Users\Hp\OneDrive\Desktop\Coursework\SP\sp3\\' + content["attachment"]
    with open(pdf_path, "rb") as f:
        attach = MIMEApplication(f.read(), _subtype="pdf")
        attach.add_header('Content-Disposition', 'attachment', filename=basename(pdf_path))
        msg.attach(attach)

    # Connect to SMTP server and send the email
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(username, password)
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()

    print('Email sent successfully!')

# Example usage
if __name__ == "__main__":
    job_title = input("Enter the job title: ")
    recipient_email = input("Enter the recipient's email address: ")
    send_email(job_title, recipient_email)
