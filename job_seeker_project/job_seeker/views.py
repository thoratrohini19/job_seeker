
from .forms import JobSeekerForm,JobApplicationForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Job, JobApplication


def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = JobSeekerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('job_list')
    else:
        form = JobSeekerForm()
    return render(request, 'signup.html', {'form': form})


def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'job_list.html', {'jobs': jobs})

def job_detail(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.user = request.user
            application.save()
            return redirect('job_list')
    else:
        form = JobApplicationForm()
    return render(request, 'job_detail.html', {'job': job, 'form': form})