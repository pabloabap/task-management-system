from ..users.models import User
from rest_framework	 import serializers
from ..tasks.models import Task, Tag

class UserRegisterSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True, required=True)

	class Meta:
		model = User
		fields = ['email', 'username', 'password']  # añade los campos que quieras mostrar

	def create(self, validated_data):

		passsword = validated_data.pop("password")	
		user = User(**validated_data)
		user.set_password(passsword)
		user.save()

		return user

class UserDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = '__all__'  # añade los campos que quieras mostrar
		read_only_fields = ['id', 'username']  # los campos que no quieres que se modifiquen vía GET/mostrar


class UserSerializer(serializers.ModelSerializer):
	created_tasks = serializers.PrimaryKeyRelatedField(many=True, queryset=Task.objects.all())
	assigned_tasks = serializers.PrimaryKeyRelatedField(many=True, queryset=Task.objects.all())
	password = serializers.CharField(write_only=True, required=True)
	class Meta:
		model=User
		fields=['id', 'username', 'password', 'created_tasks', 'assigned_tasks']
	
	def update(self, user_to_modify, validated_data):
		created_tasks_data = validated_data.pop('created_tasks', None)
		assigned_tasks_data = validated_data.pop('assigned_tasks', None)
		password = validated_data.pop('password', None)
				
		for attr, value in validated_data.items():
			setattr(user_to_modify, attr, value)

		if password:
			user_to_modify.set_password(password)

		user_to_modify.save()
				
		if created_tasks_data is not None:
			user_to_modify.created_tasks.set(created_tasks_data)
		if assigned_tasks_data is not None:
			user_to_modify.assigned_tasks.set(assigned_tasks_data)

		return user_to_modify
	


class TagSerializer(serializers.ModelSerializer):
	class Meta:
		model=Tag
		fields= ['id', 'name']

class TaskSerializer(serializers.ModelSerializer):
	created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
	tags = serializers.SlugRelatedField(many=True, queryset=Tag.objects.all(), slug_field='name')
	class Meta:
		model=Task
		fields= '__all__'