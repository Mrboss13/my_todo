# importing classes for this view
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


# class based views for crud operation

class TodoViewSet(viewsets.ViewSet):
    def list(self,request):
        todo = Todo.objects.all()
        serializer = TodoSerializer(todo, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        id = pk
        if id is not None:
            todo = Todo.objects.get(id=id)
            serializer = TodoSerializer(todo)
            return Response(serializer.data)

    def create(self, request):
        d = request.data['due_date']
        timestamp = date.today()
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response({'msg':'Todo created succesfull!..'},status=status.HTTP_201_CREATED) 
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk):
        id = pk
        due_date = request.data['due_date']
        d = date.today()
        todo = Todo.objects.get(id=id)
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data update succesfully!..'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self,request,pk):
        id = pk
        todo = Todo.objects.get(id=id)
        serializer = TodoSerializer(todo, data=request.data , partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'partial data update succesfully!..'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk):
        id = pk
        todo = Todo.objects.get(id=id)
        todo.delete()
        return Response({'msg':'data deleted succesfully!.....'})    
    
    # objects for authentication in client side
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
