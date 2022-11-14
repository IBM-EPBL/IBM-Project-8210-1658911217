Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # using SendGrid's Python Library
... # https://github.com/sendgrid/sendgrid-python
... import os
... from dotenv import load_dotenv
... 
... load_dotenv()
... from sendgrid import SendGridAPIClient
... from sendgrid.helpers.mail import Mail
... 
... def sendmail(usermail,subject,content):
...     message = Mail(from_email='maryada@student.tce.edu',to_emails=usermail,subject=subject,html_content='<strong> {} </strong>'.format(content))
...     try:
...         sg = SendGridAPIClient(os.getenv('SENDGRID_API_KEY'))
...         response = sg.send(message)
...         print(response.status_code)
...         print(response.body)
...         print(response.headers)
...     except Exception as e:
