from django.urls import path
from . import views


urlpatterns = [
    path('student/', views.studentPage, name='studentPage'),
    path('enrollclass/<int:id>', views.enrollClassInfo, name='enrollClassInfo'),
    path('student/classview/<int:id>', views.studentClassView, name='studentClassView'),
    path('student/classview/exam/<int:id>', views.studentExam, name='studentExam'),
]
