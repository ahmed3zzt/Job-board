from django.shortcuts import render
from .models import Job
# Create your views here.


def job_list(request):
    jobList = Job.objects.all()
    context = {
        'jobs': jobList
    }

    return render(request, 'job/job_list.html', context)


def job_detail(request, pk):
    job = Job.objects.get(id=pk)

    context = {
        'job': job
    }

    return render(request, 'job/job_detail.html', context)
