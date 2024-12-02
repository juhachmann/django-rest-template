from django.urls import re_path, include

urlpatterns = [
    re_path('auth', include('token_auth.urls')),
    re_path('', include('library.urls')),
]
