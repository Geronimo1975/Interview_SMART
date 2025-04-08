# accounts/views.py
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import User, UserSkill
from .serializers import UserSerializer, UserSkillSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    
    @action(detail=True, methods=['get', 'post'])
    def skills(self, request, pk=None):
        user = self.get_object()
        
        if request.method == 'GET':
            skills = UserSkill.objects.filter(user=user)
            serializer = UserSkillSerializer(skills, many=True)
            return Response(serializer.data)
        
        elif request.method == 'POST':
            serializer = UserSkillSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user=user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)