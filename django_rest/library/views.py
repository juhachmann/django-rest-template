from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Book
from .serializers import BookSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(['GET', 'POST'])
def list_or_create(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializers = BookSerializer(books, many=True)
        return Response({"Books" : serializers.data}, status = status.HTTP_200_OK)
    
    elif request.method == 'POST':
        return create(request=request)


@api_view(['GET', 'PUT', 'DELETE'])
def crud(request, pk):
    if request.method == 'GET':
        book = get_object_or_404(Book, id=pk)
        serializers = BookSerializer(book)
        return Response(serializers.data, status = status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        update(request=request, pk=pk)

    elif request.method == 'DELETE':
        delete(request=request, pk=pk)


@authentication_classes([TokenAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def create(request): 
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid(): 
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
     

@authentication_classes([TokenAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def update(request, pk): 
    book = get_object_or_404(Book, id=pk)
    serializer = BookSerializer(book, data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"book" : serializer.data}, status = status.HTTP_200_OK)
    return Response({"errors" : serializer.errors}, status = status.HTTP_400_BAD_REQUEST)


@authentication_classes([TokenAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def delete(request, pk): 
    book = get_object_or_404(Book, id=pk)
    book.delete()
    return Response(status = status.HTTP_204_NO_CONTENT)