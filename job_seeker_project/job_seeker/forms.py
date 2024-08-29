from django import forms
from .models import JobSeeker,JobApplication

class JobSeekerForm(forms.ModelForm):
    class Meta:
        model = JobSeeker
        fields = ['name', 'email', 'resume']


class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['resume']