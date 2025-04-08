# core/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Tag, Category
from .serializers import TagSerializer, CategorySerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]