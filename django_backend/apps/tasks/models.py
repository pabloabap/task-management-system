from django.db import models
from django.conf import settings


# Create your models here.
class Comment(models.Model):
	task = models.ForeignKey('Task', on_delete=models.CASCADE, related_name='comments')
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
	content = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return (
			f"Author:	{self.author}\n"
			f"Task:		{self.task}n"
			f"Contnent:	{self.content}\n"
			f"Created At:	{self.created_at}\n"
	)

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
			f"Name:			{self.name}\n"
			f"Created At:	{self.created_at}\n"
		)

class Task(models.Model):
	STATUS_CHOICES = [
		('TODO', 'To Do'),
		('INPR', 'In Progress'),
		('DONE', 'Done'),
		('CANC', 'Cancelled'),
	]
	PRIORITY_CHOICES = [
		('LOW', 'Low'),
		('MED', 'Medium'),
		('HIGH', 'High'),
		('CRIT', 'Critical'),
	]
	title = models.CharField(max_length=200)
	description = models.TextField()
	status = models.CharField(choices=STATUS_CHOICES)
	priority = models.CharField(choices=PRIORITY_CHOICES)
	due_date = models.DateTimeField()
	estimated_hours = models.DecimalField(max_digits=5, decimal_places=2)
	actual_hours = models.DecimalField(max_digits=5, decimal_places=2, null=True)
	# Relationships
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='created_tasks')
	assigned_to = models.ManyToManyField(settings.AUTH_USER_MODEL, default=None)
	tags = models.ManyToManyField(Tag, blank=True)
	parent_task = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
	# Metadata
	metadata = models.JSONField(default=dict)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	is_archived = models.BooleanField(default=False)

	def __str__(self):
		return ( 
			f"Title:			{self.title}\n"
			f"Description:		{self.description}\n"
			f"Status:			{self.status}\n"
			f"Priority:		{self.priority}\n"
			f"Due Date:		{self.due_date}\n"
			f"Estimated Hours:	{self.estimated_hours}\n"
			f"Actual Hours:		{self.actual_hours}	\n"
			f"Created By:		{self.created_by}\n"
			f"Assigned To:		{', '.join(user.username for user in self.assigned_to.all())}\n"
			f"Tags:				{', '.join(tag.name for tag in self.tags.all())}\n"
			f"Parent Task:		{self.parent_task}\n"
			f"Metadata:		{self.metadata}\n"
			f"Created At:		{self.created_at}\n"
			f"Updated At:		{self.updated_at}\n"
			f"Is Archived:		{self.is_archived}\n"
		)
      
class TaskAssignment(models.Model):
	task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='assignments')
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='task_assignments')
	assigned_at = models.DateTimeField(auto_now_add=True)
	assigned_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_tasks')

	def __str__(self):
		return f"{self.user} assigned to {self.task} at {self.assigned_at}"

class TaskHistory(models.Model):
    """Audit log for task changes"""
    ACTION_CHOICES = [
        ('CREATE', 'Created'),
        ('UPDATE', 'Updated'),
        ('ASSIGN', 'Assigned'),
        ('UNASSIGN', 'Unassigned'),
        ('STATUS_CHANGE', 'Status Changed'),
        ('COMMENT', 'Comment Added'),
        ('ARCHIVE', 'Archived'),
        ('RESTORE', 'Restored'),
    ]
    
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='history')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=20, choices=ACTION_CHOICES)
    field_name = models.CharField(max_length=50, blank=True)  # Campo que cambió
    old_value = models.TextField(blank=True)
    new_value = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-timestamp']
    
    def __str__(self):
        return f"{self.action} on {self.task.title} by {self.user}"