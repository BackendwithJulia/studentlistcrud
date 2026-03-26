from django.db import models

class Student(models.Model):
    student_id = models.CharField(max_length=20)
    student_name = models.CharField(max_length=100)
    student_email = models.EmailField()
    student_contact = models.CharField(max_length=20)

    def __str__(self):
        return self.student_name