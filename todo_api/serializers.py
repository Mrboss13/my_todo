from rest_framework import serializers
from .models import Todo

#serializer class for convert and validate data from client to database or viceversa
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id','timestamp', 'title','desc','due_date','status']