from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from rest_framework import viewsets
from profiles_api import models
from rest_framework.authentication import TokenAuthentication
from profiles_api import permissions
from rest_framework import filters

class HelloApiView(APIView):
    """test api view"""

    serializer_class = serializers.HelloSerializer


    def get(self, request, format=None):
        """returns a list of APIView features"""
        an_apiview= [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'is similar to a traditional django view',
            'Gives you the most control over your application logic',
            'is mapped manually to URLs',
        ]

        return Response({'message': 'hello!', 'an_apiview': an_apiview})


    
    def post(self, request):
        """create a hello message with our name"""


        serializer = self.serializer_class(data=request.data)


        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            
    def put(self, request, pk=None):
        """ handle updating an obj"""
        return Response({'method': 'PUT'})
    

    def patch(self,request,pk=None):
        """partial update of an obj """
        return Response({'method': 'PATCH'})


    def delete(self,request,pk=None):
        """delete an obj"""
        return Response({'method':'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """test api ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """return a hello message"""

        a_viewset =[
            'Uses actions (list, create, retrieve, update, partial_update)',
            'automaticallly maps to URLs using Routers',
            'provides more functionality with less code',
        ]

        return Response({'message': 'Hello', 'a_viewset': a_viewset})

    def create(self, request):
        """creates a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!!!!'
        
            return Response({'message': message})
        
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )
    
    def retrieve(self, request, pk=None):
        """handle getting object by id"""
        return Response({'http_method': 'GET'})

     
    def update(self, request, pk=None):
        """handle updating object by id"""
        return Response({'http_method': 'PUT'})

    
    def partial_update(self, request, pk=None):
        """handle partially updating an object by id"""
        return Response({'http_method': 'PATCH'})   


    def destroy(self, request, pk=None):
        """handle deleting object by id"""
        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """handle creating and updating profiles"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends= (filters.SearchFilter,)
    search_fields = ('name', 'email',)