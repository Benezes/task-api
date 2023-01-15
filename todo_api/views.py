from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from todo_api.serializers import TaskSerializer
from todo_api.models import Task

class TaskView(APIView):
    
    def get(self, request):
        queryset = Task.objects.all()
        serializer = TaskSerializer(queryset, many=True)
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response(serializer.data ,status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        queryset = Task.objects.get(pk=id)

        if queryset.completed:
            return Response({"message":"task is already completed"}, status=status.HTTP_400_BAD_REQUEST)
        
        queryset.completed = True
        queryset.save()
        
        serializer = TaskSerializer(queryset, many=False)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        queryset = Task.objects.get(pk=id)
        serializer = TaskSerializer(queryset, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data ,status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        queryset = Task.objects.get(pk=id)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)