from django.db import models
from accounts.models import Teacher


# Create your models here.
class ClassList(models.Model):
    classID = models.AutoField(primary_key=True)
    className = models.CharField(max_length=50, null=True)
    subject = models.CharField(max_length=50, null=True)
    section = models.CharField(max_length=15, null=True)
    enrollKey = models.CharField(max_length=20, null=True)
    teacherID = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.className + ', ' + self.subject


class TopicList(models.Model):
    topicID = models.AutoField(primary_key=True)
    topicName = models.CharField(max_length=50, null=True)
    topicDescription = models.CharField(max_length=50, null=True)
    classID = models.ForeignKey(ClassList, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.topicName


class QuizList(models.Model):
    quizID = models.AutoField(primary_key=True)
    quizName = models.CharField(max_length=50, null=True)
    quizDescription = models.CharField(max_length=50, null=True)
    topicID = models.ForeignKey(TopicList, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.quizName


class QuestionSet(models.Model):
    questionID = models.AutoField(primary_key=True)
    qName = models.CharField(max_length=50, null=True)
    qDescription = models.CharField(max_length=50, null=True)
    choiceA = models.CharField(max_length=50, null=True)
    choiceB = models.CharField(max_length=50, null=True)
    choiceC = models.CharField(max_length=50, null=True)
    choiceD = models.CharField(max_length=50, null=True)
    answer = models.CharField(max_length=5, null=True)
    quizID = models.ForeignKey(QuizList, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.qName
