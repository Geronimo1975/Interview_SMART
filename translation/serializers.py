# translation/serializers.py
from rest_framework import serializers
from .models import Language, TranslatedQuestion, TranslatedInterview
from accounts.serializers import UserSerializer

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['id', 'code', 'name']
        read_only_fields = ['id']

class TranslatedQuestionSerializer(serializers.ModelSerializer):
    translator_detail = UserSerializer(source='translator', read_only=True)
    language_detail = LanguageSerializer(source='language', read_only=True)
    
    class Meta:
        model = TranslatedQuestion
        fields = ['id', 'question', 'language', 'language_detail', 'text', 
                'expected']
        
class TranslatedInterviewSerializer(serializers.ModelSerializer):
    model = TranslatedInterview
    pass