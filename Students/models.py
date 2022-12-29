from django.db import models

# Create your models here.
class StudentData(models.Model):
    student_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    phone_no = models.PositiveIntegerField(null=True, blank=True)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.student_name

    def GetStudentByUsername(username):
        try:
            return StudentData.objects.get(username=username)
        except:
            return False

# class StudentEnrollement(models.Model):

