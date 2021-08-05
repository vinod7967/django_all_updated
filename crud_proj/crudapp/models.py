from django.db import models
class StudentModel(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    ch = [('1', 'O'), ('2', 'A')]
    blood_group = models.CharField(max_length=20,verbose_name='Blood Group',choices=ch,default='1')
    ge = [('1', 'Male'), ('2', 'Female')]
    gender = models.CharField(max_length=20,choices=ge,default='1')
    address = models.TextField()
# Create your models here.
