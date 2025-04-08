# interviews/serializers.py
from rest_framework import serializers
from .models import (
    Question, Interview, InterviewQuestion, 
    InterviewFeedback, InterviewStatistics
)
from accounts.serializers import UserSerializer
from core.serializers import TagSerializer, CategorySerializer

class QuestionSerializer(serializers.ModelSerializer):
    category_detail = CategorySerializer(source='category', read_only=True)
    tags_detail = TagSerializer(source='tags', many=True, read_only=True)
    
    class Meta:
        model = Question
        fields = ['id', 'text', 'category', 'category_detail', 'difficulty', 
                 'expected_answer', 'created_by', 'tags', 'tags_detail',
                 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

class InterviewQuestionSerializer(serializers.ModelSerializer):
    question_detail = QuestionSerializer(source='question', read_only=True)
    
    class Meta:
        model = InterviewQuestion
        fields = ['id', 'interview', 'question', 'question_detail', 
                 'order', 'answer', 'score', 'notes', 'time_spent_seconds']
        read_only_fields = ['id']

class InterviewSerializer(serializers.ModelSerializer):
    interviewer_detail = UserSerializer(source='interviewer', read_only=True)
    candidate_detail = UserSerializer(source='candidate', read_only=True)
    tags_detail = TagSerializer(source='tags', many=True, read_only=True)
    
    class Meta:
        model = Interview
        fields = ['id', 'title', 'description', 'interviewer', 'candidate',
                 'interviewer_detail', 'candidate_detail', 'scheduled_date',
                 'duration_minutes', 'status', 'notes', 'tags', 'tags_detail',
                 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

class InterviewFeedbackSerializer(serializers.ModelSerializer):
    evaluator_detail = UserSerializer(source='evaluator', read_only=True)
    
    class Meta:
        model = InterviewFeedback
        fields = ['id', 'interview', 'evaluator', 'evaluator_detail', 
                 'overall_rating', 'strengths', 'areas_for_improvement',
                 'hire_recommendation', 'comments', 'created_at']
        read_only_fields = ['id', 'created_at']

class InterviewStatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterviewStatistics
        fields = ['id', 'interview', 'total_questions', 'questions_answered',
                 'average_score', 'total_time_seconds', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']