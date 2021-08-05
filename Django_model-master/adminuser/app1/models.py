from django.db import models


# Create your models here.
class Student(models.Model):
    stdid=models.IntegerField()
    stdname=models.CharField(max_length=70)
    stdemail=models.EmailField(max_length=70)
    stdres=models.CharField(max_length=70)
    stdimg=models.ImageField(null=True)


class Index(models.Model):
    indid = models.IntegerField()
    indname = models.CharField(max_length=70)
    indemail = models.EmailField(max_length=70)
    indres = models.CharField(max_length=70)



class About(models.Model):
    abid = models.IntegerField()
    abname = models.CharField(max_length=70)
    abemail = models.EmailField(max_length=70)
    abres = models.CharField(max_length=70)
