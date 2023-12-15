from django.db import models
from accounts.models import Student
from createQuiz.models import ClassList


# Create your models here.
class EnrolledClasses(models.Model):
    enClassID = models.AutoField(primary_key=True)
    dateEnrolled = models.DateTimeField()
    studentID = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    classID = models.ForeignKey(ClassList, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.studentID.lastname + ', ' + self.studentID.firstname + ' - ' + self.classID.className
