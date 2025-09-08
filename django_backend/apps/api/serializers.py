from .models import User
from rest_framework	 import serializers
from ..tasks.models import Task

class UserSerializer(serializers.ModelSerializer):
	created_tasks = serializers.PrimaryKeyRelatedField(many=True, queryset=Task.objects.all())
	assigned_tasks = serializers.PrimaryKeyRelatedField(many=True, queryset=Task.objects.all())
	password = serializers.CharField(write_only=True, required=True)
	class Meta:
		model=User
		fields=['id', 'username', 'password', 'created_tasks', 'assigned_tasks']

	def create(self, validated_data):
		created_tasks_data = validated_data.pop('created_tasks', [])
		assigned_tasks_data = validated_data.pop('assigned_tasks', [])
		
		passsword = validated_data.pop("password")	
		user = User(**validated_data)
		user.set_password(passsword)
		user.save()

		if created_tasks_data:
			user.created_tasks.set(created_tasks_data)
		if assigned_tasks_data:
			user.assigned_tasks.set(assigned_tasks_data)

		return user
	
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