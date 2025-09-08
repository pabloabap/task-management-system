from django.views.decorators.csrf import csrf_exempt
from ..users.models import User
from ..users.serializers import UserSerializer
from ..users.paginators import UserPagination
from ..tasks.models import Task
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import mixins
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated

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
    permission_classes = [IsAuthenticatedOrReadOnly]

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
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

class me(generics.RetrieveAPIView):
    '''
        Return authenticated user or 403.
    '''
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
    

    