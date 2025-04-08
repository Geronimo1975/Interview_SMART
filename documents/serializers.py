# documents/serializers.py
from rest_framework import serializers
from .models import Document, Template
from accounts.serializers import UserSerializer
from core.serializers import TagSerializer, CategorySerializer

class DocumentSerializer(serializers.ModelSerializer):
    owner_detail = UserSerializer(source='owner', read_only=True)
    tags_detail = TagSerializer(source='tags', many=True, read_only=True)
    category_detail = CategorySerializer(source='category', read_only=True)
    
    class Meta:
        model = Document
        fields = ['id', 'title', 'description', 'file', 'document_type', 'owner', 
                 'owner_detail', 'tags', 'tags_detail', 'category', 'category_detail',
                 'is_template', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

class TemplateSerializer(serializers.ModelSerializer):
    creator_detail = UserSerializer(source='creator', read_only=True)
    tags_detail = TagSerializer(source='tags', many=True, read_only=True)
    category_detail = CategorySerializer(source='category', read_only=True)
    
    class Meta:
        model = Template
        fields = ['id', 'name', 'description', 'content', 'creator', 'creator_detail',
                 'category', 'category_detail', 'tags', 'tags_detail', 
                 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']