from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from ..users.models import User
from .serializers import UserSerializer
from .paginators import UserPagination
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import mixins
from rest_framework import generics
from rest_framework.exceptions import NotAuthenticated
from rest_framework.permissions import IsAuthenticated

class user_list(generics.ListAPIView):
    """
    Cenutrio
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #def get(self, request, format=None):
    #    return self.list(request, *args, **kwargs)

    #def post(self, request, format=None):
    #    serializer = UserSerializer(data=request.data)
    #    if serializer.is_valid():
    #        serializer.save()
    #        return Response(serializer.data, status=status.HTTP_201_CREATED)
    #    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class register(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class login(APIView):
    def post(self, request, format=None):
        return Response("OK")
    

class logout(APIView):
    def post(self, request, format=None):
        return Response("OK")
    

class refresh(APIView):
    def post(self, request, format=None):
        return Response("OK")


class users_list(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = UserPagination

class user_details(mixins.RetrieveModelMixin,
              mixins.UpdateModelMixin,
              generics.GenericAPIView):
    '''
        Handle single user details.

        Methods:
            - GET: Return user information
            - PUT: Update all user information
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

class me(generics.RetrieveAPIView):
    '''
        Return authenticated user or 401.
    '''
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
    