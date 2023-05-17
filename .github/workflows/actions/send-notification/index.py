import smtplib

def send_notification(release_tag):
    # Customize the email settings
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    sender_email = 'pyjulia.3.8@gmail.com'
    receiver_email = 'stefanarsic2002@gmail.com'
    subject = f'New release: {release_tag}'
    message = f'A new release with tag {release_tag} has been published.'

    # Connect to the SMTP server and send the email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, 'pyjulia.010.')
        server.sendmail(sender_email, receiver_email, f'Subject: {subject}\n\n{message}')

# Get the release tag input from the workflow
# release_tag = input('release_tag')

# Set the release tag directly
release_tag = 'v1.0.0'  # Replace with the desired release tag

# Send the notification
send_notification(release_tag)
