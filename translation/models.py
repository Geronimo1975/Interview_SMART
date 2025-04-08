# translation/models.py
from django.db import models
from django.conf import settings
from core.models import TimeStampedModel
from interviews.models import Question, Interview

class Language(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class TranslatedQuestion(TimeStampedModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='translations')
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    text = models.TextField()
    expected_answer = models.TextField(blank=True)
    translator = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_NULL, 
        null=True, 
        related_name='translated_questions'
    )
    
    def __str__(self):
        return f"{self.question.text[:30]} ({self.language.code})"
    
    class Meta:
        unique_together = ['question', 'language']

class TranslatedInterview(TimeStampedModel):
    interview = models.ForeignKey(Interview, on_delete=models.CASCADE, related_name='translations')
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    translator = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_NULL, 
        null=True, 
        related_name='translated_interviews'
    )
    
    def __str__(self):
        return f"{self.interview.title} ({self.language.code})"
    
    class Meta:
        unique_together = ['interview', 'language']