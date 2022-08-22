from django.db import models


# Create your models here.
class StudentModel(models.Model):
    roll = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    class_name = models.CharField(max_length=10)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)

