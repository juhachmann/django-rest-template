from django.urls import re_path
from .views import list_or_create, crud

urlpatterns = [
    re_path('books', list_or_create),
    re_path('books/<int:pk>', crud),
]
