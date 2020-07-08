from rest_framework import serializers
from api import models

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testiong our APIView"""
    name = serializers.CharField(max_length=10)
    age =  serializers.IntegerField(max_value=120, min_value=0)

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta: #configures the serializer to point to a specific model in our project site
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True, #we dont want the password to be shown
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email = validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password']
        )
        return user
