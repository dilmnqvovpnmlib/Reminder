from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import LectureViewSet, ProfessorViewSet, TaskViewSet, Test

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'lectures', LectureViewSet)
router.register(r'professors', ProfessorViewSet)

urlpatterns = [
    path('test/', Test.as_view()),
    path('', include(router.urls)),
]
