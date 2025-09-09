from django.views.decorators.csrf import csrf_exempt
from ..users.models import User
from .serializers import UserSerializer, UserDetailSerializer, UserRegisterSerializer, TaskSerializer
from .paginators import UserPagination, TaskPagination
from ..tasks.models import Task
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import mixins
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated

class register(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
            
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

    def get_serializer_class(self):
        if self.request.method in ('PUT', 'PATCH'):
            return UserSerializer
        return UserDetailSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

class me(generics.RetrieveAPIView):
    '''
        Return authenticated user or 403.
    '''
    serializer_class = UserDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
    

class tasks_list(mixins.CreateModelMixin,
                 mixins.ListModelMixin,
                 generics.GenericAPIView):
    '''
        Create or list tasks
        
        Methods:
            - GET: Return task information
            - POST: Create new task
    '''
    queryset = Task.objects.all()
    pagination_class = TaskPagination
    serializer_class = TaskSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class task_details(mixins.RetrieveModelMixin,
              mixins.UpdateModelMixin,
              mixins.DestroyModelMixin,
              generics.GenericAPIView):
    '''
        Handle single task operations.

        Methods:
            - GET: Return task information
            - PUT: Update all task information
            - PATCH: Update partial task information
            - DELETE: Remove task
    '''
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
