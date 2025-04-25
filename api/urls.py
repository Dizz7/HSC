from django.urls import path
from .views import CategoriaListAPIView

from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('categorias/', CategoriaListAPIView.as_view(), name='api_categorias'),
    
]
