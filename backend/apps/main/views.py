from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from apps.main.serializers import DisasterListSerializer, DisasterQuerySerializer, DisasterEmailSerializer
from disaster_explorer import query_agent
from django.conf import settings
import random
import json
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class DisasterList(generics.ListCreateAPIView):
    serializer_class = DisasterListSerializer
    query_serializer_class = DisasterQuerySerializer
    
    def get(self, request, format=None):
        return Response('api is ready', status=status.HTTP_200_OK)
 
    def post(self, request, format=None):
        serializer = DisasterQuerySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        query = serializer.validated_data['query']

        result = query_agent.run_query(query)
        return Response(result, status=status.HTTP_200_OK)


class DisasterEmail(generics.ListCreateAPIView):
    serializer_class = DisasterListSerializer
    query_serializer_class = DisasterQuerySerializer

    

    
    def get(self, request, format=None):
        return Response('api email is ready', status=status.HTTP_200_OK)
 
    def post(self, request, format=None):
        serializer = DisasterEmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']

        response = self.send_message(email)

        if response is False:
            return Response('email sent', status=status.HTTP_200_OK)

        return Response('email not sent', status=status.HTTP_400_BAD_REQUEST) 
    
    def send_message(self, email):
        email_host_user= os.getenv("EMAIL_HOST_USER")
        email_password= os.getenv("EMAIL_PASSWORD")
        
        fail = False
        from_email = email_host_user
        to_email = email

        years = [1900, 2008]
        random_year = random.randint(years[0], years[1])

        message = query_agent.run_query(
            query=f'give me an curious fact of the disasters that happened in the year {random_year}, give this to the user like if he is going to read a newsletter',
        )

        if message is None:
            message = 'no data this time, keep trying'

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
            smtp_server.login(email_host_user, email_password)  # Replace with your email login credentials
            smtp_server.send_message(email)
            smtp_server.quit()
            return False
        except Exception as e:
            print(f'Error sending email: {e}')
            return True
        