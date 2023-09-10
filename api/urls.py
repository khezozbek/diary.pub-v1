from django.urls import path
from .views import (
    StudentList, StudentDetail,
    GroupList, GroupDetail,
    SubjectList, SubjectDetail,
    CompletedTopicList, CompletedTopicDetail,
    LessonList, LessonDetail,
    CommentList, CommentDetail,
    TeacherList, TeacherDetail, CustomTokenObtainPairView,
)

urlpatterns = [
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('students/', StudentList.as_view(), name='student-list'),
    path('students/<int:pk>/', StudentDetail.as_view(), name='student-detail'),

    path('groups/', GroupList.as_view(), name='group-list'),
    path('groups/<int:pk>/', GroupDetail.as_view(), name='group-detail'),

    path('subjects/', SubjectList.as_view(), name='subject-list'),
    path('subjects/<int:pk>/', SubjectDetail.as_view(), name='subject-detail'),

    path('completed-topics/', CompletedTopicList.as_view(), name='completed-topic-list'),
    path('completed-topics/<int:pk>/', CompletedTopicDetail.as_view(), name='completed-topic-detail'),

    path('lessons/', LessonList.as_view(), name='lesson-list'),
    path('lessons/<int:pk>/', LessonDetail.as_view(), name='lesson-detail'),

    path('comments/', CommentList.as_view(), name='comment-list'),
    path('comments/<int:pk>/', CommentDetail.as_view(), name='comment-detail'),

    path('teachers/', TeacherList.as_view(), name='teacher-list'),
    path('teachers/<int:pk>/', TeacherDetail.as_view(), name='teacher-detail'),
]