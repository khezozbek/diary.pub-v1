from rest_framework import serializers
from .models import Student, Group, Subject, CompletedTopic, Lesson, Comment, Teacher

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user
        return data


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'family', 'img', 'groups', 'achieved_results', 'average_rating']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'name']


class CompletedTopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompletedTopic
        fields = ['id', 'student', 'subject', 'topic_name']


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'student', 'date', 'unit', 'grammar', 'vocabulary', 'homework']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'lesson', 'student', 'text']


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'name', 'family_name', 'picture', 'groups', 'class_start_time']
