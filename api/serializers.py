from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testiong our APIView"""
    name = serializers.CharField(max_length=10)
    age =  serializers.IntegerField(max_value=120, min_value=0)
