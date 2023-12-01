from django.urls import path
from . import views


urlpatterns = [
    path('quizzes/', views.quizPage, name='quizPage'),
]
