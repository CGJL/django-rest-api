from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """test api view"""

    def get(self, request, format=None):
        """returns a list of APIView features"""
        an_apiview= [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'is similar to a traditional django view',
            'Gives you the most control over your application logic',
            'is mapped manually to URLs',
        ]

        return Response({'message': 'hello!', 'an_apiview': an_apiview})