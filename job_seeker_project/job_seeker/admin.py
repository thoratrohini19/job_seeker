from django.contrib import admin
from .models import JobSeeker,Job,JobApplication

# Register your models here.
class JobSeekerAdmin(admin.ModelAdmin):
    list_display=['name','email','resume']

class JobAdmin(admin.ModelAdmin):
    list_display=["title","description","location","company","posted_date"]

class JobApplicationAdmin(admin.ModelAdmin):
    list_display=["job","user","resume","applied_date"]


admin.site.register(JobSeeker, JobSeekerAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(JobApplication, JobApplicationAdmin)
