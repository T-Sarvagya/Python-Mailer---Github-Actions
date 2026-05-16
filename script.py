import smtplib
from email.mime.text import MIMEText #MIMEText is a class used to create the email content
from email.mime.multipart import MIMEMultipart #MIMEMultipart is a class used to create the email message with multiple parts (e.g., text and attachments)
import os

def send_email(workflow_name, repo_name, workflow_run_id):
    # Email details
    sender_email = os.getenv('SENDER_EMAIL')  # Get sender email from environment variable
    sender_password = os.getenv('SENDER_PASSWORD')  # Get sender password from environment variable
    receiver_email = os.getenv('RECEIVER_EMAIL')  # Get receiver email from environment variable

    # Email message
    subject = f"Workflow '{workflow_name}' Failed in Repository '{repo_name}'"
    body = f"The workflow '{workflow_name}' in the repository '{repo_name}' has failed. Please check the GitHub Actions logs for more details.\n More Details: \nRun_ID: {workflow_run_id}"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try: 
      server = smtplib.SMTP('smtp.gmail.com', 587)  # Use Gmail's SMTP server
      server.starttls()  # Upgrade to a secure connection 
      server.login(sender_email, sender_password)  # Log in to the email account
      text = msg.as_string()  # Convert the message to a string
      server.sendmail(sender_email, receiver_email, text)  # Send the email
      print("Email sent successfully!") 
    except Exception as e:
      print(f"Failed to send email: {e}")

send_email(os.getenv('WORKFLOW_NAME'), os.getenv('REPO_NAME'), os.getenv('WORKFLOW_RUN_ID'))  # Call the function with environment variables