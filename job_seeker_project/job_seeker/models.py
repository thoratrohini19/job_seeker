from django.db import models

# Create your models here.

class JobSeeker(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    resume = models.FileField(upload_to='resumes/')

    def __str__(self):
        return self.name
    
class Job(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    posted_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class JobApplication(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)  # Assuming you are using Django's default User model
    resume = models.FileField(upload_to='applications/')
    applied_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Application by {self.user.username} for {self.job.title}"