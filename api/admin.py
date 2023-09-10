from django.contrib import admin
from .models import Student, Group, Subject, CompletedTopic, Lesson, Comment, Teacher


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['username', 'name', 'family', 'average_rating', 'is_staff']
    list_filter = ['is_staff', 'groups']
    search_fields = ['username', 'name', 'family']


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(CompletedTopic)
class CompletedTopicAdmin(admin.ModelAdmin):
    list_display = ['student', 'subject', 'topic_name']


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['student', 'date', 'unit']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['lesson', 'student', 'text']


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['username', 'name', 'family_name', 'is_staff']
    list_filter = ['is_staff', 'groups']
    search_fields = ['username', 'name', 'family_name']
