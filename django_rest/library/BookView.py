from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer

class BookView (APIView):

    def get(self, request):
        return 
    
    def post(self, request):
        return 