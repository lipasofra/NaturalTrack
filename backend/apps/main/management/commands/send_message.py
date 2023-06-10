import json
from django.core.management.base import BaseCommand
from pprint import pprint
from django.contrib.auth.models import Group, Permission
import csv
from apps.main.models import disasters19002021, disasters19702021, Disasters
from utils import read_csv
from pprint import pprint
from heyoo import WhatsApp
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.conf import settings
from utils import render_output_filtered
from disaster_explorer import query_agent
import random

class Command(BaseCommand):
    help = 'Import disasters from CSV file'

    def handle(self, *args, **options):
        fail = False
        email = 'andres-yoyo@hotmail.com'

        from_email = settings.EMAIL_HOST_USER
        to_email = email

        years = [1900, 2021]
        random_year = random.randint(years[0], years[1])

        message = query_agent.run_query(
            query=f'give me an curious fact of the disasters that happened in the year {random_year}, give this to the user like if he is going to read a newsletter',
        )

        # Create the email message
        email = MIMEMultipart()
        email['From'] = from_email
        email['To'] = to_email
        email['Subject'] = 'climatic disasters'

        # Attach the message to the email
        email.attach(MIMEText(message, 'plain'))
        try:
            # Connect to the SMTP server and send the email
            smtp_server = smtplib.SMTP('smtp.gmail.com', 587)  # Replace with your SMTP server details
            smtp_server.starttls()
            smtp_server.login(settings.EMAIL_HOST_USER, settings.EMAIL_PASSWORD)  # Replace with your email login credentials
            smtp_server.send_message(email)
            smtp_server.quit()
        except Exception as e:
            print(f'Error sending email: {e}')
            fail = True

        return fail



        

