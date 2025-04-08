# interviews/views.py
from rest_framework import viewsets, filters, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import (
    Question, Interview, InterviewQuestion, 
    InterviewFeedback, InterviewStatistics
)
from .serializers import (
    QuestionSerializer, InterviewSerializer, InterviewQuestionSerializer,
    InterviewFeedbackSerializer, InterviewStatisticsSerializer
)

class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['text', 'category__name', 'tags__name']
    ordering_fields = ['created_at', 'difficulty']
    
    def get_queryset(self):
        return Question.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class InterviewViewSet(viewsets.ModelViewSet):
    serializer_class = InterviewSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description', 'candidate__username', 'interviewer__username']
    ordering_fields = ['scheduled_date', 'created_at']
    
    def get_queryset(self):
        user = self.request.user
        if user.user_type == 'admin':
            return Interview.objects.all()
        elif user.user_type == 'interviewer':
            return Interview.objects.filter(interviewer=user)
        else:  # candidate
            return Interview.objects.filter(candidate=user)
    
    @action(detail=True, methods=['get', 'post'])
    def questions(self, request, pk=None):
        interview = self.get_object()
        
        if request.method == 'GET':
            questions = InterviewQuestion.objects.filter(interview=interview)
            serializer = InterviewQuestionSerializer(questions, many=True)
            return Response(serializer.data)
        
        elif request.method == 'POST':
            serializer = InterviewQuestionSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(interview=interview)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=['get', 'post'])
    def feedback(self, request, pk=None):
        interview = self.get_object()
        
        if request.method == 'GET':
            feedback = InterviewFeedback.objects.filter(interview=interview)
            serializer = InterviewFeedbackSerializer(feedback, many=True)
            return Response(serializer.data)
        
        elif request.method == 'POST':
            serializer = InterviewFeedbackSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(interview=interview, evaluator=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InterviewQuestionViewSet(viewsets.ModelViewSet):
    serializer_class = InterviewQuestionSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        if user.user_type == 'admin':
            return InterviewQuestion.objects.all()
        elif user.user_type == 'interviewer':
            return InterviewQuestion.objects.filter(interview__interviewer=user)
        else:  # candidate
            return InterviewQuestion.objects.filter(interview__candidate=user)

class InterviewFeedbackViewSet(viewsets.ModelViewSet):
    serializer_class = InterviewFeedbackSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        if user.user_type == 'admin':
            return InterviewFeedback.objects.all()
        elif user.user_type == 'interviewer':
            return InterviewFeedback.objects.filter(evaluator=user)
        else:  # candidate
            return InterviewFeedback.objects.filter(interview__candidate=user)
    
    def perform_create(self, serializer):
        serializer.save(evaluator=self.request.user)

class InterviewStatisticsViewSet(viewsets.ModelViewSet):
    serializer_class = InterviewStatisticsSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        if user.user_type == 'admin':
            return InterviewStatistics.objects.all()
        elif user.user_type == 'interviewer':
            return InterviewStatistics.objects.filter(interview__interviewer=user)
        else:  # candidate
            return InterviewStatistics.objects.filter(interview__candidate=user)