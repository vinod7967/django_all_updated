from django.contrib import admin
from .models import employee
class employeeAdmin(admin.ModelAdmin):
    admin.site.register(employee)
# Register your models here.
