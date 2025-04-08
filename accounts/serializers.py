# accounts/serializers.py
from rest_framework import serializers
from .models import User, UserSkill

class UserSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSkill
        fields = ['id', 'name', 'level']
        read_only_fields = ['id']

class UserSerializer(serializers.ModelSerializer):
    skills = UserSkillSerializer(many=True, read_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 
                 'user_type', 'phone_number', 'profile_picture', 
                 'position', 'department', 'bio', 'preferred_language', 'skills']
        read_only_fields = ['id']
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = super().create(validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user