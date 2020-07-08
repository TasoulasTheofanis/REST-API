from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from api import serializers #from the folder api, include the serializers.py file
from api import models
from api import permissions

class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        an_apiview = [ #a list of messages to show up
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
        ]
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    serializer_class = serializers.HelloSerializer #this configures that we have a serializer

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data) #retrieve the serializer class, the data are passed as a reuest
        if serializer.is_valid():
            name = serializer.validated_data.get('name') #check if the data is the correct type (in serializers.py we defined name to be Char with max_length=10)
            age = serializer.validated_data.get('age')
            message = f'Hello {name}, you are {age} years old'
            return Response({'message':message}) #return a dictionary
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST ) #in case of a bad request

    def put(self, request, pk=None):
        """Fully updating an object (all of its fields)"""
        return Response({'method:': 'PUT'})

    def patch(self, request, pk=None):
        """partial update of an object (some fields)"""
        return Response({'method': 'PATCH'})

    def delete (self, request, pk=None):
        """Delete object"""
        return Response({'method': 'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        a_viewset = [
            'User actions (lists, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using routers',
            'Provides more functionallity with less code',
        ]
        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            age = serializer.validated_data.get('age')
            message = f'Hello {name}, you are {age} years old!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object by its Primary Key"""
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """ Update objects """
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Partially Update objects"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Remove object"""
        return Response({'http_method': 'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)

class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
