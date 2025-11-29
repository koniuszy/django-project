from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register viewsets
router = DefaultRouter()
router.register(r'books', views.BookViewSet, basename='book')
router.register(r'authors', views.AuthorViewSet, basename='author')

urlpatterns = [
    path('', views.api_root, name='api-root'),
    path('', include(router.urls)),
]
