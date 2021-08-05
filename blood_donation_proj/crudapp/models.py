from django.db import models
class StudentModel(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    ch = [('O+','O+'), ('A+','A+'),('B+','B+'),('AB+','AB+'),('O-','O-'), ('A-','A-'),('B-','B-'),('AB-','AB-')]
    blood_group = models.CharField(max_length=20,verbose_name='Blood Group',choices=ch,default='1')
    ge = [('male', 'Male'), ('female', 'Female')]
    gender = models.CharField(max_length=20,choices=ge,default='1')
    address = models.TextField()
# Create your models here.
