# interviews/models.py
from django.db import models
from django.conf import settings
from core.models import TimeStampedModel, Tag, Category

class Question(TimeStampedModel):
    DIFFICULTY_CHOICES = (
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    )
    
    text = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default='medium')
    expected_answer = models.TextField(blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    
    def __str__(self):
        return self.text[:50]

class Interview(TimeStampedModel):
    STATUS_CHOICES = (
        ('scheduled', 'Scheduled'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    )
    
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    interviewer = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='conducted_interviews'
    )
    candidate = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='received_interviews'
    )
    scheduled_date = models.DateTimeField()
    duration_minutes = models.IntegerField(default=60)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='scheduled')
    notes = models.TextField(blank=True)
    questions = models.ManyToManyField(Question, through='InterviewQuestion')
    tags = models.ManyToManyField(Tag, blank=True)
    
    def __str__(self):
        return f"{self.title} - {self.candidate.username}"

class InterviewQuestion(models.Model):
    interview = models.ForeignKey(Interview, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0)
    answer = models.TextField(blank=True)
    score = models.IntegerField(null=True, blank=True, choices=[(i, i) for i in range(1, 6)])
    notes = models.TextField(blank=True)
    time_spent_seconds = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return f"Q{self.order}: {self.question.text[:30]}"
        
    class Meta:
        ordering = ['order']
        unique_together = ['interview', 'question']

class InterviewFeedback(TimeStampedModel):
    interview = models.ForeignKey(Interview, on_delete=models.CASCADE, related_name='feedbacks')
    evaluator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    overall_rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    strengths = models.TextField(blank=True)
    areas_for_improvement = models.TextField(blank=True)
    hire_recommendation = models.BooleanField(default=False)
    comments = models.TextField(blank=True)
    
    def __str__(self):
        return f"Feedback for {self.interview}"

class InterviewStatistics(models.Model):
    interview = models.OneToOneField(Interview, on_delete=models.CASCADE, related_name='statistics')
    total_questions = models.IntegerField(default=0)
    questions_answered = models.IntegerField(default=0)
    average_score = models.FloatField(null=True, blank=True)
    total_time_seconds = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Stats for {self.interview}"