from django.urls import path
from . import views


urlpatterns = [
    path('classes/', views.classPage, name='classPage'),
    path('createClass/', views.createClassPage, name='createClass'),
    path('classInfo/<int:id>', views.classInfo, name='classInfo'),
    path('topicInfo/<int:id>', views.topicInfo, name='topicInfo'),
    path('quizSet/<int:id>', views.quizSet, name='quizSet'),

    path('deleteQuestion/<int:id>', views.deleteQuestion, name="deleteQuestion"),
    path('updateQuestion/<int:id>', views.updateQuestion, name="updateQuestion"),
    path('updateClass/<int:id>', views.updateClass, name="updateClass"),
    path('updateTopic/<int:id>', views.updateTopic, name="updateTopic"),
]
