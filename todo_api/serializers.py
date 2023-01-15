from rest_framework import serializers
from todo_api.models import Task


class TaskSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    description = serializers.CharField()
    completed = serializers.BooleanField()

    class Meta:
        fields = ('id', 'title', 'description', 'completed')

    def create(self, task):
        return Task.objects.create(**task)
    
    def update(self, instance, task):
        instance.title = task.get('title', instance.title)
        instance.description = task.get('description', instance.description)
        instance.completed = task.get('completed', instance.completed)
        instance.save()
        return instance