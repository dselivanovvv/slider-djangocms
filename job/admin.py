from django.contrib import admin

# Register your models here.
from job.models import Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    pass