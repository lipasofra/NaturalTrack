from rest_framework import serializers

class DisasterListSerializer(serializers.Serializer):
    pass

class DisasterQuerySerializer(serializers.Serializer):
    query = serializers.CharField(max_length=10000)

class DisasterEmailSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=10000)