from django.db import models
class abs_info(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    class Meta:
        abstract = True
class dept(abs_info):
    deptname = models.CharField(max_length=50)
    age = None
class emp(abs_info):
    sal = models.IntegerField()

class mul_info(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
class ano_table(mul_info):
    salary = models.IntegerField()
class proyx_info(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
class stu(proyx_info):
    class Meta:
        proxy = True
# Create your models here.
