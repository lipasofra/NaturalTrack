from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from apps.main.serializers import DisasterListSerializer, DisasterQuerySerializer
from disaster_explorer import query_agent
import json


class DisasterList(generics.ListCreateAPIView):
    serializer_class = DisasterListSerializer
    query_serializer_class = DisasterQuerySerializer
    
    def get(self, request, format=None):
        return Response('api is ready', status=status.HTTP_200_OK)
 
    def post(self, request, format=None):
        serializer = DisasterQuerySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        query = serializer.validated_data['query']

        print(query)

        result = query_agent.run_query(query)
        return Response(result, status=status.HTTP_200_OK)
