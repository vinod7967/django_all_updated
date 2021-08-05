from django.db import models
# one to one relationship
from django.db.models import manager


class user(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
class student(models.Model):
    user = models.OneToOneField(user,on_delete=models.CASCADE,parent_link=False)
    roll = models.CharField(max_length=20)
    subj_name = models.CharField(max_length=20)
# many to one relationship
class user1(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
class student1(models.Model):
    user = models.ForeignKey(user1,on_delete=models.CASCADE)
    roll = models.CharField(max_length=20)
    subj_name = models.CharField(max_length=20)
# many to many relationship
class user2(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
class student2(models.Model):
    user = models.ManyToManyField(user2)
    roll = models.CharField(max_length=20)
    subj_name = models.CharField(max_length=20)
# Create your models here.
class man(models.Model):
    name = models.CharField(max_length=20)
    roll = models.IntegerField()
    student = models.Manager()